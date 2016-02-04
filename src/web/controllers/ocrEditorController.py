class OcrEditorController:

    def __init__(self, p_env, p_ocr_editor_service):
        self.env = p_env
        self.ocr_editor_service = p_ocr_editor_service

    def show(self):
        return self.env.get_template('checkOcr.jade').render(total_pages=56)
