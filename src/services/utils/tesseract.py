from task import Task
from subprocess import call

class Tesseract(Task):

    def __init__(self,p_language,p_format, p_input_dir):
        self.language = p_language
        self.format = p_format
        self.input_dir = p_input_dir


    def exec(self):
           call( "parallel tesseract -l "+ self.language + " {} {.} " + self.format+  " ::: " + self.input_dir,shell=True)
            

