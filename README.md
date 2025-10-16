---

### 📝 Terminal Instructions

```bash
cd ~/airflow  # or your actual project folder
nano README.md
```

Then paste the following content:

```markdown
# 📊 Airflow + PostgreSQL ETL Pipeline

## Overview
This project orchestrates a modular ETL pipeline using Apache Airflow and PostgreSQL to ingest, transform, and store stock market data. It’s designed for reproducibility, CLI-friendly debugging, and production-grade scheduling.

## 🔧 Tech Stack
- Apache Airflow
- PostgreSQL
- Python (pandas, requests)
- SQL scripts
- Docker (optional)

## 🧩 Project Structure
```
airflow-postgress-etl/
├── dags/
├── include/sql/
├── scripts/
├── webserver_config.py
├── airflow.cfg
├── requirements.txt
└── README.md
```

## 🚀 Setup Instructions

```bash
# Clone and activate environment
git clone https://github.com/mainamuragev/airflow-postgress-etl.git
cd airflow-postgress-etl
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Initialize Airflow
export AIRFLOW_HOME=$(pwd)
airflow db init
airflow users create --username admin --password admin --role Admin \
  --email muragevincent39@gmail.com --firstname Maina --lastname Murage

# Start services
airflow webserver --port 8080
airflow scheduler

# Validate pipeline
python scripts/validate_pipeline.py
```

## 📂 DAGs Breakdown

| DAG Name              | Description                            | Schedule      |
|----------------------|----------------------------------------|---------------|
| `extract_stock_data` | Pulls raw data from external API       | Daily @ 8 AM  |
| `transform_data`     | Cleans and formats using pandas        | Daily @ 8:30 AM |
| `load_to_postgres`   | Inserts validated data into PostgreSQL | Daily @ 9 AM  |

## 🖼️ Screenshots

> Save these in `screenshots/` and reference them below.

```markdown
![DAGs Overview](./screenshots/dag-overview.png)
![Task Tree](./screenshots/task-tree.png)
![Graph View](./screenshots/graph-view.png)
![Postgres Table](./screenshots/postgres-table.png)
![Validation Output](./screenshots/validation-output.png)
```

## 🔐 Webserver Config Highlights
- Auth type: `AUTH_DB`
- CSRF protection: Enabled
- Theme: `superhero.css`
- OAuth scaffolded for Google login

## 🙌 Author
**Maina Murage** — Mechanical Engineer pivoting into Data Engineering  
📍 Nairobi, Kenya | 💻 Cohort 4 @ Lux Tech Academy  
🔗 [GitHub](https://github.com/mainamuragev) | ✉️ muragevincent39@gmail.com
```
