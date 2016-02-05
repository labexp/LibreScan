import base64
import sys
from bottle import HTTPResponse
from utils.log import Log
from jpegtran import JPEGImage

class CameraController:
    def __init__(self, p_env, p_camera_service, p_queue_service):
        self.env = p_env
        self.camera_service = p_camera_service
        self.queue_service = p_queue_service
        self.pending_pics = []

    def create(self):

        pic_names = self.camera_service.take_pictures()

        if len(self.pending_pics) != 0:
            self.queue_service.push(self.pending_pics)
        self.pending_pics = pic_names

        return {'photo1': pic_names[0], 'photo2': pic_names[1], 'status': 1}


    def update(self):
        pic_names = self.camera_service.take_pictures()
        self.camera_service.delete_photos(self.pending_pics)
        self.pending_pics = pic_names
        return {'photo1': pic_names[0], 'photo2': pic_names[1], 'status': 1}

    def prepare_devices(self):
        try:
            pass
            self.camera_service.set_camera_config()
            self.camera_service.prepare_cams()
        except:
            print("Unexpected error:", sys.exc_info()[0])
            log = Log()
            log.log_error('Error in the method set_new_project_config')
            return {'status': 1}
        return {'status': 1}

    def delete(self):
        pass

    def stop_scanning(self):
        self.queue_service.push(self.pending_pics)
        self.queue_service.wait_process()
        return {'ready': True}

    def get_thumbnail(self, id):
        return self._get_img_response(id)

    def get_photo(self, id):
        return self._get_img_response(id, False)

    def _get_img_response(self, id, thumb=True):
        path = "{0}/raw/{1}.jpg".format(self.camera_service.working_dir, id)
        headers = {
            'Content-Type': 'image/jpg'
        }
        image = JPEGImage(path)
        if thumb:
            image = image.exif_thumbnail
        body = image.as_blob()
        return HTTPResponse(body, **headers)