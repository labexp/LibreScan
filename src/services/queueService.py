__author__ = 'sd'

from queue import Queue
import threading
from services.utils.taskManager import TaskManager


class queueSerivice:

    def start(self):

        while True:
            item = [self.queue.get(block=True)]
            print("Procesando imagen: "+item[0])
            t = TaskManager("/home/sd/Documents/prueba/pruebaSpreads/SD")
            t.process(item)
            self.queue.task_done()

    def push(self, p_image):
        if isinstance(p_image, list):
            for image in p_image:
                #print(image)
                self.queue.put(image)
        else:
            self.queue.put(p_image)

    def __init__(self, p_worker_threads=2):
        self.queue = Queue()
        self.worker_threads = p_worker_threads
        for i in range(self.worker_threads):
            t = threading.Thread(target=self.start)
            t.setDaemon(True)
            t.start()

    def get_active_threads(self):
        return threading.active_count()