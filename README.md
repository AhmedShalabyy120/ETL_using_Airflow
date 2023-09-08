# Airflow Data Transformation and Export

This repository contains an Apache Airflow DAG (Directed Acyclic Graph) for performing data transformation and exporting the generated data to a local directory. The DAG uses various Airflow operators to read CSV files, perform data transformations using Python, and then export the resulting data as a CSV file to a specified location.

## Prerequisites

Before running the Airflow DAG, make sure you have the following prerequisites:

- Apache Airflow installed and configured
- Docker installed on your machine
- Python 

## DAG Operators

This project utilizes the following Apache Airflow DAG operators:

- **PythonOperator**: The `PythonOperator` is used to execute Python functions within the DAG. In this project, it is used to run the `transform_data` function for data transformation.

- **PythonOperator**: Another `PythonOperator` is used to run the `copy_data_to_local` function, which copies the generated data file to a local directory.
