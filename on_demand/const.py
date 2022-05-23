# Project and Bucket
import os
GCP_PROJECT_ID = os.getenv('GCP_PROJECT_ID')
GCS_BUCKET_NAME = os.getenv('GCS_BUCKET_NAME')

# Datasets
GCS_RAW_DATASET = os.getenv('GCS_RAW_DATASET')
GCS_STAGING_DATASET = os.getenv('GCS_STAGING_DATASET')
GCS_VISUAL_DATASET = os.getenv('GCS_VISUAL_DATASET')

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
