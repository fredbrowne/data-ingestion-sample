{{ config(materialized='table') }}

WITH trips as (
  SELECT
    region
    ,SPLIT(REPLACE(REPLACE(origin_coord, 'POINT (', ''), ')', ''), ' ')[OFFSET(1)] AS origin_coord_lat
    ,SPLIT(REPLACE(REPLACE(origin_coord, 'POINT (', ''), ')', ''), ' ')[OFFSET(0)] AS origin_coord_lon
    ,SPLIT(REPLACE(REPLACE(destination_coord, 'POINT (', ''), ')', ''), ' ')[OFFSET(1)] AS destination_coord_lat
    ,SPLIT(REPLACE(REPLACE(destination_coord, 'POINT (', ''), ')', ''), ' ')[OFFSET(0)] AS destination_coord_lon
    ,datetime
    ,datasource
  FROM {{ source('raw' , 'trips' )}}
)
SELECT * FROM trips
ORDER BY
  origin_coord_lat
  ,origin_coord_lon
  ,destination_coord_lat
  ,destination_coord_lon
  ,datetime
