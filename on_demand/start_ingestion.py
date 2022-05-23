from classes.ingestion import Ingestion
from const import (
    SOURCE_FILE_PATH,
    GCS_RAW_DATASET,
    GCS_STAGING_DATASET,
    GCS_VISUAL_DATASET,
)

for filename,filepath in SOURCE_FILE_PATH.items():
    # Start process
    ingestion_process = Ingestion(filename, ',')

    # Retrieve file to be sent to GCS
    ingestion_process._retrieve_file(filepath)

    # Upload file to GCS    
    ingestion_process._upload_file_gcs()

    # Create datasets
    ingestion_process._get_or_create_bigquery_datasets(GCS_RAW_DATASET)
    ingestion_process._get_or_create_bigquery_datasets(GCS_STAGING_DATASET)
    ingestion_process._get_or_create_bigquery_datasets(GCS_VISUAL_DATASET)

    # Load CSV into Raw Dataset
    table_id = filename[:-4]

    ingestion_process._create_or_replace_table(table_id, GCS_RAW_DATASET)

    # End of Ingestion
