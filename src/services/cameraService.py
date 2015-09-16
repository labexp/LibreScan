__author__ = 'tonyzeru'

from model.camera import Camera
from services.utils.chdkptp import Chdkptp
import multiprocessing


class CameraService:

    global savePath
    savePath = "/home/diugalde/LibreScanProjects/L1/raw/"

    picNumber = 0

    def __init__(self):
        self.cams = [Camera("head"), Camera("tail")]

    def takePictures(self):
        jobs = []
        for cam in self.cams:
            CameraService.picNumber += 1
            process = multiprocessing.Process(target=Chdkptp.shoot, args=(cam, savePath+str(CameraService.picNumber)))
            jobs.append(process)
            process.start()

        for j in jobs:
            j.join()

    def prepareCams(self):
        for cam in self.cams:
            Chdkptp.prepare(cam)
        for cam in self.cams:
            Chdkptp.recMode(cam)

<<<<<<< HEAD
    def prepare(self):
        pass    
=======
>>>>>>> upstream/develop

cs = CameraService()
cs.prepareCams()
cs.takePictures()
