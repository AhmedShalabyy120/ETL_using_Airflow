# ETL using Apache Airflow

This project demonstrates an ETL (Extract, Transform, Load) process using Apache Airflow to import data from CSV files, perform data transformation by merging tables into one, and export the resulting data back to your local host.

## Table of Contents

- [Overview](#overview)
- [Setup](#setup)
- [Tasks](#tasks)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview

In this project, we use Apache Airflow to perform the following tasks:

1. **Task 1: Transform and Merge Data** - We insert CSV files and merge multiple tables into one table using Python operators.

2. **Task 2: Export Data to Local Host** - After data transformation, we export the resulting data to your local host using a Python operator.

## Setup

### Prerequisites

Before getting started, ensure that you have the following prerequisites installed on your system:

- Docker
- Apache Airflow

### Docker Setup

This project uses Docker containers for Apache Airflow. You can set up Docker for your project environment.

## Tasks

### Task 1: Transform and Merge Data

- Python Operator: `transform_data`
- Description: Loads data from CSV files (e.g., `booking.csv`, `client.csv`, `hotel.csv`), merges the tables into one, and saves the transformed data to a shared volume.

### Task 2: Export Data to Local Host

- Python Operator: `copy_data_to_local`
- Description: Copies the transformed data from the shared volume to your local host (e.g., `E:\Data`).

## Usage

Follow these steps to run the ETL process:

1. Start Docker containers for Apache Airflow.

2. Access the Apache Airflow web UI to trigger the DAG (Directed Acyclic Graph, which represents the ETL workflow) and monitor the tasks' progress.

3. Task 1 will load and transform the data from CSV files, and Task 2 will export the transformed data to your local host.

4. You can schedule or manually trigger the DAG to execute the ETL process as needed.

## Contributing

Contributions and improvements are welcome! If you'd like to contribute to this project, follow these steps:

1. Fork the repository.

2. Create a new branch for your feature or enhancement.

3. Make your changes and commit them.

4. Push your changes to your fork.

5. Submit a pull request to the main repository to collaborate on improving this project.

