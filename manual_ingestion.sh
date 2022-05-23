# Start process
echo *****On Demand Ingestion process has started

# Export variables for DBT use
export STAGING_DATASET_ID=dataset_bigquery_staging_data_lake
export VISUAL_DATASET_ID=dataset_bigquery_visual_data_lake
export RAW_DATASET_ID=dataset_bigquery_raw_data_lake
export GCP_PROJECT_ID='data-ingestion-sample1'
# Call Ingestion Process
python3 on_demand/start_ingestion.py

# Call Modeling Process

echo *****On Demand Ingestion process has ended

cd on_demand/data_ingestion_sample1

dbt --no-version-check run
