# 🌀 News ETL Pipeline 

This project extracts tech news from NewsAPI, processes it using Python, and loads it into Snowflake — all automated with Apache Airflow running in Docker.

---

## ⚙️ Tech Stack

- Docker  
- Apache Airflow  
- Python  
- Snowflake  
- Power BI (for dashboard)

---

## 📁 Project Structure
```
ETL Pipeline
├── dags/
│   └── news_etl_to_snowflake.py         # Main DAG definition
│             └── extract                # Extract data from NewsAPI
|                 transform              # Clean and normalize article data
|                 load                   # Load data into PostgreSQL
│
├── docker-compose.yml          # Runs Airflow + Scheduler
├── requirements.txt            # Python dependencies
├── .env                        # API keys and DB credentials
└── README.md                   # You're here

```
---

## 🔐 .env File Format

```env
NEWS_API_KEY=your_api_key
SNOWFLAKE_USER= XYZ
SNOWFLAKE_PASSWORD=your_password
SNOWFLAKE_ACCOUNT=XXXXXXXXXXXX
SNOWFLAKE_WAREHOUSE=AIRFLOW_WH
SNOWFLAKE_DATABASE=AIRFLOW_DB
SNOWFLAKE_SCHEMA=PUBLIC
```

# 🚀 How to Run
```
git clone https://github.com/YOUR_USERNAME/news-etl-airflow.git
cd news-etl-airflow
docker-compose up airflow-init
docker-compose up -d
```

Open Airflow: http://localhost:8080
Login: airflow
Password: airflow
Enable & Trigger DAG: news_etl_to_snowflake

# ❄️ Snowflake Table: TECH_NEWS

| Column        | Type      |
| ------------- | --------- |
| TITLE         | STRING    |
| DESCRIPTION   | STRING    |
| URL           | STRING    |
| PUBLISHED\_AT | TIMESTAMP |

# 📊 Power BI

- Connect to Snowflake

- Server: SNOWFLAKE_ACCOUNT.snowflakecomputing.com

- Table: TECH_NEWS

- Use DirectQuery for live dashboard



