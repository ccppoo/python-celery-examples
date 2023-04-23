import requests
import threading
import time


class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        start = time.time()
        r = requests.get("http://127.0.0.1:8000")
        cost = time.time() - start

        task_id = r.json()

        while True:
            r2 = requests.get(f"http://127.0.0.1:8000/task?id={task_id}")
            if r2.json()["result"]:
                break
            else:
                time.sleep(0.005)
        print(r2.json())


if __name__ == "__main__":
    start = time.time()
    ww = [Worker(x) for x in range(12)]

    [x.start() for x in ww]
    [x.join() for x in ww]
    print(f"cost : {time.time() - start:.3f}")
