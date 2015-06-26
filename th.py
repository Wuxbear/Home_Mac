import threading
from time import sleep

def worker(num):
    """thread worker function"""
    for i in range(10):
        print('Worker: %s' % num)
        sleep(1)


threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

print("done!")
