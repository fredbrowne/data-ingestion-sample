{{ config(materialized='table') }}

with avg_trips_per_region AS(
  SELECT 
    region
    ,DATE_TRUNC(DATE(datetime), WEEK(MONDAY)) AS Week_Of_Trip
    ,COUNT(*) AS Visit
  FROM {{ ref('stg_trips') }}
  GROUP BY
    region
    ,Week_Of_Trip
  ORDER BY 
    Week_Of_Trip
)
SELECT 
  Week_of_Trip
  ,region
  ,AVG(Visit) Avg_Per_Week
FROM avg_trips_per_region
GROUP BY
  Week_Of_Trip
  ,region
