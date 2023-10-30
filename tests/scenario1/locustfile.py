from locust import HttpUser, task, between, tag

class MyUser(HttpUser):
    wait_time = between(1, 3)  # Wait between 1 and 3 seconds between tasks

    @tag("tag5", "tag2")
    @task()
    def my_task(self):
        # Define the URL you want to request (in this case, google.com)
        url = "https://www.google.com"

        # Perform an HTTP GET request to google.com
        self.client.get("/")