# Start process
echo *****On Demand Ingestion process has started


# Project and Bucket
export GCP_PROJECT_ID='data-ingestion-sample1'
export GCS_BUCKET_NAME='data-ingestion-sample1-data-lake-source-files'
# Export variables for DBT use
export GCS_STAGING_DATASET=dataset_bigquery_staging_data_lake
export GCS_VISUAL_DATASET=dataset_bigquery_visual_data_lake
export GCS_RAW_DATASET=dataset_bigquery_raw_data_lake

# Call Ingestion Process
python3 on_demand/start_ingestion.py

# Call Modeling Process

echo *****On Demand Ingestion process has ended

cd on_demand/data_ingestion_sample1

dbt --no-version-check run

echo *****All tasks successfully executed.
echo *****You can query your data on https://console.cloud.google.com/bigquery?referrer=search&project=data-ingestion-sample1
echo *****Thank you and goodbye.
