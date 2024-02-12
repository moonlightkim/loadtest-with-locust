from locust import events
from locust.runners import MasterRunner

@events.init.add_listener
def on_locust_init(environment, **kwargs):
    if isinstance(environment.runner, MasterRunner):
        print("===I'm on master node")
    else:
        print("====I'm on a worker or standalone node")