from locust import HttpUser, task, events

class HelloWorldUser(HttpUser):
    fixed_count = 2 # exactly 2 users spawned to run all these tasks. Each user can run tasks many times.

    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")


@events.test_start.add_listener
def ggg(environment, **kwargs):
    pass

@events.init.add_listener
def fff(environment, **kwargs):
    pass