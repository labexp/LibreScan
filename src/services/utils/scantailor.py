import yaml
from task import Task
from subprocess import call


class Scantailor(Task):

    def __init__(self, p_input_dir, p_output_dir):
        self.params = self.get_configuration()
        self.input_dir = p_input_dir
        self.output_dir = p_output_dir

    #Loads scantailor configuration from src/configuration/config.yaml in python dictionary.
    def get_configuration(self):
        f = open('../../configuration/config.yaml')
        data_map = yaml.safe_load(f)
        f.close()
        return data_map['scantailor']

    #Iterates through python dictionary to create the command string.
    def command_maker(self):
        command = "scantailor-cli"
        for param in self.params:
            command += " -" + param + "=" + str(self.params[param])
        command += " " + self.input_dir + " " + self.output_dir
        return command

    def exec(self):
        command = self.command_maker()
        call(command)


