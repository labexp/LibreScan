from utils.pdfBeads import PDFBeads
from utils.outputPreparer import OutputPreparer
from patterns.singleton import Singleton


class OutputService(metaclass=Singleton):

    def __init__(self, p_working_dir):
        self.working_dir = p_working_dir
        self.output_preparer = OutputPreparer(p_working_dir)
        self.output_makers = [PDFBeads()]  # OutputMaker

    def generate(self):
        self.output_preparer.run()
        for output_maker in self.output_makers:
            output_maker.make(self.working_dir, "out")
