from models.projectPhoto import ProjectPhoto
from os import getenv
from patterns.singleton import Singleton
from queue import Queue
import threading


class QueueService(metaclass=Singleton):

    def __init__(self, p_worker_threads=2):
        self.queue = Queue()
        self.worker_threads = p_worker_threads
        self.reset_queue()
        for i in range(self.worker_threads):
            t = threading.Thread(target=self.start)
            t.setDaemon(True)
            t.start()

    def start(self):
        while True:
            photos = [self.queue.get(block=True)]
            print("Processing image: " + photos[0].pic_name)
            self.task_manager.process(photos)
            self.queue.task_done()

    def push(self, p_image_list):
        if isinstance(p_image_list, list):
            for image in p_image_list:
                self._queue_pic(image)
        else:
            self._queue_pic(p_image_list)

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

    def _queue_pic(self, p_picture):
        working_dir = getenv("LS_PROJECT_PATH")
        photo = ProjectPhoto(working_dir, p_picture)
        self.queue.put(photo)

    @staticmethod
    def get_active_threads():
        return threading.active_count()
