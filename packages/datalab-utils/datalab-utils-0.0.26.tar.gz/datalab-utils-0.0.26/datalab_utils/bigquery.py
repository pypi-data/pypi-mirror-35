import codecs
import io
import os
import pandas as pd
import random
import tempfile
import uuid

from google.cloud import bigquery, storage


def execute_bq(project_id,
               query,
               destination_project=None,
               destination_dataset=None,
               destination_table=None,
               create_disposition='CREATE_IF_NEEDED',
               write_disposition='WRITE_TRUNCATE'):
    print('Executing (on project %s):\n%s' % (project_id, query))
    client = bigquery.Client(project=project_id)
    job_config = bigquery.QueryJobConfig()
    job_config.use_legacy_sql = False

    if destination_dataset and destination_table:
        print('Writing results to: %s.%s.%s' % (project_id, destination_dataset, destination_table))
        dataset_ref = client.dataset(destination_dataset, project=destination_project or project_id)
        table_ref = dataset_ref.table(destination_table)
        job_config.destination = table_ref
        job_config.allow_large_results = True
        job_config.create_disposition = create_disposition
        job_config.write_disposition = write_disposition

    job = client.query(query, job_config=job_config)
    job.result()


def to_gbq(df,
           project_id,
           dataset_id,
           table_id,
           write_disposition='WRITE_EMPTY',
           create_disposition='CREATE_IF_NEEDED',
           schema=None):
    if df.empty:
        print('DataFrame is empty, skipping load')
        return

    if schema:
        columns = list(schema.keys())
        df = df[columns]

    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id, project=project_id)
    table_ref = dataset_ref.table(table_id)

    print('Loading DataFrame to %s' % table_ref)
    temporary_local_file = os.path.join(tempfile.gettempdir(), str(uuid.uuid4()) + '.csv')
    try:
        print('Creating temporary %s' % temporary_local_file)
        df.to_csv(temporary_local_file, index=False, encoding='utf-8')
        rb_file = codecs.open(temporary_local_file, 'rb', encoding='utf-8')
        print('Loading temporary csv to %s' % table_ref)
        job_config = bigquery.LoadJobConfig()
        job_config.encoding = 'UTF-8'
        job_config.source_format = 'CSV'
        job_config.write_disposition = write_disposition
        job_config.create_disposition = create_disposition
        job_config.schema = _create_bq_schema(schema) if schema else _extract_bq_schema(df)
        job_config.skip_leading_rows = 1
        job = client.load_table_from_file(rb_file, table_ref, job_config=job_config)
        job.result()
        print('DataFrame loaded to %s' % table_ref)
    finally:
        os.remove(temporary_local_file)


def read_gbq(
        query,
        project_id,
        tmp_bucket=None,
        tmp_dataset=None):
    if tmp_bucket and tmp_dataset:
        return _read_gbq_with_temporary_storage(query, project_id, tmp_bucket, tmp_dataset)
    else:
        return _read_gbq_direct(query, project_id)


def _read_gbq_with_temporary_storage(query, project_id, tmp_bucket, tmp_dataset):
    tmp_table = random.randint(0, 9999999999)
    execute_bq(project_id, query, destination_dataset=tmp_dataset, destination_table=tmp_table)
    df = read_gbq_table(project_id, tmp_dataset, tmp_table, tmp_bucket)
    _delete_bq_table(project_id, tmp_dataset, tmp_table)
    return df


def _read_gbq_direct(query, project_id):
    job_config = bigquery.QueryJobConfig()
    job_config.flatten_results = True

    print('Executing %s' % query)
    client = bigquery.Client(project=project_id)
    job = client.query(query, job_config)
    results = job.result()

    print('Fetching results')
    rows = list(results)
    fields = [field.to_api_repr() for field in results.schema]
    columns = [field['name'] for field in fields]
    return pd.DataFrame.from_records(rows, columns=columns)


def read_gbq_table(
        project_id,
        dataset_id,
        table_id,
        temporary_bucket_name='temporary_work',
        facturation_project_id=None,
        tqdm=None):
    work_directory = _extract_bq_table(project_id, dataset_id, table_id, temporary_bucket_name, facturation_project_id)
    columns = _table_columns(project_id, dataset_id, table_id)
    df = _load_from_storage(project_id, temporary_bucket_name, work_directory, columns, tqdm)
    _delete_bucket_data(project_id, temporary_bucket_name, work_directory)
    return df


def _extract_bq_table(project_id, dataset_id, table_id, bucket_name, facturation_project_id):
    work_directory = str(uuid.uuid4())
    facturation_project_id = facturation_project_id or project_id

    # Prepare extract job
    client = bigquery.Client(project=facturation_project_id)
    dataset_ref = client.dataset(dataset_id, project=project_id)
    table_ref = dataset_ref.table(table_id)
    gs_uri = "gs://{}/{}/part_*.csv.gz".format(bucket_name, work_directory)
    extract_conf = bigquery.ExtractJobConfig()
    extract_conf.compression = 'GZIP'
    extract_conf.destination_format = 'CSV'
    extract_conf.print_header = False

    # Ensure bucket exists
    location = client.get_dataset(dataset_ref).location
    _ensure_bucket(project_id, bucket_name, location)

    print('Extracting table %s to %s' % (table_ref, gs_uri))
    extract_job = client.extract_table(table_ref, gs_uri, job_config=extract_conf)
    extract_job.result()
    _check_job_status(extract_job)
    return work_directory


def _table_columns(project_id, dataset_id, table_id):
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id, project=project_id)
    table_ref = dataset_ref.table(table_id)
    dtype_map = {'STRING': 'str', 'INTEGER': 'float64', 'FLOAT': 'float64', 'BOOLEAN': 'bool', 'TIMESTAMP': 'M8[ns]', 'RECORD': 'object'}
    return [
        [field.name, dtype_map[field.field_type]]
        for field in client.get_table(table_ref).schema
    ]


def _load_from_storage(project_id, bucket_name, work_directory, columns, tqdm):
    client = storage.client.Client(project=project_id)
    bucket = storage.bucket.Bucket(client, bucket_name)
    parts = list(bucket.list_blobs(prefix=work_directory + "/"))
    parts = tqdm(parts) if tqdm else parts
    raw_data = []
    print('Loading DataFrame from %s files in gs://%s/%s' % (len(parts), bucket_name, work_directory))
    for part in parts:
        df = _load_part(part, columns)
        raw_data.append(df)
    final = pd.concat(raw_data)
    return final


def _load_part(blob, columns):
    content = blob.download_as_string()
    names = [c[0] for c in columns]
    dtype = dict(columns)
    return pd.read_csv(io.BytesIO(content), names=names, dtype=dtype, compression='gzip')


def _ensure_bucket(project_id, bucket_name, location):
    client = storage.client.Client(project=project_id)
    bucket = storage.bucket.Bucket(client, bucket_name)
    bucket.location = location
    if not bucket.exists():
        print('Creating bucket gs://%s (location: %s)' % (bucket_name, location))
        bucket.create()
    return bucket


def _delete_bucket_data(project_id, bucket_name, work_directory):
    client = storage.client.Client(project=project_id)
    bucket = storage.bucket.Bucket(client, bucket_name)
    blobs = list(bucket.list_blobs(prefix=work_directory + "/"))

    print('Deleting %s files in gs://%s/%s' % (len(blobs), bucket_name, work_directory))
    bucket.delete_blobs(blobs)


def _delete_bq_table(project_id, dataset_id, table_id):
    print('Deleting %s.%s.%s' % (project_id, dataset_id, table_id))
    client = bigquery.Client(project=project_id)
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)
    client.delete_table(table_ref)


def _create_bq_schema(columns):
    return [
        bigquery.SchemaField(column_name, bq_type)
        for column_name, bq_type in columns.items()
    ]


def _get_bq_type(dtype):
    return {
        'i': 'INTEGER',
        'b': 'BOOLEAN',
        'f': 'FLOAT',
        'O': 'STRING',
        'S': 'STRING',
        'U': 'STRING',
        'M': 'TIMESTAMP'
    }.get(dtype.kind, 'STRING')


def _extract_bq_schema(df):
    return [
        bigquery.SchemaField(column_name, _get_bq_type(dtype))
        for column_name, dtype in df.dtypes.iteritems()
    ]


def _check_job_status(job):
    error_result = job.error_result
    if error_result:
        raise RuntimeError('Could not execute operation: %s' % error_result.get('message', ''))
