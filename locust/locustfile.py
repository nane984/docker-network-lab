from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # vreme između zahteva u sekundama

    @task
    def home(self):
        self.client.get("/test")

    @task
    def admin_login(self):
        # samo test POST ako želiš, ili healthcheck
        self.client.get("/admin/login/")
