from os import getenv
from patterns.singleton import Singleton
from threading import Thread
from utils.output.impl.pdfBeads import PDFBeads
from utils.output.outputPreparer import OutputPreparer


class OutputService(metaclass=Singleton):

    def __init__(self, p_output_name="Out"):
        self.working_dir = None
        self.output_name = p_output_name
        self.output_preparer = OutputPreparer()
        self.output_makers = [PDFBeads()]  # OutputMaker
        self.generators = []

    def generate(self):
        self.working_dir = getenv("LS_PROJECT_PATH")
        self.output_preparer.run()
        for output_maker in self.output_makers:
            t = Thread(target=output_maker.make, args=(self.working_dir, self.output_name))
            t.setDaemon(True)
            self.generators.append(t)
            t.start()

    def wait_process(self):
        for g in self.generators:
            g.join()
