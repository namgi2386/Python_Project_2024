from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)


    def on_start(self): # <<<<<<<<< 유저 생성시 자동호출
        print('test start')

    @task
    def namgi_sort(self):
        self.client.get("test/test_json/data/null_data/ave/")

    @task
    def jiwon_sort(self):
        self.client.get("test/jywon_avg/")

    @task
    def suyeon_sort(self):
        self.client.get("test/sooyeun_avg/")