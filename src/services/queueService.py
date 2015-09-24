__author__ = 'sd'

from queue import Queue
import threading


q = Queue()

def worker():
    while True:
        item = q.get()
        do_work(item)
        q.task_done()


for i in range(num_worker_threads):
     t = threading.Thread(target=worker)
     t.daemon = True
     t.start()

for item in source():
    q.put(item)

