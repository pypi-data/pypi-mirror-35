import os
import pytest
import optel.datalake.big_query as odbq


def test_write_to_bigquery(mocker, false_dataframe):
    mocker.patch("optel.datalake.big_query.write_parquet")
    mocker.patch("optel.datalake.big_query.bigquery.Client")
    mocker.patch("optel.datalake.big_query.create_bq_load_job_config")
    mocker.patch("optel.datalake.big_query.cleanup")
    odbq.write_to_bigquery(
        false_dataframe, "", dataset="", bucket="", temp_zone=""
    )
    odbq.write_parquet.assert_called_with(false_dataframe, "gs://")
    odbq.create_bq_load_job_config.assert_called_with("PARQUET",
                                                      "WRITE_TRUNCATE")
    odbq.cleanup.assert_called_once()
    odbq.bigquery.Client().load_table_from_uri. \
        assert_called_with("gs://part-*",
                           odbq.bigquery.Client().dataset().table(),
                           job_config=odbq.create_bq_load_job_config(), )



def test_append_to_bigquery(mocker, false_dataframe):
    mocker.patch("optel.datalake.big_query.write_parquet")
    mocker.patch("optel.datalake.big_query.bigquery.Client")
    mocker.patch("optel.datalake.big_query.create_bq_load_job_config")
    mocker.patch("optel.datalake.big_query.cleanup")
    odbq.append_to_bigquery(
        false_dataframe, "", dataset="", bucket="", temp_zone=""
    )
    odbq.write_parquet.assert_called_with(false_dataframe, "gs://")
    odbq.create_bq_load_job_config.assert_called_with("PARQUET", "WRITE_APPEND")
    assert odbq.create_bq_load_job_config().schema_update_options == ["ALLOW_FIELD_ADDITION"]
    odbq.cleanup.assert_called_once()
    odbq.bigquery.Client().load_table_from_uri.\
        assert_called_with("gs://part-*",
                           odbq.bigquery.Client().dataset().table(),
                           job_config=odbq.create_bq_load_job_config(),)



def test_create_bq_load_job_config(mocker):
    mocker.patch("optel.datalake.big_query.bigquery.LoadJobConfig")
    config = odbq.create_bq_load_job_config("Hello", "World")
    assert config.source_format == "Hello"
    assert config.write_disposition == "World"


def test_cleanup(mocker):
    config = {
        'list_blobs.return_value': [mocker.MagicMock() for i in range(3)]
    }
    mocker.patch("optel.datalake.big_query.get_storage_bucket", **config)
    odbq.get_storage_bucket.return_value = odbq.get_storage_bucket  # hack
    odbq.cleanup("", "", "")

    # verify each MagicMock delete mock was called once
    for mock in  config['list_blobs.return_value']:
        assert mock.delete.call_count == 1


def test_sanitize_datatypes_for_big_query(all_types_df):
    df = odbq.sanitize_datatypes_for_big_query(all_types_df)
    assert 'decimal' not in [types[1] for types in df.dtypes]


def test_get_storage_bucket(mocker):
    mocker.patch("optel.datalake.big_query.storage.Client")
    odbq.get_storage_bucket("")
    odbq.storage.Client.assert_called_once()
