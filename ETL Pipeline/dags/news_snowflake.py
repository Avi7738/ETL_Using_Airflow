from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import requests, json, re
import snowflake.connector

# -----------------------------
# Snowflake Config
# -----------------------------
SNOWFLAKE_CONFIG = {
    "user": "AVINASH",
    "password": "cYmHtAqNM6FNqU3",
    "account": "nscziip-bj25145",
    "warehouse": "AIRFLOW_WH",
    "database": "AIRFLOW_DB",
    "schema": "PUBLIC",
    "role": "ACCOUNTADMIN"
}

# -----------------------------
# Step 1: Extract
# -----------------------------
def extract_news():
    url = "https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey=fb037a4a2ef144ad8efada0fa3fdd8da"
    response = requests.get(url)
    data = response.json()
    with open('/tmp/news_raw.json', 'w') as f:
        json.dump(data['articles'], f)

# -----------------------------
# Step 2: Transform
# -----------------------------
def clean_text(text):
    return re.sub(r'<[^>]*>', '', text).strip()

def transform_news():
    with open('/tmp/news_raw.json', 'r') as f:
        raw_data = json.load(f)

    transformed = []
    for article in raw_data:
        transformed.append({
            "title": clean_text(article.get("title", "")),
            "description": clean_text(article.get("description", "")),
            "url": article.get("url", ""),
            "published_at": article.get("publishedAt", "")
        })

    with open('/tmp/news_transformed.json', 'w') as f:
        json.dump(transformed, f)

# -----------------------------
# Step 3: Load to Snowflake
# -----------------------------
def load_to_snowflake():
    conn = snowflake.connector.connect(
        user=SNOWFLAKE_CONFIG['user'],
        password=SNOWFLAKE_CONFIG['password'],
        account=SNOWFLAKE_CONFIG['account'],
        warehouse=SNOWFLAKE_CONFIG['warehouse'],
        database=SNOWFLAKE_CONFIG['database'],
        schema=SNOWFLAKE_CONFIG['schema'],
        role=SNOWFLAKE_CONFIG['role']
    )
    cur = conn.cursor()

    # Create warehouse, database, schema, table
    cur.execute("CREATE WAREHOUSE IF NOT EXISTS AIRFLOW_WH WAREHOUSE_SIZE = 'XSMALL'")
    cur.execute("CREATE DATABASE IF NOT EXISTS AIRFLOW_DB")
    cur.execute("USE DATABASE AIRFLOW_DB")
    cur.execute("CREATE SCHEMA IF NOT EXISTS PUBLIC")
    cur.execute("USE SCHEMA PUBLIC")
    cur.execute("""
        CREATE TABLE IF NOT EXISTS TECH_NEWS (
            TITLE STRING,
            DESCRIPTION STRING,
            URL STRING,
            PUBLISHED_AT TIMESTAMP
        )
    """)

    with open('/tmp/news_transformed.json', 'r') as f:
        news_data = json.load(f)

    for article in news_data:
        cur.execute("""
            INSERT INTO TECH_NEWS (TITLE, DESCRIPTION, URL, PUBLISHED_AT)
            VALUES (%s, %s, %s, %s)
        """, (
            article['title'],
            article['description'],
            article['url'],
            article['published_at']
        ))

    conn.commit()
    cur.close()
    conn.close()

# -----------------------------
# DAG Definition
# -----------------------------
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

with DAG(
    dag_id='news_etl_to_snowflake',
    default_args=default_args,
    description='ETL: Fetch tech news and load into Snowflake',
    start_date=datetime(2025, 6, 30),
    schedule_interval='@hourly',
    catchup=False
) as dag:

    t1 = PythonOperator(
        task_id='extract_news',
        python_callable=extract_news
    )

    t2 = PythonOperator(
        task_id='transform_news',
        python_callable=transform_news
    )

    t3 = PythonOperator(
        task_id='load_to_snowflake',
        python_callable=load_to_snowflake
    )

    t1 >> t2 >> t3
