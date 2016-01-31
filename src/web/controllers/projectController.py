from models.cameraConfig import CameraConfig
from models.project import Project
from services.cameraService import CameraService
from services.queueService import QueueService
from services.projectService import ProjectService
from utils.taskManager import TaskManager
from bottle import request
import time


class ProjectController:

    def __init__(self, p_env, p_project_service):
        self.env = p_env
        self.project_service = p_project_service

    def home(self):
        return self.env.get_template('home.jade').render()

    def get_config(self):
        pass

    def new(self):
        avaible_langs = ProjectService().get_available_languages()
        return self.env.get_template('newProject.jade').render(langs=avaible_langs)

    def create(self):
        params = request.json['postData']
        name = params['project_name']
        description = params['project_description']
        language = params['config']['language']
        camera_config = CameraConfig(params['config']['zoom'], 0)
        project = Project(None, name, description, language, camera_config, ['pdfbeads'])
        project_path = self.project_service.create(project)
        self.set_new_project_config(project_path)
        return {'status': 1}

    def show(self):
        projects_map = self.project_service.get_all()
        if projects_map is None:
            project_list = []
        else:
            project_list = sorted(list(projects_map.items()), key=lambda x: x[1]["creation_date"])
        return self.env.get_template('showProjects.jade').render(projects=project_list)

    def set_new_project_config(self, p_working_dir):
        camera_service = CameraService()
        camera_service.working_dir = p_working_dir
        camera_service.set_camera_config()
        camera_service.prepare_cams()

        queue_service = QueueService()
        queue_service.task_manager = TaskManager(p_working_dir)
