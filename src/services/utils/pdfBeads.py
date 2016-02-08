__author__ = 'melalonso'

from outputMaker import OutputMaker
from subprocess import call


class PDFBeads(OutputMaker):

    def make(self, path, filename):
        call("pdfbeads "+path+".tif > "+filename+".pdf", shell=True)
