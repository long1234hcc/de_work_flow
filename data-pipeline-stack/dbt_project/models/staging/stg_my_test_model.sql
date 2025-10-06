-- models/stg_my_first_model.sql

{{
  config(
    materialized='table',
    engine='ReplacingMergeTree(created_at)',
    order_by='(user_id, created_at)',
    settings={
      'index_granularity': 8192
    }
  )
}}

SELECT
    1 AS user_id,
    'John Doe test' AS user_name,
    'active' AS status,
    NOW() AS created_at

UNION ALL

SELECT
    2 AS user_id,
    'Jane Smith  test' AS user_name,
    'inactive' AS status,
    NOW() AS created_at