import os
import subprocess
import yaml
from patterns.singleton import Singleton
import time


class ProjectService(metaclass=Singleton):
    def __init__(self):
        self.config_folder = os.environ["HOME"] + "/.librescan"
        self.project_path = None

    def create(self, p_project):
        path = self.config_folder + "/config.yaml"
        folder_name = self.get_folder_name(path)
        new_project_path = self.get_projects_path(path) + "/" + folder_name
        self.project_path = new_project_path
        os.mkdir(new_project_path)
        os.mkdir(new_project_path + "/raw")
        os.mkdir(new_project_path + "/processed")

        # Creates the project config template with default values.
        src = self.config_folder + "/defaultProjectConfig.yaml"
        destiny = new_project_path + "/.projectConfig.yaml"
        os.system("cp " + src + " " + destiny)
        os.system("touch " + new_project_path + "/.pics.ls")
        os.system("touch " + new_project_path + "/.toDelete.ls")

        # Update project configuration
        self.change_config(p_project, destiny)

        # Append new project to projects file.
        self.append_project(self.config_folder + "/projects.yaml", folder_name, p_project.name, p_project.description)
        return new_project_path

    def remove(self, p_id):
        config_path = self.config_folder + "/projects.yaml"
        f = open(config_path)
        data_map = yaml.safe_load(f)
        f.close()
        data_map.pop(p_id)
        project_path = os.environ["HOME"] + '/LibreScanProjects/' + p_id
        os.system("rm -rf " + project_path)

        f = open(config_path, 'w')
        if data_map:
            f.write(yaml.dump(data_map, default_flow_style=False, allow_unicode=True))
        else:
            f.seek(0)
            f.truncate()
        f.close()
        return 1

    def load(self, p_id):
        self.project_path = os.environ["HOME"] + '/LibreScanProjects/' + p_id

    def get_all(self):
        config_path = self.config_folder + "/projects.yaml"
        f = open(config_path)
        data_map = yaml.safe_load(f)
        f.close()
        return data_map

    def get_config(self, p_id):
        return 1

    def change_config(self, p_project, p_config_path):
        f = open(p_config_path)
        data_map = yaml.safe_load(f)
        f.close()
        if p_project.cam_config is not None:
            data_map['camera']['zoom'] = p_project.cam_config.zoom
            data_map['camera']['iso'] = p_project.cam_config.iso

        data_map['general-info']['name'] = p_project.name
        data_map['general-info']['description'] = p_project.description
        data_map['general-info']['output-formats'] = p_project.output_formats
        data_map['tesseract']['lang'] = p_project.lang

        f = open(p_config_path, 'w')
        f.write(yaml.dump(data_map, default_flow_style=False, allow_unicode=True))
        f.close()

    def get_folder_name(self, p_path):
        f = open(p_path)
        data_map = yaml.safe_load(f)
        f.close()
        project_id = data_map['project']['last-id'] + 1
        data_map['project']['last-id'] = project_id
        folder_name = "L" + str(project_id)
        f = open(p_path, 'w')
        f.write(yaml.dump(data_map, default_flow_style=False, allow_unicode=True))
        f.close()
        return folder_name

    def get_projects_path(self, p_path):
        f = open(p_path)
        projects_path = yaml.safe_load(f)['project']['path']
        f.close()
        return projects_path

    def append_project(self, p_projects_path, p_id, p_name, p_description):
        creation_date = time.strftime("%x %X")
        project = {str(p_id): {'name': p_name, 'description': p_description, 'creation_date': creation_date}}
        f = open(p_projects_path, "a")
        f.write(yaml.dump(project, default_flow_style=False, allow_unicode=True))
        f.close()

    def get_available_languages(self):
        available_langs = (subprocess.Popen(['tesseract', "--list-langs"],
                                            stderr=subprocess.STDOUT,
                                            stdout=subprocess.PIPE)
                           .communicate()[0].decode('utf-8')
                           .split("\n")[1:-1])
        return available_langs

    def get_project_last_pic(self, p_id):
        config_path = os.environ["HOME"] + '/LibreScanProjects/' + p_id + '/.projectConfig.yaml'
        f = open(config_path)
        last_pic_number = yaml.safe_load(f)['camera']['last-pic-number']
        f.close()
        return last_pic_number

    def remove_file_pics(self, p_index=-1):
        pics_file = self.working_dir + '/.pics.ls'
        f = open(pics_file, "r")
        contents = f.readlines()
        f.close()

        if p_index == -1:
            p_index = len(contents) - 2

        contents.pop(p_index)
        contents.pop(p_index+1)

        f = open(pics_file, "w")
        f.writelines(contents)
        f.close()
