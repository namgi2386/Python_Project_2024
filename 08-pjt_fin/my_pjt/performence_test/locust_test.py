from locust import HttpUser, task, between

class SampleUser(HttpUser):
    wait_time = between(1, 3)


    def on_start(self): # <<<<<<<<< 유저 생성시 자동호출
        print('test start')

    @task
    def normal_sort(self):
        self.client.get("test/normal_sort/")

    @task
    def priority_queue(self):
        self.client.get("test/priority_queue/")

    @task
    def bubble_sort(self):
        self.client.get("test/bubble_sort/")


