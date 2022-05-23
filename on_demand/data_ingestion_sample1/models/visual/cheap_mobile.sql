-- What regions has the `cheap_mobile` datasource appeared in?
{{ config(materialized='table') }}

SELECT 
  region
  ,count(*) Cheap_Mobile_Count
FROM {{ ref(stg_trips) }}
WHERE datasource = 'cheap_mobile'
group by region
