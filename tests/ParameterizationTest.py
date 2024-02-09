from locust import HttpUser, task, events, constant
from utils.ReadFile import readjson
import random

# How we can dynamically manipulate sets of input data

# Example server is mcportal. Use json data
class GetMeUser(HttpUser):
    host = 'http://localhost:33380/api/v32'

    def __init__(self, *args):
        super().__init__(*args)
        self.tokendata = readjson('/Users/moonlight/Desktop/loadtest-with-locust/tests/data/token.json').tokens

    @task
    def getme(self):
        tokendata = list(self.tokendata)
        idx = random.randint(0, 50000)

        print('===Auth Token=== ', tokendata[idx])
        self.client.get('/users/me', headers= {"Authorization": f"Bearer {tokendata[idx]}"})
