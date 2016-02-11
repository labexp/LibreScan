from queue import Queue
import threading
from patterns.singleton import Singleton


class QueueService(metaclass=Singleton):

    def __init__(self, p_worker_threads=2):
        self.queue = Queue()
        self.worker_threads = p_worker_threads
        for i in range(self.worker_threads):
            t = threading.Thread(target=self.start)
            t.setDaemon(True)
            t.start()

    def start(self):
        while True:
            item = [self.queue.get(block=True)]
            print("Processing image: "+item[0])
            self.task_manager.process(item)
            self.queue.task_done()

    def push(self, p_image_list):
        if isinstance(p_image_list, list):
            for image in p_image_list:
                self.queue.put(image)
        else:
            self.queue.put(p_image_list)

    def is_processing(self):
        return not(self.queue.empty())

    def wait_process(self):
        self.queue.join()

    def clean_queue(self):
        with self.queue.mutex:
            self.queue.queue.clear()
        print("The queue has been cleaned")
