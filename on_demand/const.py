# Project and Bucket
GCS_PROJECT_ID = 'data-ingestion-sample1'
GCS_BUCKET_NAME = 'data-ingestion-sample1-data-lake-source-files'
# Datasets
GCS_RAW_DATASET = 'dataset_bigquery_raw_data_lake'
GCS_STAGING_DATASET = 'dataset_bigquery_staging_data_lake'
GCS_VISUAL_DATASET = 'dataset_bigquery_visual_data_lake'
# Initial File Source location
SOURCE_FILE_PATH = {
    'trips.csv':'../data-ingestion-sample/source_files/',
}

from schemas_const import (
    TRIPS_SCHEMA,
)

def get_schema(source) -> dict:
    schema = {
        "trips": TRIPS_SCHEMA,
    }
    return schema.get(source, {})
