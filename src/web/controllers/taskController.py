from services.queueService import QueueService
from services.outputService import OutputService
from bottle import request


class TaskController:

    def __init__(self, p_env):
        self.env = p_env
        self.output_service = OutputService()
        self.queue_service = QueueService()

    def generate_output(self):
        self.queue_service.wait_process()
        self.output_service.generate()

        return ""




