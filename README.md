# tutorials-apache-airflow
This repo is being used to track any tutorials/learnings related to Apache Airflow

# Setup

## Prerequisites

Requires the following:

1. Docker
2. Docker Compose

Follow the below steps to setup the environment:

1. Run `docker-compose up airflow-init` (you should only need to do this once)
2. Run `docker-compose up -d`
3. Wait for all containers to be up and running (3 might say unhealthy)
    a. You can check the status with `docker container ls -a`

# Links

* https://airflow.apache.org/docs/apache-airflow/stable/start/docker.html
* https://www.youtube.com/watch?v=IH1-0hwFZRQ