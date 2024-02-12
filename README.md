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

# Config in a file
Define all configs for running CLI in a file makes running command faster. Here is how:
- Create a config file: [locust.conf](tests/locust.conf)
- Run in terminal:
    ```
    pipenv run locust -f tests --config tests/locust.conf
    ```

# Distributed Testing
Locust makes it easier to run distributed testing than JMeter. Here is how:
- On master machine's terminal run:
    ```
    pipenv run locust -f tests --master
    ```

- On worker machine's terminal run:
    ```
    pipenv run locust -f tests --worker --master-host <ip-addr>
    ```

- [Reference](https://docs.locust.io/en/stable/running-distributed.html#)


# Locust event and eventhook
- [Reference](https://docs.locust.io/en/stable/writing-a-locustfile.html#events)