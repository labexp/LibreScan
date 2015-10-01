from services.utils.taskManager import TaskManager


class WorkFlowService:
    def __init__(self):
        self.task_manager = TaskManager("/home/diugalde/Desktop")

    def push_photos(self, p_list_ids):
        pass

    def finish_product(self):
        self.task_manager.generate()

ws = WorkFlowService()
ws.finish_product()

