from os import getenv
from os import mkdir
from os import system
from os.path import exists as f_checker
from patterns.singleton import Singleton
from services.queueService import QueueService
import subprocess
import time
import yaml


class ProjectService(metaclass=Singleton):
    def __init__(self):
        self.config_folder = getenv("HOME") + "/.librescan"
        self.project_path = None
        self.working_dir = None

    def create(self, p_project):
        path = self.config_folder + "/config.yaml"
        folder_name = self.get_folder_name(path)
        new_project_path = self.get_projects_path(path) + "/" + folder_name
        self.project_path = new_project_path
        mkdir(new_project_path)
        mkdir(new_project_path + "/raw")
        mkdir(new_project_path + "/processed")

        # Creates the project config template with default values.
        src = self.config_folder + "/defaultProjectConfig.yaml"
        destiny = new_project_path + "/.projectConfig.yaml"

        system("cp " + src + " " + destiny)
        system("touch " + new_project_path + "/.pics.ls")
        system("touch " + new_project_path + "/.toDelete.ls")

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
        project_path = getenv("HOME") + '/LibreScanProjects/' + p_id
        system("rm -rf " + project_path)

        f = open(config_path, 'w')
        if data_map:
            f.write(yaml.dump(data_map, default_flow_style=False, allow_unicode=True))
        else:
            f.seek(0)
            f.truncate()
        f.close()
        return 1

    def load(self, p_project_path):
        self.project_path = p_project_path
        pics_file = self.project_path + '/.pics.ls'
        f = open(pics_file, "r")
        contents = f.readlines()
        f.close()
        index = 1
        queue_service = QueueService()
        processed_path = self.project_path + "/processed/"
        for c in contents:
            pic_path = processed_path + c[:-1]
            if (not f_checker(pic_path + ".tif") or
                    not f_checker(pic_path + ".hocr")):
                if (not f_checker(processed_path + "rlsp" + str(index).zfill(5) + ".tif") or
                        not f_checker(processed_path + "rlsp" + str(index).zfill(5) + ".hocr")):
                    queue_service.push([c[:-1]])
                    print("Pushing " + c[:-1])
            index += 1

    def get_all(self):
        config_path = self.config_folder + "/projects.yaml"
        f = open(config_path)
        data_map = yaml.safe_load(f)
        f.close()
        return data_map

    @staticmethod
    def get_config(p_id):
        return 1

    @staticmethod
    def change_config(p_project, p_config_path):
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

    @staticmethod
    def get_folder_name(p_path):
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

    @staticmethod
    def get_projects_path(p_path):
        f = open(p_path)
        projects_path = yaml.safe_load(f)['project']['path']
        f.close()
        return projects_path

    @staticmethod
    def append_project(p_projects_path, p_id, p_name, p_description):
        creation_date = time.strftime("%x %X")
        project = {str(p_id): {'name': p_name, 'description': p_description, 'creation_date': creation_date}}
        f = open(p_projects_path, "a")
        f.write(yaml.dump(project, default_flow_style=False, allow_unicode=True))
        f.close()

    @staticmethod
    def get_available_languages():
        available_langs = (subprocess.Popen(['tesseract', "--list-langs"],
                                            stderr=subprocess.STDOUT,
                                            stdout=subprocess.PIPE)
                           .communicate()[0].decode('utf-8')
                           .split("\n")[1:-1])
        return available_langs

    @staticmethod
    def get_project_last_pic(p_id):
        config_path = getenv("HOME") + '/LibreScanProjects/' + p_id + '/.projectConfig.yaml'
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
