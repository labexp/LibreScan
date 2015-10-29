from services.cameraService import CameraService
from services.queueService import QueueService
from utils.taskManager import TaskManager


class ProjectController:

    def __init__(self, p_env, p_project_service):
        self.env = p_env
        self.project_service = p_project_service

    def home(self):
        return self.env.get_template('home.jade').render()

    def get_config(self):
        pass

    def new(self):
        return self.env.get_template('newProject.jade').render()

    def create(self):
        pass

    def load(self):
        pass

    def set_new_project_config(self, p_working_dir):
        camera_service = CameraService()
        camera_service.set_save_path(p_working_dir)
        camera_service.set_camera_config()

        queue_service = QueueService()
        queue_service.task_manager = TaskManager(p_working_dir)