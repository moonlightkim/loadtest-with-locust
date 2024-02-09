from locust import SequentialTaskSet, HttpUser, task, constant


class UserTasks(SequentialTaskSet):
    @task
    def goToHome(self):
        self.client.get('/task1')

    @task
    def goToProfile(self):
        self.client.get('/task2')

    @task
    def updateInfo(self):
        self.client.post("/task3", json={"username":"foo", "password":"bar"})


class FooUser(HttpUser):
    wait_time = constant(4)
    host = 'http://localhost:33380/api/v32'

    tasks = [UserTasks]