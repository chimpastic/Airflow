from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator

# need to mention teh owner, retries amd retry delay
default_args = {
    'owner': 'Pythonowner',
    'retries': 3,
    'retry_delay': timedelta(minutes=2)
}

# This fucntion will be executed


def welcome():
    print("welcome to airflow")


with DAG(
    default_args=default_args,
    dag_id="our_first_dag_1.2",
    description="This is our first DAG",
    start_date=datetime(2022, 10, 31, 11),
    schedule=timedelta(days=1)

) as dag:
    task1 = PythonOperator(
        task_id="welcome",

        # fuction name in python callable
        python_callable=welcome
    )
