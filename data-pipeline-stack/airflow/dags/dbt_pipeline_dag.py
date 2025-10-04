from __future__ import annotations
import pendulum
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator

# --- Best Practice: Định nghĩa các hằng số cấu hình ---
# Giúp DAG dễ đọc và dễ bảo trì hơn
## Đoạn trên này test
# DBT_PROJECT_DIR = "/opt/dbt"
DBT_PROJECT_DIR = "/opt/dbt_project" 
DBT_PROFILE_TARGET = "docker_pipeline" # Target dành cho môi trường Docker

with DAG(
    dag_id="daily_dbt_pipeline",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Ho_Chi_Minh"),
    schedule="@daily",
    catchup=False,
    doc_md="""
    ### Daily dbt Pipeline
    DAG này chạy các model và test của dbt mỗi ngày.
    - **dbt_run**: Thực thi tất cả các model trong dự án.
    - **dbt_test**: Chạy tất cả các data tests sau khi model đã được build.
    """,
    tags=["dbt", "production"],
) as dag:

    # Task 1: Chạy tất cả các dbt models
    dbt_run = BashOperator(
        task_id="dbt_run",
        # Sử dụng --target để chỉ định profile cho môi trường Docker
        bash_command=(
            f"cd {DBT_PROJECT_DIR} && "
            f"dbt run --target {DBT_PROFILE_TARGET}"
        ),
    )

    # Task 2: Chạy data tests để đảm bảo chất lượng dữ liệu
    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command=(
            f"cd {DBT_PROJECT_DIR} && "
            f"dbt test --target {DBT_PROFILE_TARGET}"
        ),
    )

    dbt_run >> dbt_test