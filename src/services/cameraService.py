from model.camera import Camera
from services.utils.chdkptp import Chdkptp
import multiprocessing


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
            process = multiprocessing.Process(target=Chdkptp.shoot, args=(cam, save_path+str(CameraService.pic_number)))
            jobs.append(process)
            process.start()

        for j in jobs:
            j.join()

    def prepare_cams(self):
        for cam in self.cams:
            Chdkptp.prepare(cam)
        for cam in self.cams:
            Chdkptp.recMode(cam)
