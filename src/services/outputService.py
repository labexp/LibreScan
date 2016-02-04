from utils.pdfBeads import PDFBeads
from utils.outputPreparer import OutputPreparer
from patterns.singleton import Singleton
import threading


class OutputService(metaclass=Singleton):

    def __init__(self, p_working_dir=None, p_output_name=None):
        self.working_dir = p_working_dir
        self.output_name = p_output_name
        self.output_preparer = OutputPreparer(p_working_dir)
        self.output_makers = [PDFBeads()]  # OutputMaker
        self.generators = []

    def generate(self):
        self.output_preparer.run()
        for output_maker in self.output_makers:
            t = threading.Thread(target=output_maker.make, args=(self.working_dir, self.output_name))
            t.setDaemon(True)
            self.generators.append(t)
            t.start()

    def wait_process(self):
        print("Esperando que se generen los output...")
        for g in self.generators:
            g.join()
