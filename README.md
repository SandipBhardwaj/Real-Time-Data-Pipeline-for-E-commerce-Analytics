Real-Time Data Pipeline for E-commerce Analytics

Overview

This project demonstrates an end-to-end real-time data analytics pipeline for e-commerce, built with Python. It covers the generation of mock data, data ingestion, cleaning, aggregation, analytics, ETL orchestration, dashboard reporting, and storage using PostgreSQL. Modern tools like Apache Airflow (for orchestration) and Streamlit (for interactive dashboards) are integrated.

Features:

Mock Data Generation: Create realistic users, products, and orders using Python.

Data Ingestion: Read raw CSV data for flexible, reproducible ETL.

Data Cleaning & Enrichment: Pre-process, merge, and validate datasets.

Data Aggregation: Summarize sales, trends, and user behaviors.

Database Integration: Store clean and analytical tables in PostgreSQL.

ETL Orchestration: Schedule and manage the data pipeline with Apache Airflow.

Interactive Dashboard: Visualize KPIs, trends, and tables in Streamlit.

Alerting & Monitoring: (Optional) Set up email/Slack notifications for pipeline health.

Project Structure:-

REAL-TIME DATA PIPELINE FOR E-commerce Analytics/
│
├── Csv-files/
│   ├── main.py         # Mock data generation
│   ├── users.csv
│   ├── products.csv
│   └── orders.csv
│
├── Data_ingestion/
│   └── main.py         # Data ingestion scripts
│
├── Data_process_Cleaning/
│   └── main.py         # Data cleaning & preprocessing
│
├── Data_aggre_Analytics/
│   └── main.py         # Data aggregation/analytics
│
├── Data_Visualize/
│   └── dashboard.py    # Streamlit dashboard for visualization
│
├── ELT_Orchestration/
│   └── main.py         # Airflow DAGs/automation scripts
│
├── daily_sales.csv         # Example output
├── sales_per_product.csv   # Example output

Tech Stack :-

Python & Pandas

PostgreSQL (database/data warehouse)

Apache Airflow (ETL orchestration)

Streamlit (interactive dashboard)
├── products.csv
├── users.csv
├── orders.csv
└── README.md

How to Run
1. Clone the repository
bash
git clone https://github.com/yourusername/ecommerce-data-pipeline.git
cd ecommerce-data-pipeline
2. Install dependencies
bash
pip install -r requirements.txt
(Add Streamlit, pandas, SQLAlchemy, psycopg2, and Airflow to your requirements.txt)

3. Generate Mock Data
bash
python Csv-files/main.py

4. Run ETL Pipeline
Manually:
Run scripts in Data_ingestion, Data_process_Cleaning, Data_aggre_Analytics.

Automated (Airflow):
Start Airflow and schedule/run DAG in ELT_Orchestration/main.py.

5. Store in PostgreSQL
Make sure your database credentials are configured in the scripts.

6. Start Dashboard
bash
streamlit run Data_Visualize/dashboard.py

Example Outputs
Top-Selling Products

Revenue Trends

User Order Table

Screenshots and charts will appear in your Streamlit dashboard!

License
MIT

Author:
Sandip Bhardwaj
