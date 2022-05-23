# data-ingestion-sample
Basic Pipeline process designed to ingest data on-demand


# Manual Ingestion Execution Steps

Create and activate your virtual environment:
`python3 -m venv venv` && `source venv/bin/activate`

Install requirements.txt:
`pip install requirements.txt`

Set execute permission to the following file:
`chmod +x manual_ingestion.sh`

## CLOUD CONFIGURATION

### If you have a key:

Copy the JSON key into the root folder and export your Key:

`export GOOGLE_APPLICATION_CREDENTIALS="your-key-file-name.json"`

Start the process by running:
`./manual_ingestion.sh`

### If you don't have a key

Create a Google Cloud project by following this:
`https://cloud.google.com/resource-manager/docs/creating-managing-projects#console`

Remember to create a project name called `data-ingestion-sample1`.
In the future, this project will retrieve from a single-source, making
it easier to deploy to other projects without too much manual intervention.

Create a Service Account
`https://cloud.google.com/iam/docs/creating-managing-service-accounts`

Set up a JSON Key for the Service Account
`https://cloud.google.com/iam/docs/creating-managing-service-account-keys`

Copy the JSON key into the root folder and export your Key:
`export GOOGLE_APPLICATION_CREDENTIALS="your-key-file-name.json"`

Start the process by running:
`./manual_ingestion.sh`

Running queries:

The process has now:

    - Ingested the file into Cloud Storage
    - Created the Datasets that will hold the tables in BigQuery
    - Created a raw table into BigQuery on dataset `dataset_bigquery_raw_data_lake`
    - Executed DBT to module a staging table based on the raw `trips` table.
    - Created 3 tables in VISUAL dataset:
        - avg_trips_per_region
            Weekly Average number of trips for an area, defined by region
        - cheap_mobile
            Regions that has "cheap_mobile" as datasource and the number of times it appears for each region
        - latest_datasorce
            The lastest Datasource that appeared for the two most common regions

Query away!
