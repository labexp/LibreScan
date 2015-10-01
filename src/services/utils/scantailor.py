import subprocess
from services.utils.task import Task


class Scantailor(Task):
    def __init__(self, p_config_params, p_photo_extension="jpg"):
        self.config_params = p_config_params
        self.photo_extension = p_photo_extension

    # Iterates through python dictionary to create the command string.
    def command_maker(self, p_input_dir, p_photo):
        command = "scantailor-cli"

        for param in self.config_params:
            command += " -" + param + "=" + str(self.config_params[param])
        input_path = p_input_dir + "/" + p_photo + "." + self.photo_extension
        output_path = p_input_dir
        command += " " + input_path + " " + output_path + "/"
        return command

    def exec(self, params):
        command = self.command_maker(params['input_dir'], params['photo'])
        subprocess.call(command, shell=True)
