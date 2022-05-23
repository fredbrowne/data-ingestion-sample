'''
    This class is responsible for all functions related
    to data ingestion into BigQuery.

    Following functions are part of this class:

    - _retrieve_file()
    - _upload_file_gcs()
    - _get_or_create_bigquery_datasets()
    - _create_or_replace_table
'''
from gcloud import storage
from google.cloud import bigquery
from const import (
    GCP_PROJECT_ID,
    GCS_BUCKET_NAME,
    GCS_RAW_DATASET,
    get_schema,
)

class Ingestion():
    def __init__(self, file_name, field_delimiter=','):
        self.file_name = file_name
        self.field_delimiter = field_delimiter
        self.file_path = ''

    def _retrieve_file(self, path):
        self.file_path = ''.join([path,self.file_name])

    def _upload_file_gcs(self):
        '''
            Function responsible to upload the file into GCS.
        '''
        # Cloud information
        self.client = storage.Client(GCP_PROJECT_ID)

        # Get the bucket or create
        try:
            bucket = self.client.get_bucket(GCS_BUCKET_NAME)
        except:
            bucket = self.client.create_bucket(GCS_BUCKET_NAME)

        destination = '/'.join(['source1',self.file_name])
        staging = bucket.blob(destination)

        # Upload file to GCS
        staging.upload_from_filename(self.file_path)
        self.uploaded_file_URI = f'gs://{GCS_BUCKET_NAME}/{destination}'

    def _get_or_create_bigquery_datasets(self, dataset_id):
        '''
            Function responsible to set up the environment
            and create the dataset.
            Params:
                - dataset_id: dataset to be created
        '''
        client = bigquery.Client(GCP_PROJECT_ID)
        dataset_id = f"{GCP_PROJECT_ID}.{dataset_id}"
        dataset = bigquery.Dataset(dataset_id)
        dataset.location = "US"
        try:
            dataset = client.get_dataset(dataset_id)
            print("Dataset already exists {}.{}".format(
                GCP_PROJECT_ID
                ,dataset.dataset_id)
            )
        except:
            dataset = client.create_dataset(dataset, timeout=30)
            print("Created dataset {}.{}".format(
                GCP_PROJECT_ID
                ,dataset.dataset_id)
            )

    def _create_or_replace_table(self, table_id, dataset):
        '''
            Function responsible to create or replace table in the dataset.
            Params:
                - table_id: table name to retrieve schema and create in data-lake
                - dataset: dataset that will hold the table
        '''
        client = bigquery.Client(GCP_PROJECT_ID)

        full_table_id = f'{GCP_PROJECT_ID}.{GCS_RAW_DATASET}.{table_id}'

        job_config = bigquery.LoadJobConfig(
            write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE,
            schema = get_schema(table_id),
            skip_leading_rows=1,
            source_format=bigquery.SourceFormat.CSV,
        )

        #Load Job into BQ
        load_job = client.load_table_from_uri(
            self.uploaded_file_URI
            ,full_table_id
            ,job_config=job_config
        )
        
        # Wait job to finish
        load_job.result()        
        
        #Retrieve table and count
        destination_table = client.get_table(full_table_id)
        print("Table {} loaded with {} rows.".format(
                full_table_id
                ,destination_table.num_rows)
        )
