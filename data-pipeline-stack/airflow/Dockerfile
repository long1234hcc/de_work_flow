FROM apache/airflow:2.9.2-python3.11

# Build-time args để đồng bộ UID/GID với host
ARG AIRFLOW_UID=50000
ARG AIRFLOW_GID=50000

USER root

RUN apt-get update && apt-get install -y --no-install-recommends git && apt-get clean && rm -rf /var/lib/apt/lists/*



# Tạo tất cả thư mục cần thiết và set quyền
RUN mkdir -p /opt/dbt/logs /opt/dbt/target /opt/dbt/models \
    /opt/dbt_project/logs /opt/dbt_project/target && \
    chown -R ${AIRFLOW_UID}:${AIRFLOW_GID} /opt/dbt /opt/dbt_project && \
    chmod -R 775 /opt/dbt /opt/dbt_project

# Copy requirements
COPY requirements.txt .

# Chuyển về user airflow để pip install
USER airflow
RUN pip install --no-cache-dir -r requirements.txt

