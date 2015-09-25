from model.camera import Camera
from services.utils.chdkptp import Chdkptp
from threading import Thread
from PIL import Image
import time


class CameraService:

    global save_path
    save_path = "/home/diugalde/LibreScanProjects/L1/raw/"

    pic_number = 0

    def __init__(self):
        self.cams = [Camera("head"), Camera("tail")]

    def take_pictures(self):
        jobs = []
        for cam in self.cams:
            CameraService.pic_number += 1
            process = Thread(target=Chdkptp.shoot, args=(cam, save_path+str(CameraService.pic_number)))
            jobs.append(process)
            process.start()
            time.sleep(0.0005)

        for j in jobs:
            j.join()

        self.rotate(CameraService.pic_number-1, CameraService.pic_number)

    def prepare_cams(self):
        for cam in self.cams:
            Chdkptp.prepare(cam)
        for cam in self.cams:
            Chdkptp.recMode(cam)

        if self.cams[0].orientation == "left":
            self.cams.reverse()

    def rotate(self, p_left_photo, p_right_photo):
        left_photo = Image.open(save_path + str(p_left_photo)+".jpg")
        right_photo = Image.open(save_path + str(p_right_photo)+".jpg")
        left_photo = left_photo.rotate(90)
        right_photo = right_photo.rotate(270)
        left_photo.save(save_path + str(p_left_photo)+".jpg")
        right_photo.save(save_path + str(p_right_photo)+".jpg")

