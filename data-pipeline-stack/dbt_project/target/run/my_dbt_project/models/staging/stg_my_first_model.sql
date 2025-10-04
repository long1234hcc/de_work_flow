
  
    
    
    
        
        insert into `default`.`stg_my_first_model__dbt_backup`
        ("user_id", "user_name", "status", "created_at")-- models/stg_my_first_model.sql



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
  
  