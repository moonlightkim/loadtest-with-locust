from locust import HttpUser, task


# Each class that inherits HttpUser represents a user.
# A user can do tasks many times..

class AdminUser(HttpUser):
    fixed_count = 1 # exactly 1 user spawned to request all these tasks.

    @task
    def seeAllUsers(self):
        self.client.get('/admin/users')