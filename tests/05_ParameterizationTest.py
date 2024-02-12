from locust import HttpUser, task, events, constant
from utils.ReadFile import readjson
import random

# How we can dynamically manipulate sets of input data

# Example server is mcportal. Use json data from token.json to get tokens to access protected route.
class GetMeUser(HttpUser):
    host = 'http://localhost:33380/api/v32'

    # Read token data on start
    def on_start(self):
        print('== on start ==')
        self.tokendata = readjson('/Users/moonlight/Desktop/loadtest-with-locust/tests/data/token.json').tokens

    @task
    def getme(self):
        tokendata = list(self.tokendata)
        idx = random.randint(0, 50000)

        print('===Auth Token=== ', tokendata[idx])
        self.client.get('/users/me', headers= {"Authorization": f"Bearer {tokendata[idx]}"})
 
    def on_stop(self):
        print('== on STOP ==')