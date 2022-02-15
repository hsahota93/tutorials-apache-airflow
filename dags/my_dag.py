from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime
from random import randint

# Just return a random number between 1 and 10
def _training_model():
    return randint(1, 10)


# Get the results from each task and check which one had the highest value. Use that value
# to determine which task to call
def _best_model(ti):

    results = ti.xcom_pull(task_ids=[
        'model_A',
        'model_B',
        'model_C'
    ])

    best_accuracy = max(results)
    if (best_accuracy > 8):
        return 'accurate'
    return 'inaccurate'


with DAG("my_dag", start_date=datetime(2022, 1, 1), schedule_interval="*/15 * * * *", catchup=False) as dag:

    model_A = PythonOperator(
        task_id="model_A",
        python_callable=_training_model
    )

    model_B = PythonOperator(
        task_id="model_B",
        python_callable=_training_model
    )

    model_C = PythonOperator(
        task_id="model_C",
        python_callable=_training_model
    )

    best_model = BranchPythonOperator(
        task_id="best_model",
        python_callable=_best_model
    )

    accurate = BashOperator(
        task_id="accurate",
        bash_command="echo 'It was above 8'"
    )

    inaccurate = BashOperator(
        task_id="inaccurate",
        bash_command="echo 'It was below 8'"
    )

# Building out the graph
[model_A, model_B, model_C] >> best_model >> [accurate, inaccurate]
