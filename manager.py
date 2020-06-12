
import time
from timeit import default_timer
class Timer():
    def __init__(self, timer = default_timer):
        self.timer = default_timer
    def __enter__(self):
        self.start = self.timer()
        print(self.start)
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = self.timer()
        print(self.end)
        print(f'elapsed:{self.end - self.start}')

def test(n=10):
    times = 0
    while True:
        time.sleep(1)
        times += 1
        if times > n:
            break


with Timer():
     test(4)
