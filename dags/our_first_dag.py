from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'haldi',
    'retries': 3,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    default_args={
        'owner': 'haldi',
        'retries': 3,
        'retry_delay': timedelta(minutes=2)
    },
    dag_id="our_first_dag_112d",
    description="This is our first DAG",
    start_date=datetime(2022, 10, 31, 11),
    schedule=timedelta(days=1)

) as dag:
    task1 = BashOperator(
        task_id="first_task",
        bash_command="echo hello ajc"
    )
