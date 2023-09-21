from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator

with DAG(
    'hello-postgres',
    default_args = {
        'depends_on_past': False,
        'email': ['airflow@airflow.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes = 5)
    },
    description = 'Adding a single row to postgres database',
    schedule = timedelta(days = 1),
    start_date = datetime(2023,9,1),
    catchup = False,
    tags = ['example'],
) as dag:
    # Task
    t1 = PostgresOperator(
        task_id = 'create_log_table',
        postgres_conn_id = 'tutorial_pg_conn',
        sql = '''
            CREATE TABLE IF NOT EXISTS hello_postgres (
            "id" SERIAL PRIMARY KEY,
            "event_name" VARCHAR(50),
            "current_date" VARCHAR(50)
            );
        '''
    )

    t2 = PostgresOperator(
        task_id = 'adding_date_log',
        postgres_conn_id = 'tutorial_pg_conn',
        sql = """
        INSERT INTO hello_postgres
        VALUES (DEFAULT, 'log_event', '""" + str(datetime.now()) + """');
        """
    )

    t1 >> t2