import os
from models.cameraConfig import CameraConfig
from models.project import Project
from services.cameraService import CameraService
from services.queueService import QueueService
from services.projectService import ProjectService
from services.outputService import OutputService
from utils.taskManager import TaskManager
from bottle import request


class ProjectController:

    def __init__(self, p_env, p_project_service):
        self.env = p_env
        self.project_service = p_project_service

    def get_config(self):
        pass

    def new(self):
        available_langs = ProjectService().get_available_languages()
        return self.env.get_template('newProject.jade').render(langs=available_langs)

    def create(self):
        params = request.json['post_data']
        name = params['project_name']
        description = params['project_description']
        language = params['config']['language']
        camera_config = CameraConfig(params['config']['zoom'], 0)
        project = Project(None, name, description, language, camera_config, ['pdfbeads'])
        project_path = self.project_service.create(project)
        status = self.set_services_working_dir(project_path)
        return {'status': status}

    def load(self, id):
        project_id = id
        project_path = os.environ["HOME"] + '/LibreScanProjects/' + project_id
        self.project_service.load(project_id)
        last_pic_number = self.project_service.get_project_last_pic(project_id)
        status = self.set_services_working_dir(project_path, last_pic_number)
        return {'status': status}

    def remove(self):
        project_id = request.json['id']
        status = self.project_service.remove(project_id)
        return {'status': status}

    def show(self):
        projects_map = self.project_service.get_all()
        if projects_map is None:
            project_list = []
        else:
            project_list = sorted(list(projects_map.items()), key=lambda x: x[1]["creation_date"], reverse=True)
        return self.env.get_template('showProjects.jade').render(projects=project_list)

    def set_services_working_dir(self, p_working_dir, p_pic_number=0):
        camera_service = CameraService(p_pic_number=p_pic_number)
        camera_service.working_dir = p_working_dir
        queue_service = QueueService()
        queue_service.task_manager = TaskManager(p_working_dir)
        output_service = OutputService(p_working_dir, "out")
        return 1