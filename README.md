# ETL_Using_Airflow

# 🌀 News ETL Pipeline with Apache Airflow + Snowflake + Docker

This project builds an end-to-end automated pipeline to extract real-time tech news using a public API, transform the content, and load the data into a Snowflake table — all orchestrated using Apache Airflow inside Docker.

---

## 📦 Tech Stack

| Tool        | Role                          |
|-------------|-------------------------------|
| 🐳 Docker    | Containerization & orchestration |
| 🌀 Airflow   | Workflow scheduler for ETL     |
| 🐍 Python    | Logic: API call, JSON transform |
| ❄️ Snowflake | Cloud data warehouse           |
| 📊 Power BI  | Dashboard from Snowflake       |

---

## 🧱 Project Structure

```bash
news-etl-airflow/
├── dags/                    # Airflow DAGs
│   └── news_etl_to_snowflake.py
├── config/                  # Optional configs
├── logs/                    # Airflow logs (auto-created)
├── plugins/                 # (empty or custom plugins)
├── .env                     # Secret env variables (DO NOT commit)
├── .gitignore               # Ignore .env, logs etc.
├── docker-compose.yml       # Main Docker setup
└── README.md                # This file

