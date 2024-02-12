from locust import HttpUser, task, constant, SequentialTaskSet, events
import logging


################ Events ################
@events.spawning_complete.add_listener
def spawn_done(user_count, **kwargs):
    print('==on spawn done== ', user_count)

@events.request.add_listener
def send_notification(exception, **kwargs):
    if exception:
        print("== Sending failure notifcation", exception)
    else:
        print('== Sending success notification')


@events.quitting.add_listener
def sla(environment, **kwargs):
    print('==dir env==', dir(environment))
    if environment.stats.total.fail_ratio > 0.01:
        logging.error('===Test failed due to fail ratio > 0.01')
        environment.process_exit_code = 1
        print("== env exit code", environment.process_exit_code)
    else:
        environment.process_exit_code = 0
        print("== env exit code", environment.process_exit_code)



############# Test scenario #############
class LoadTestSet(SequentialTaskSet):
    @task
    def homepage(self):
        self.client.get('/', name="T01_homepage")
        self.client.get('/users/me', name="T02_FailRequests", headers= {"Authorization": f"Bearer 50000|50000_static_access_token"})


class TestScenario(HttpUser):
    wait_time = constant(2)
    tasks = [LoadTestSet]
