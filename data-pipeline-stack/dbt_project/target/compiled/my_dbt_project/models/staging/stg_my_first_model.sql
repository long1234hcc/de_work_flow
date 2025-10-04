-- models/stg_my_first_model.sql



SELECT
    1 AS user_id,
    'John Doe' AS user_name,
    'active' AS status,
    NOW() AS created_at

UNION ALL

SELECT
    2 AS user_id,
    'Jane Smith' AS user_name,
    'inactive' AS status,
    NOW() AS created_at