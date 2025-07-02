# ETL_Using_Airflow

# 🌀 News ETL Pipeline with Airflow, Snowflake & Docker

This project extracts news via API, applies NLP sentiment analysis, and stores results in Snowflake. Built with Airflow inside Docker and visualized via Power BI.

## 🔧 Tech Stack

- Apache Airflow (via Docker)
- Python (ETL + NLP)
- Snowflake (Data Warehouse)
- Power BI (Dashboard)

## 🚀 How to Run

1. Create a `.env` file (see `.env.example`)
2. Start services:
   ```bash
   docker-compose up --build
