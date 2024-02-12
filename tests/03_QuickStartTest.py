import time
from locust import HttpUser, task, between, constant

class QuickstartUser(HttpUser):
    wait_time = constant(10) # delay 10secs after each task.
    fixed_count = 3

    @task(10)
    def hello_world(self):
        self.client.get("/home")
        # self.stop()

    @task
    def view_items(self):
        for item_id in range(10):
            self.client.get(f"/item?id={item_id}", name="/item")
            # self.stop()

            # time.sleep(1)

    def on_start(self):
        print('===on start====')
        self.client.post("/login", json={"username":"foo", "password":"bar"})