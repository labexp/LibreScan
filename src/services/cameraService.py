from threading import Thread
import time
import os

from PIL import Image
import yaml
import base64

from models.camera import Camera
from models.cameraConfig import CameraConfig
from patterns.singleton import Singleton
from utils.chdkptp import Chdkptp


class CameraService(metaclass=Singleton):

    def __init__(self, p_working_dir=None, p_pic_number=0):
        self.cams = [Camera("head"), Camera("tail")]
        self.working_dir = p_working_dir
        self.camera_config = None
        self.pic_number = p_pic_number

    def set_save_path(self, p_working_dir):
        self.working_dir = p_working_dir + "/raw/"

    def set_camera_config(self):
        self.camera_config = self.get_configuration()

    def get_configuration(self):
        config_path = self.working_dir + "/.projectConfig.yaml"
        f = open(config_path)
        data_map = yaml.safe_load(f)["camera"]
        f.close()
        return CameraConfig(data_map["zoom"], data_map["iso"])

    def take_pictures(self, p_last_pic_index=-1):
        jobs = []
        pic_names = []
        save_path = self.working_dir + '/raw/'
        for cam in self.cams:
            self.pic_number += 1
            pic_name = "lsp"+str(self.pic_number).zfill(5)
            pic_names.append(pic_name)
            process = Thread(target=Chdkptp.shoot, args=(cam, save_path + pic_name))
            jobs.append(process)
            process.start()
            time.sleep(0.000005)

        for j in jobs:
            j.join()

        self.update_last_pic_number(self.pic_number)
        self.insert_pics_to_file(p_last_pic_index, pic_names)
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
        save_path = self.working_dir + '/raw/'
        with Image.open(save_path + p_left_photo+".jpg") as left_photo:
            left_photo = left_photo.rotate(90)
            left_photo.save(save_path + p_left_photo+".jpg")
            left_photo.close()
        with Image.open(save_path + p_right_photo+".jpg") as right_photo:
            right_photo = right_photo.rotate(270)
            right_photo.save(save_path + p_right_photo+".jpg")
            right_photo.close()

    def delete_photos(self, p_photo_list):
        pics_file = self.working_dir + '/.pics.ls'
        f = open(pics_file, "r")
        contents = f.readlines()
        f.close()

        print(contents)

        for photo in p_photo_list:
            os.remove(self.working_dir + "/raw/" + photo + ".jpg")
            contents.remove(photo + '\n')

        f = open(pics_file, "w")
        f.writelines(contents)
        f.close()

    def encode_image(self, p_img_name):
        image_file = open(self.working_dir + '/raw/' + p_img_name + '.jpg', "rb")
        encoded_string = base64.b64encode(image_file.read())
        image_file.close()
        return encoded_string.decode(encoding="UTF-8")  # convert it to string

    def update_last_pic_number(self, p_pic_number):
        config_path = self.working_dir + "/.projectConfig.yaml"
        f = open(config_path)
        data_map = yaml.safe_load(f)
        f.close()
        data_map['camera']['last-pic-number'] = p_pic_number
        f = open(config_path, 'w')
        f.write(yaml.dump(data_map, default_flow_style=False, allow_unicode=True))
        f.close()

    def insert_pics_to_file(self, p_index, pic_list):
        pics_file = self.working_dir + '/.pics.ls'
        f = open(pics_file, "r")
        contents = f.readlines()
        f.close()

        if p_index == -1:
            p_index = len(contents) - 1

        for pic in pic_list:
            contents.insert(p_index+1, pic + '\n')
            p_index += 1

        f = open(pics_file, "w")
        f.writelines(contents)
        f.close()


