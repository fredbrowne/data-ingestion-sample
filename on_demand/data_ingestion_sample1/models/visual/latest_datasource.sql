-- From the two most commonly appearing regions, which is the latest datasource
{{ config(materialized='table') }}

WITH two_most_common AS (
  SELECT
    region
    ,count(*) AS Number_of_Trips
    ,max(datetime) AS datetime
    ,ROW_NUMBER() OVER (ORDER BY count(*) DESC) AS ROWNUMBER
  FROM {{ ref('stg_trips') }}
  group by region
),
regions AS (
  SELECT
    region
    ,datetime
  FROM two_most_common
  WHERE ROWNUMBER <= 2
)
SELECT 
  trips.region Top_Regions
  ,trips.datasource AS Latest_Datasource
  ,trips.datetime Latest_Datetime
FROM {{ ref('stg_trips') }} trips
JOIN regions regions ON regions.region = trips.region AND regions.datetime = trips.datetime
