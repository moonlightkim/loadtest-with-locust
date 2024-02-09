# Overview
This project showcases how to use Locust to do Performance Testing
- Tool: Locust https://locust.io/

# Prerequisite
- Install pipenv: https://pipenv.pypa.io/en/latest/installation.html

# Setup
- Install dependecies
    ```
    pipenv install
    ```
- Run Locust
    ```
    pipenv run locust -f tests --class-picker
    ```

- Open web app - http://0.0.0.0:8089