from gettext import translation
from bottle import *
from jinja2 import Environment, FileSystemLoader

from services.hocrService import HocrService
from services.imageService import ImageService
from services.mailService import MailService
from services.projectService import ProjectService
from services.queueService import QueueService
from services.outputService import OutputService
from services.ocrEditorService import OcrEditorService
from services.devScannerService import DevScannerService
from services.scannerService import ScannerService
from web.controllers.imageController import ImageController
from web.controllers.jabiruController import JabiruController
from web.controllers.languageController import LanguageController
from web.controllers.mailController import MailController
from web.controllers.navigationController import NavigationController
from web.controllers.scannerController import ScannerController
from web.controllers.projectController import ProjectController
from web.controllers.taskController import TaskController
from web.controllers.textController import TextController
from web.controllers.ocrEditorController import OcrEditorController


class LibreScanWeb:
    def __init__(self):
        self.dev_mode = os.environ["LS_DEV_MODE"] == "True"
        self.host = '127.0.0.1'
        self.port = '3333'
        self.app = Bottle()
        self.default_language = 'spa'
        self.env = self.init_environment()
        self.controllers = self.init_controllers()
        self.init_routes()

    def init_environment(self):
        env = Environment(loader=FileSystemLoader(searchpath='web/views/'),
                          extensions=['pyjade.ext.jinja.PyJadeExtension',
                                      'jinja2.ext.i18n'])
        translations = translation(domain='messages',
                                   localedir='./web/i18n/locale',
                                   languages=[self.default_language])
        env.install_gettext_translations(translations)
        return env

    def init_routes(self):
        self._init_scanner_routes()
        self._init_mail_routes()
        self._init_navigation_routes()
        self._init_project_routes()
        self._init_task_routes()
        self._init_ocr_editor_routes()
        # self._init_jabiru_routes()
        self.app.route('/assets/:p_file#.+#', name='static',
                       callback=self.return_resource)
        self.app.route('/language/<lang>', method="GET",
                       callback=self.controllers['language'].change_language)
        # The other routes would go here.

    def _init_project_routes(self):
        self.app.route('/project/<id>/config', method="GET",
                       callback=self.controllers['project'].get_config)
        self.app.route('/project', method="POST",
                       callback=self.controllers['project'].create)
        self.app.route('/project/<id>', method="GET",
                       callback=self.controllers['project'].load)
        self.app.route('/project/new', method="GET",
                       callback=self.controllers['project'].new)
        self.app.route('/projects/show', method="GET",
                       callback=self.controllers['project'].show)
        self.app.route('/project', method="DELETE",
                       callback=self.controllers['project'].remove)

    def _init_scanner_routes(self):
        # Route to handle shoot.
        self.app.route('/photo', method="POST",
                       callback=self.controllers['scanner'].create_photos)
        # Route to handle recapture.
        self.app.route('/photo', method="PUT",
                       callback=self.controllers['scanner'].update_photos)
        # Route to handle delete.
        self.app.route('/photo', method="DELETE",
                       callback=self.controllers['scanner'].delete_photos)
        # Route to handle get photo.
        self.app.route('/photo/<id>', method="GET",
                       callback=self.controllers['scanner'].get_photo)
        # Route to handle get thumbnail.
        self.app.route('/thumbnail/<id>', method="GET",
                       callback=self.controllers['scanner'].get_thumbnail)
        # Route to handle cam preparation.
        self.app.route('/camera/prepare', method="POST",
                       callback=self.controllers['scanner'].prepare_devices)
        # Route to handle cam preparation.
        self.app.route('/camera/calibrate', method="POST",
                       callback=self.controllers['scanner'].recalibrate_cams)
        self.app.route('/scan', method="GET",
                       callback=self.controllers['scanner'].scan)
        self.app.route('/scan/halt', method="POST",
                       callback=self.controllers['scanner'].stop_scanning)
        self.app.route('/progress', method="GET",
                       callback=self.controllers['scanner']
                       .get_process_progress)

    def _init_mail_routes(self):
        self.app.route('/mail', method="GET",
                       callback=self.controllers['mail'].create)

    def _init_navigation_routes(self):
        self.app.route('/', method="GET",
                       callback=self.controllers['navigation'].home)
        self.app.route('/about', method="GET",
                       callback=self.controllers['navigation'].about)
        self.app.route('/contact', method="GET",
                       callback=self.controllers['navigation'].contact)
        self.app.route('/outputPreview', method="GET",
                       callback=self.controllers['navigation'].output_preview)

    def _init_task_routes(self):
        self.app.route('/output', method="POST",
                       callback=self.controllers['task'].generate_output)
        self.app.route('/pdf', method="GET",
                       callback=self.controllers['task'].get_pdf)

    def _init_ocr_editor_routes(self):
        self.app.route('/ocrs', method="GET",
                       callback=self.controllers['ocr_editor'].show)

    def _init_jabiru_routes(self):
        self.app.route('/pages', method="GET",
                       callback=self.controllers['jabiru'].home)
        self.app.route('/images/<id>', method="GET",
                       callback=self.controllers['image'].get_image)
        self.app.route('/images/last/id', method="GET",
                       callback=self.controllers['image'].get_last_id)
        self.app.route('/texts/<id>', method="GET",
                       callback=self.controllers['text'].get_text)
        self.app.route('/saves/<id>', method="POST",
                       callback=self.controllers['text'].save_text)

    def init_controllers(self):
        if self.dev_mode:
            scanner_service = DevScannerService()
        else:
            scanner_service = ScannerService()
        mail_service = MailService()
        project_service = ProjectService()
        queue_service = QueueService()
        output_service = OutputService()
        ocr_editor_service = OcrEditorService()
        image_service = ImageService()
        hocr_service = HocrService()
        controllers = {
            'navigation': NavigationController(self.env),
            'scanner': ScannerController(self.env, scanner_service,
                                         queue_service),
            'project': ProjectController(self.env, project_service),
            'mail': MailController(self.env, mail_service),
            'language': LanguageController(self.env),
            'task': TaskController(self.env, output_service),
            'ocr_editor': OcrEditorController(self.env, ocr_editor_service),
            'jabiru': JabiruController(self.env),
            'image': ImageController(image_service),
            'text': TextController(hocr_service)
        }
        return controllers

    def return_resource(self, p_file):
        return static_file(p_file, root='web/assets')

    def run_app(self):
        self.app.run(host=self.host, port=self.port, quiet=False, debug=True)
