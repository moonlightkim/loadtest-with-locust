from locust import HttpUser, task, constant
from locust.event import EventHook


send_email_notif = EventHook()
send_txt_notif = EventHook()


def email(i, j, req_id, message=None, **kwargs):
    print("Sending", message, " in Email for request ", req_id)

def sms_txt(i, j, req_id, message=None, **kwargs):
    print("Sending", message, "in SMS for request ", req_id)

# ??
send_email_notif.add_listener(email)
send_txt_notif.add_listener(sms_txt)


class TestScenario(HttpUser):
    wait_time = constant(2)

    @task
    def homepage(self):
        with self.client.get('/', name="01_Homepage", catch_response=True) as response:
            if response.status_code == 200:
                send_email_notif.fire(i=1, j=2, req_id=1, message="success")
                send_email_notif.fire(i=1, j=2, req_id=1, message="success")

            else:
                send_email_notif.fire(i=1, j=2, req_id=1, message="failed")
                send_email_notif.fire(i=1, j=2, req_id=1, message="failed")

        with self.client.get("/users/me",
                             name="02_UserMe",
                             catch_response=True,
                             headers={"Authorization": f"Bearer 50000|50000_static_access_token"}) as response:
            if response.status_code == 200:
                    send_email_notif.fire(i=1, j=2, req_id=1, message="success")
                    send_email_notif.fire(i=1, j=2, req_id=1, message="success")

            else:
                send_email_notif.fire(i=1, j=2, req_id=1, message="failed")
                send_email_notif.fire(i=1, j=2, req_id=1, message="failed")