from __future__ import annotations
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

# --- Best Practice: Định nghĩa các hằng số cấu hình ---
DBT_PROJECT_DIR = "/opt/dbt_project"
DBT_PROFILE_TARGET = "docker_pipeline"
# Đường dẫn hoặc tên model cần chạy
DBT_MODEL_PATH = "models/stagging/stg_my_first_model.sql"

with DAG(
    dag_id="dbt_run_specific_model",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Ho_Chi_Minh"),
    schedule=None,  # DAG này có thể chạy thủ công khi cần
    catchup=False,
    doc_md="""
    ### DAG: Run specific dbt model
    DAG này dùng để chạy **một model cụ thể** trong dự án dbt.
    - **dbt_run_specific**: Chạy model `stg_my_first_model.sql` trong thư mục staging.
    """,
    tags=["dbt", "staging", "on_demand"],
) as dag:

    dbt_run_specific = BashOperator(
        task_id="dbt_run_specific",
        bash_command=(
            f"cd {DBT_PROJECT_DIR} && "
            f"dbt run --target {DBT_PROFILE_TARGET} --select {DBT_MODEL_PATH}"
        ),
    )
