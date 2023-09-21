# Airflow Scripts

This repository contains DAGs from Airflow. It includes tutorials and sandboxes from first steps on Airflow (it starts with hello-*.py) as well as some small projects integrating multiple steps for learning. This repository will be updated periodically to aggregate my learnings on Airflow.

## hello-world.py

This DAG is from the official tutorial, it has 3 tasks using BashOperator.

## hello-postgres.py

This DAG uses the PostgresOperator to:
1. Create a table on PostgreSQL database (if the table doesn't exist)
2. Add a row to this table, with a log event string and a datestamp.