from patterns.singleton import Singleton
from queue import Queue
import threading
from utils.task.taskManager import TaskManager


class QueueService(metaclass=Singleton):

    def __init__(self, p_worker_threads=2):
        self.queue = Queue()
        self.worker_threads = p_worker_threads
        self.task_manager = TaskManager()
        self.reset_queue()
        for i in range(self.worker_threads):
            t = threading.Thread(target=self.start)
            t.setDaemon(True)
            t.start()

    def start(self):
        while True:
            item = [self.queue.get(block=True)]
            print("Processing image: " + item[0])
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

    def reset_queue(self):
        self.clean_queue()
        self.wait_process()

    @staticmethod
    def get_active_threads():
        return threading.active_count()
