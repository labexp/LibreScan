import yaml
import subprocess
from services.utils.task import Task


class Scantailor(Task):
    def __init__(self, p_photo_extension="jpg"):
        self.params = self.get_configuration()
        self.photo_extension = p_photo_extension

    # Loads scantailor configuration from src/configuration/config.yaml in python dictionary.
    def get_configuration(self):
        f = open('configuration/config.yaml')
        data_map = yaml.safe_load(f)
        f.close()
        return data_map['scantailor']

    # Iterates through python dictionary to create the command string.
    def command_maker(self, p_input_dir, p_photo):
        command = "scantailor-cli"
        for param in self.params:
            command += " -" + param + "=" + str(self.params[param])
        input_path = p_input_dir + "/" + p_photo + "." + self.photo_extension
        output_path = p_input_dir
        command += " " + input_path + " " + output_path + "/"
        return command

    def exec(self, params):
        command = self.command_maker(params['input_dir'], params['photo'])
        subprocess.call(command, shell=True)
