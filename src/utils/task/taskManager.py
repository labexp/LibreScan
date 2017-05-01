from os import getenv
from utils.task.impl.scantailor import Scantailor
from utils.task.impl.tesseract import Tesseract
from yaml import safe_load


class TaskManager:

    def __init__(self):
        self.working_dir = getenv("LS_PROJECT_PATH")
        if self.working_dir:
            configuration = self.get_configuration()
            scantailor = Scantailor(configuration['scantailor'])
            tesseract = Tesseract(configuration['tesseract'])
            self.tasks = [scantailor, tesseract]

    def process(self, p_list):
        # TODO: Trace code and find why the ProjectService.load is not changing the working_dir
        self.working_dir = getenv("LS_PROJECT_PATH")    # Remove this when figured out
        for photo in p_list:
            params = {'input_dir': self.working_dir, 'photo': photo}
            for task in self.tasks:
                task.exec(params)

    # Loads tools configuration from the project configuration.
    def get_configuration(self):
        self.working_dir = getenv("LS_PROJECT_PATH")    # Remove this when figured out
        config_path = self.working_dir + "/.projectConfig.yaml"
        f = open(config_path)
        data_map = safe_load(f)
        f.close()
        return data_map
