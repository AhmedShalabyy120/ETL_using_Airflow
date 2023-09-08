from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import os
import pandas as pd
import shutil

def transform_data():
    # Loading Data
    booking = pd.read_csv('/opt/airflow/data/booking.csv')
    client = pd.read_csv('/opt/airflow/data/client.csv')
    hotel = pd.read_csv('/opt/airflow/data/hotel.csv')

    # Merging Data
    data = pd.merge(booking, client, on="client_id")
    data.rename(columns={"Name": "Client_Name", 'type': 'Client_Type'}, inplace=True)

    data = pd.merge(data, hotel, on="hotel_id")
    data.rename(columns={'name': 'Hotel_Name'}, inplace=True)

    # Save the transformed data to a CSV file in a shared volume
    data.to_csv('/opt/airflow/data/generated_data.csv', index=False)

default_args = {
    "owner": 'airflow',
    "start_date": datetime(2023, 9, 9)
}

dag = DAG(
    dag_id='ahmed5',
    default_args=default_args,
    description="First Dag from flat file to postgres sql",
    catchup=False,
    schedule_interval=timedelta(days=1)
)

Task_1 = PythonOperator(
    task_id="transform_data",
    python_callable=transform_data,
    dag=dag
)

# Add a task to copy the generated data file to a shared volume
def copy_data_to_local():
    shutil.copy('/opt/airflow/data/generated_data.csv', 'E:\Data')

copy_task = PythonOperator(
    task_id="copy_data_to_local",
    python_callable=copy_data_to_local,
    dag=dag
)

Task_1 >> copy_task  # Set the order of task execution
