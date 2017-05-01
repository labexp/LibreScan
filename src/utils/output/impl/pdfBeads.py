import subprocess
from utils.output.outputMaker import OutputMaker


class PDFBeads(OutputMaker):

    def make(self, p_path, p_output_name):
        input_path = p_path + "/processed/"
        output_path = p_path + "/" + p_output_name
        command = 'cd {0}; pdfbeads *.tif > {1}.pdf'.format(input_path, output_path)
        subprocess.call(command, shell=True)
