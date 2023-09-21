from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    'hello-world',
    default_args = {
        'depends_on_past': False,
        'email': ['airflow@airflow.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 1,
        'retry_delay': timedelta(minutes = 5)
    },
    description = 'A simple tutorial DAG',
    schedule = timedelta(days = 1),
    start_date = datetime(2023,9,1),
    catchup = False,
    tags = ['example'],
) as dag:
    # tasks
    t1 = BashOperator(
        task_id = 'print_date',
        bash_command = 'date',
    )

    t2 = BashOperator(
        task_id = 'sleep',
        depends_on_past = False,
        bash_command = 'sleep 5',
        retries = 3,
    )

    t3 = BashOperator(
        task_id = 'say_hi',
        bash_command = 'echo Hi',
    )

    t1 >> t2 >> t3