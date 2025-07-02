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
```

#🚀 How to Run the Project
## ✅ Step 1: Clone the Repository

git clone https://github.com/YOUR_USERNAME/news-etl-airflow.git
cd news-etl-airflow

## ✅ Step 2: Add .env File
Create a .env file in the root as shown above with your News API key and Snowflake credentials.

## ✅ Step 3: Start Docker Environment

docker-compose up airflow-init     # Run once to initialize metadata DB
docker-compose up -d               # Starts Airflow webserver & scheduler

## ✅ Step 4: Open Airflow UI
Go to http://localhost:8080
Login with:

Username: airflow
Password: airflow

## ✅ Step 5: Trigger the ETL DAG

In the Airflow UI, locate DAG news_etl_to_snowflake

Turn it ON

Click ▶️ Trigger DAG

Monitor logs to confirm success

# 🌀 Airflow DAG Workflow
This DAG automates the following ETL steps:

Step	Task ID	Description
Extract news	extract_news	Calls News API for latest tech headlines
Transform data	transform_news	Cleans HTML tags and prepares JSON
Load to Snowflake	load_to_snowflake	Creates table (if not exists) and inserts rows

# ❄️ Snowflake Table: TECH_NEWS
Column	Type	Description
TITLE	STRING	News article title
DESCRIPTION	STRING	News summary
URL	STRING	Link to the original article
PUBLISHED_AT	TIMESTAMP	Date/time of article publication

📊 Power BI Integration
You can connect Power BI directly to Snowflake to build real-time dashboards.

🧩 Steps to Connect:
Open Power BI Desktop

Click Get Data → Snowflake

Fill the following fields:

Field	Value
Server	nscziip-bj25145.snowflakecomputing.com
Warehouse	AIRFLOW_WH
Database	AIRFLOW_DB
Schema	PUBLIC

Select the table: TECH_NEWS

Choose DirectQuery for live updates

Build visuals:

📋 Table: news headlines + links

📈 Line chart: published_at vs count

🧠 Add filters by title/description/date

💡 Future Improvements
Add NLP sentiment analysis using HuggingFace or Spark NLP

Load enriched data into TECH_NEWS_ENRICHED

Add alerting (Slack/Email) for specific keyword-based news

Add Streamlit or Flask dashboard on top of Snowflake

Switch from batch to real-time Kafka ingestion

👨‍💻 Author
Avinash Rajbhar
Data Engineer | ETL & Dashboard Automator | Real-Time Pipeline Builder
Made with ❤️ using Docker, Python, Airflow & Snowflake

yaml
Copy
Edit

---

✅ Ab bhai tu yeh full `README.md` copy-paste kar de GitHub repo me — tera project ready hai interview, demo, or showcase ke liye 💯

Bol — chahiye kya:
- `.env.example`
- `docker-compose.yml`
- DAG file cleanup
- Power BI `.pbix` file template?

Main ready hoon 💥
