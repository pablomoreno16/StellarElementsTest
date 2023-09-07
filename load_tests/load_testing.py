from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 5)
    host = "https://automationexercise.com/api"

    @task
    def get_products(self):
        self.client.get("/productsList")
