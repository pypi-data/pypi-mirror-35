"""
Standalone python package meant to be sent to gc to test the package in
cluster condition of dataproc.
"""


def all_types_df_for_live_test():
    """
    make a diverse schema for live tests.

    Returns:
        pyspark.sql.DataFrame: DataFrame with many different type of data.

    """
    import decimal
    import datetime
    from pyspark.sql.types import StringType
    from pyspark.sql.types import StructField
    from pyspark.sql.types import StructType
    from pyspark.sql.types import DecimalType
    from pyspark.sql.types import TimestampType
    from pyspark.sql.types import DateType
    from pyspark.sql.types import LongType
    from pyspark.sql.types import DoubleType
    from optel.datalake.config.sparksession import default_spark

    sparksession = default_spark()
    values = [
        (
            datetime.datetime.now(),
            datetime.date.today(),
            "HELLO WORLD THIS IS A STRING",
            decimal.Decimal(10.15984567),
            1056659845,
            10.5555555555,
        ),
        (
            datetime.datetime.now(),
            datetime.date.today(),
            "HELLO WORLD THIS IS A STRING",
            decimal.Decimal(10.15984567),
            1056659845,
            0.05654,
        )
    ]
    schema = StructType(
        [
            StructField("datetime", TimestampType()),
            StructField("date", DateType()),
            StructField("string", StringType()),
            StructField("decimal", DecimalType(28, 16)),
            StructField("long", LongType()),
            StructField("double", DoubleType()),
        ]
    )
    return sparksession.createDataFrame(values, schema)


def bq_client():
    """gives the bigquery client"""
    from google.cloud import bigquery
    return bigquery.Client()


def big_query(live_test_name):
    """gives the parameters to use for live big query tests"""
    dataset_id = "test2"
    bucket_id = "optel-datalake"
    table_id = live_test_name
    return {"name": table_id, "dataset": dataset_id, "bucket": bucket_id}


def write_to_elastic_test(all_types_df):
    """try to write to elastic with the diverse schema."""
    from optel.datalake import ingest

    destination = "test_datalake"
    username = ""
    password = ""
    nodes = "10.200.12.10"
    all_types_df.show()
    ingest.write_to_elastic(
        all_types_df, destination, nodes, username, password
    )


def live_bq_write_test(all_types_df, big_query, bq_client):
    """Try to write to big query for real"""
    import optel.datalake.big_query as odbq

    odbq.write_to_bigquery(
        all_types_df,
        big_query["name"],
        dataset=big_query["dataset"],
        bucket=big_query["bucket"],
    )
    dataset_ref = bq_client.dataset(big_query["dataset"])
    table_ref = dataset_ref.table(big_query["name"])
    bq_table = bq_client.get_table(table_ref)

    assert bq_table.num_rows == all_types_df.count()
    assert len(bq_table.schema) == len(all_types_df.columns)


def live_bq_append_test(all_types_df, big_query, bq_client):
    """
    try to append to big query for real.
    Also try to append with a new field.
    """
    import optel.datalake.big_query as odbq
    from pyspark.sql.functions import lit
    from pyspark.sql.functions import when

    odbq.append_to_bigquery(
        all_types_df,
        big_query["name"],
        dataset=big_query["dataset"],
        bucket=big_query["bucket"],
    )
    dataset_ref = bq_client.dataset(big_query["dataset"])
    table_ref = dataset_ref.table(big_query["name"])
    bq_table = bq_client.get_table(table_ref)

    assert bq_table.num_rows == all_types_df.count() * 2
    assert len(bq_table.schema) == len(all_types_df.columns)

    new_df = all_types_df.withColumn(
        "another_col",
        when(all_types_df["double"] > 1, lit("")).otherwise(lit(None))
    )
    new_df.printSchema()

    odbq.append_to_bigquery(
        new_df,
        big_query["name"],
        dataset=big_query["dataset"],
        bucket=big_query["bucket"],
    )

    dataset_ref = bq_client.dataset(big_query["dataset"])
    table_ref = dataset_ref.table(big_query["name"])
    bq_table = bq_client.get_table(table_ref)

    assert bq_table.num_rows == all_types_df.count() * 3
    assert len(bq_table.schema) == len(all_types_df.columns) + 1


if __name__ == "__main__":
    import glob
    from subprocess import call

    distribution = glob.glob("*.tar.gz")
    virtualenv_path = "/opt/.virtualenvs/jobs-submission/bin/python"
    call(
        [
            virtualenv_path,
            "-m",
            "pip",
            "install",
            "--upgrade",
            "--force-reinstall",
            distribution[0],
        ]
    )
    test_df = all_types_df_for_live_test()
    client = bq_client()
    bq_info = big_query("test_datalake")
    live_bq_write_test(test_df, bq_info, client)
    live_bq_append_test(test_df, bq_info, client)
    write_to_elastic_test(test_df)
