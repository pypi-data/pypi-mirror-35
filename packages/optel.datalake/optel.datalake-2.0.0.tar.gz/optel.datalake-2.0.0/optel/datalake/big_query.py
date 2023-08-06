import os
import re
from concurrent.futures import TimeoutError
from google.cloud import bigquery
from google.cloud import storage
from google.cloud.bigquery import job
from google.cloud import exceptions

from optel.datalake.ingest import write_parquet
from optel.datalake.sanity_checks import convert_decimal_to_float


def write_to_bigquery(
    df, table_name, *, dataset, bucket, temp_zone="pyspark/tmp"
):
    """
    Write a pyspark dataframe to google BigQuery. It uses a temporary folder
    in a google cloud storage bucket to do the operation. It then deletes
    everything it just wrote.

    .. Note: Needs to be run from a google cloud compute engine with access
             to google cloud storage and google big query.

    Args:
        df (pyspark.sql.DataFrame): DataFrame to write to BigQuery.
        table_name (str): Name to use in BigQuery.
        bucket (str): Google Cloud Storage Bucket to use for the temp folder.
        dataset (str): Name of the dataset in BigQuery.
        temp_zone (str): Name of the temp folder we'll use as staging.
    """
    bq_client = bigquery.Client()
    bq_dataset = bq_client.dataset(dataset)

    job_config = create_bq_load_job_config("PARQUET", "WRITE_TRUNCATE")

    _transfer_to_google_big_query(
        df, bucket, temp_zone, table_name, bq_dataset, job_config, bq_client
    )


def append_to_bigquery(
    df, table_name, *, dataset, bucket, temp_zone="pyspark/tmp"
):
    """
    Append pyspark dataframe to a google BigQuery table. The schema must
    be the same or have new nullable fields.
    It uses a temporary folder in a google cloud storage bucket to do the
    operation. It then deletes everything it just wrote.

    .. Note: Needs to be run from a google cloud compute engine with access
             to google cloud storage and google big query.

    Args:
        df (pyspark.sql.DataFrame): DataFrame to write to BigQuery.
        table_name (str): Name to use in BigQuery.
        bucket (str): Google Cloud Storage Bucket to use for the temp folder.
        dataset (str): Name of the dataset in BigQuery.
        temp_zone (str): Name of the temp folder we'll use as staging.
    """

    bq_client = bigquery.Client()
    bq_dataset = bq_client.dataset(dataset)

    job_config = create_bq_load_job_config("PARQUET", "WRITE_APPEND")
    job_config.schema_update_options = [
        job.SchemaUpdateOption.ALLOW_FIELD_ADDITION
    ]

    _transfer_to_google_big_query(
        df, bucket, temp_zone, table_name, bq_dataset, job_config, bq_client
    )


def _transfer_to_google_big_query(
        df, bucket, temp_zone, table_name, bq_dataset, job_config, bq_client
):
    table_name = sanitize_name_for_big_query(table_name)
    parquet_destination = os.path.join("gs://", bucket, temp_zone, table_name)

    df = sanitize_datatypes_for_big_query(df)
    write_parquet(df, parquet_destination)

    try:
        load_job = bq_client.load_table_from_uri(
            os.path.join("gs://", bucket, temp_zone, table_name, "part-*"),
            bq_dataset.table(table_name),
            job_config=job_config,
        )
        load_job.result()
    except exceptions.GoogleCloudError as e:
        raise e
    except TimeoutError as te:
        raise te
    finally:
        cleanup(bucket, temp_zone, table_name)


def sanitize_name_for_big_query(table_name):
    """
    Remove illegal characters from a table name.

    >>> sanitize_name_for_big_query('my_table')
    'my_table'
    >>> sanitize_name_for_big_query('test-datalake')
    'testdatalake'
    >>> sanitize_name_for_big_query('t1e5s&t-.+_data($)lake')
    't1e5st_datalake'

    Args:
        table_name (str): Table name in sanitize.

    Returns:
        str: sanitized table name ready to used as a name in big query.

    """
    return re.sub(r'\W+', '', table_name)


def sanitize_datatypes_for_big_query(df):
    """
    Big Query support decimal of scale(38,9) while spark supports (38,37).
    When inferred from schema, it will be (38, 18) which is not supported by
    big query, so we cast it as float...

    Args:
        df (pyspark.sql.DataFrame):

    Returns:
        pyspark.sql.DataFrame: dataframe with no decimal type.

    """
    df = convert_decimal_to_float(df)
    return df


def create_bq_load_job_config(source_format, write_disposition):
    config = bigquery.LoadJobConfig()
    config.source_format = source_format
    config.write_disposition = write_disposition
    return config


def cleanup(bucket, temp_zone, table_name):
    storage_bucket = get_storage_bucket(bucket)
    temp_blobs = storage_bucket.list_blobs(
        prefix=os.path.join(temp_zone, table_name)
    )
    for blob in temp_blobs:
        blob.delete()


def get_storage_bucket(bucket):
    storage_client = storage.Client()
    return storage_client.bucket(bucket)
