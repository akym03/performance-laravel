from locust import HttpUser, task

class SimplePage(HttpUser):
    @task
    def access_to_smple_page(self):
        self.client.get("/simple.html")
