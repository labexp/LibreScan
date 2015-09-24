import os
import yaml
class ProjectService:

    def create(self, p_project):
        path = os.environ["HOME"] #This needs to be changed to environ["LibreScan"]
        path += ".LibreScan/config.yaml"
        f = open(path)
        data_map = yaml.safe_load(f)
        f.close()
        data_map['project']
        return 1

    def remove(self, p_id):
        return 1

    def load(self, p_id):
        return 1

    def get_all(self):
        return []

    def get_config(self, p_id):
        return 1

    def change_config(self, config):
        return 1

    def create_threads(self):
        return 1
