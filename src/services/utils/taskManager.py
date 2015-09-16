from services.utils.pdfBeads import PDFBeads
from services.utils.scantailor import Scantailor
from services.utils.tesseract import Tesseract


class TaskManager:

    def __init__(self, p_working_dir):
        self.working_dir = p_working_dir
        self.tasks = [Scantailor(), Tesseract()]  # Task
        self.output_makers = [PDFBeads()]  # OutputMaker

    def process(self, p_list):
        for photo in p_list:
            params = {'input_dir': self.working_dir, 'photo': photo}
            for task in self.tasks:
                task.exec(params)

    def rename(self):
        pass

    def generate(self):
        for output_maker in self.output_makers:
            output_maker.make(self.working_dir, "out")

'''
Example:
    t = TaskManager("/home/diugalde/Desktop")
    t.process(['015', '016'])
    t.generate()
'''