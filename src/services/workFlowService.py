from pdfBeads import PDFBeads


class WorkFlowService:

    def __init__(self):
        self.output_maker_list = [PDFBeads()]

    def push_photos(self, p_list_ids):
        pass

    def finish_product(self):
        for output_maker in self.output_maker_list:
            output_maker.make("path/to/tiff_files", "output")
