__author__ = 'melalonso'

from task import Task
from subprocess import call

class Tesseract(Task):

    def exec(self,p_language,p_format, p_input_dir):
           call( "parallel tesseract -l "+ p_language + " {} {.} " + p_format+  " ::: " + p_input_dir,shell=True)


