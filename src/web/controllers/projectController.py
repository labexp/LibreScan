from bottle import request
from models.cameraConfig import CameraConfig
from models.project import Project
from os import environ as env
from services.devScannerService import DevScannerService
from services.scannerService import ScannerService
from services.projectService import ProjectService


class ProjectController:

    def __init__(self, p_env, p_project_service):
        self.env = p_env
        self.project_service = p_project_service

    def get_config(self):
        pass

    def new(self):
        available_langs = ProjectService().get_available_languages()
        black_list = ['equ', 'osd']
        available_langs = {x for x in available_langs if x not in black_list}
        template = self.env.get_template('newProject.jade')
        return template.render(langs=available_langs)

    def create(self):
        params = request.json['post_data']
        name = params['project_name']
        description = params['project_description']
        language = params['config']['language']
        zoom = int(params['config']['zoom'])
        camera_config = CameraConfig(zoom, 0)
        project = Project(None, name, description, language, camera_config,
                          ['pdfbeads'])
        project_path = self.project_service.create(project)
        env["LS_PROJECT_PATH"] = project_path
        self.services_last_pic()
        return {'status': 1}

    def load(self, id):
        project_id = id
        project_path = env["HOME"] + '/LibreScanProjects/' + project_id
        last_pic_number = self.project_service.get_project_last_pic(project_id)
        env["LS_PROJECT_PATH"] = project_path
        self.services_last_pic(last_pic_number)
        self.project_service.load(project_path)
        return {'status': 1}

    def remove(self):
        project_id = request.json['id']
        status = self.project_service.remove(project_id)
        return {'status': status}

    def show(self):
        projects_map = self.project_service.get_all()
        if projects_map is None:
            project_list = []
        else:
            project_list = sorted(list(projects_map.items()),
                                  key=lambda x: x[1]["creation_date"],
                                  reverse=True)
        template = self.env.get_template('showProjects.jade')
        return template.render(projects=project_list)

    @staticmethod
    def services_last_pic(p_pic_number=0):
        if env["LS_DEV_MODE"] == "True":
            DevScannerService(p_pic_number=p_pic_number)
        else:
            ScannerService(p_pic_number=p_pic_number)

