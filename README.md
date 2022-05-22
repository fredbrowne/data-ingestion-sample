# data-ingestion-sample
Basic Pipeline process designed to ingest data on-demand


# Manual Ingestion Execution Steps

Create and activate your virtual environment:
`python3 -m venv venv` && `source venv/bin/activate`

Install requirements.txt:
`pip install requirements.txt`

Set execute permission to the following file:
`chmod +x manual_ingestion.sh`

Create your `gcloud` key:
`export GOOGLE_APPLICATION_CREDENTIALS="/home/fredbrowne/Development/Github/data-ingestion-sample/data-ingestion-sample1-03dbf59b9e68.json"`

Start the process by running:
`./manual_ingestion.sh`

