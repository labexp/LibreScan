import subprocess
from subprocess import call
from services.utils.task import Task


class Tesseract(Task):

    def __init__(self, p_language='spa', p_format='hocr'):
        self.language = p_language
        self.output_format = p_format

    def exec(self, params):
        input_path = params['input_dir'] + '/' + params['photo']
        output_path = params['input_dir'] + '/' + params['photo'].split('.')[0]
        command = "tesseract -l " + self.language + " " + input_path + " " + output_path + " " + self.output_format
        subprocess.call(command, shell=True)