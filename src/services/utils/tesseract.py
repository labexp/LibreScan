import subprocess
from services.utils.task import Task


class Tesseract(Task):

    def __init__(self, p_language='spa', p_format='hocr', p_photo_extension='tif'):
        self.language = p_language
        self.output_format = p_format
        self.photo_extension = p_photo_extension

    def exec(self, params):
        input_path = params['input_dir'] + '/' + params['photo'] + "." + self.photo_extension
        output_path = params['input_dir'] + '/' + params['photo']
        command = "tesseract -l " + self.language + " " + input_path + " " + output_path + " " + self.output_format
        subprocess.call(command, shell=True)