from threading import Thread
import time

from PIL import Image
from pathlib import Path
import yaml

from models.camera import Camera
from models.cameraConfig import CameraConfig
from patterns.singleton import Singleton
from utils.chdkptp import Chdkptp


class CameraService(metaclass=Singleton):

    pic_number = 0

    def __init__(self):
        self.cams = [Camera("head"), Camera("tail")]
        self.save_path = None
        self.camera_config = None

    def set_save_path(self, p_working_dir):
        self.save_path = p_working_dir + "/raw/"

    def set_camera_config(self):
        self.camera_config = self.get_configuration()

    def get_configuration(self):
        path_object = Path(self.save_path)
        config_path = str(path_object.parents[0])+"/.projectConfig.yaml"
        f = open(config_path)
        data_map = yaml.safe_load(f)["camera"]
        f.close()
        return CameraConfig(data_map["zoom"], data_map["iso"])

    def take_pictures(self):
        jobs = []
        pic_names = []
        for cam in self.cams:
            CameraService.pic_number += 1
            pic_name = "lsp"+str(CameraService.pic_number).zfill(5)
            pic_names.append(pic_name)
            process = Thread(target=Chdkptp.shoot, args=(cam, self.save_path + pic_name))
            jobs.append(process)
            process.start()
            time.sleep(0.0005)

        for j in jobs:
            j.join()

        self.rotate(pic_names[0], pic_names[1])
        return pic_names

    def prepare_cams(self):
        for cam in self.cams:
            Chdkptp.prepare(cam, self.camera_config)
        for cam in self.cams:
            Chdkptp.rec_mode(cam)
        if self.cams[0].orientation == "left":
            self.cams.reverse()

    def rotate(self, p_left_photo, p_right_photo):
        left_photo = Image.open(self.save_path + p_left_photo+".jpg")
        right_photo = Image.open(self.save_path + p_right_photo+".jpg")
        left_photo = left_photo.rotate(90)
        right_photo = right_photo.rotate(270)
        left_photo.save(self.save_path + p_left_photo+".jpg")
        right_photo.save(self.save_path + p_right_photo+".jpg")

