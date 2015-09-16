import os
from pathlib import Path
import subprocess
from services.utils.outputMaker import OutputMaker


class PDFBeads(OutputMaker):

    def get_output_path(self, p_path):
        path_object = Path(p_path)
        return str(path_object.parents[0])

    def make(self, p_path, p_output_name):
        output = self.get_output_path(p_path) + "/" + p_output_name
        command = "pdfbeads " + "*.tif > " + output +".pdf"
        os.chdir(p_path)
        subprocess.call(command, shell=True)
