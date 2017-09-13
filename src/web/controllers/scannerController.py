import sys
from bottle import HTTPResponse
from utils.log import Log
from jpegtran import JPEGImage


class ScannerController:
    def __init__(self, p_env, p_camera_service, p_queue_service):
        self.env = p_env
        self.scanner_service = p_camera_service
        self.queue_service = p_queue_service
        self.pending_pics = []

    def scan(self):
        if self.scanner_service is None:
            return {'status': -1}
        last_pics = self.scanner_service.get_last_photo_names()
        return self.env.get_template('scan.jade').render(last_pics=last_pics)

    def create_photos(self):
        pic_names = self.scanner_service.take_pictures()
        if pic_names == -1:
            return {'status': -1}
        if len(self.pending_pics) != 0:
            self.queue_service.push(self.pending_pics)
        self.pending_pics = pic_names
        return {'status': 1, 'photo1': pic_names[0], 'photo2': pic_names[1]}

    def update_photos(self):
        pic_names = self.scanner_service.take_pictures()

        if pic_names == -1:
            return {'status': -1}
        self.scanner_service.delete_photos(self.pending_pics)
        self.pending_pics = pic_names
        return {'status': 1, 'photo1': pic_names[0], 'photo2': pic_names[1]}

    def prepare_devices(self):
        try:
            self.scanner_service.set_camera_config()
            self.scanner_service.prepare_cams()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            log = Log()
            log.log_error('Error in the method set_new_project_config')
            return {'status': -1}
        return {'status': 1}

    # Delete a pair of photos.
    def delete_photos(self):
        pass

    def get_process_progress(self):
        items_left = self.queue_service.queue.qsize()
        if items_left == 0:
            self.queue_service.wait_process()
        return {'itemsLeft': items_left}

    def stop_scanning(self):
        print(self.pending_pics)
        self.queue_service.push(self.pending_pics)
        return {'ready': True}

    def get_thumbnail(self, id):
        return self._get_img_response(id)

    def get_photo(self, id):
        return self._get_img_response(id, False)

    def _get_img_response(self, id, thumb=True):
        path = "{0}/raw/{1}.jpg".format(self.scanner_service.working_dir, id)
        headers = {
            'Content-Type': 'image/jpg'
        }
        image = JPEGImage(path)
        if thumb:
            image = image.downscale(500, 375)
        body = image.as_blob()
        return HTTPResponse(body, **headers)

    def recalibrate_cams(self):
        status = self.scanner_service.recalibrate()
        return {'status': status}
