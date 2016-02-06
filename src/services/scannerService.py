import time
import os
import yaml

from models.cameraConfig import CameraConfig
from patterns.singleton import Singleton
from utils.chdkptpPT import ChdkptpPT
from jpegtran import JPEGImage


class ScannerService(metaclass=Singleton):
    def __init__(self, p_working_dir=None, p_pic_number=0):
        self.working_dir = p_working_dir
        self.camera_config = None
        self.pic_number = p_pic_number
        self.cam_driver = ChdkptpPT()

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

    def take_pictures(self):
        pic_names = []
        save_path = self.working_dir + '/raw/'

        self.pic_number += 1
        pic_names.append("lsp" + str(self.pic_number).zfill(5))
        self.pic_number += 1
        pic_names.append("lsp" + str(self.pic_number).zfill(5))
        self.cam_driver.shoot(save_path, pic_names)
        self.insert_pics_to_file(-1, pic_names)
        self.update_last_pic_number(self.pic_number)
        try:
            self.rotate_photos(pic_names[0], pic_names[1])
        except:
            print("Exception, pictures were not found yet.")
            time.sleep(1)
            self.rotate_photos(pic_names[0], pic_name[1])
        return pic_names

    def prepare_cams(self):
        self.cam_driver.detect_cams()
        self.cam_driver.prepare(self.camera_config)

    def rotate_photos(self, p_left_photo, p_right_photo):
        time.sleep(0.4)
        save_path = self.working_dir + '/raw/'

        left = JPEGImage(save_path + p_left_photo + ".jpg")
        right = JPEGImage(save_path + p_right_photo + ".jpg")

        left.rotate(90).save(save_path + p_left_photo + ".jpg")
        right.rotate(270).save(save_path + p_right_photo + ".jpg")

    def delete_photos(self, p_photo_list):
        pics_file = self.working_dir + '/.pics.ls'
        f = open(pics_file, "r")
        contents = f.readlines()
        f.close()

        for photo in p_photo_list:
            os.remove(self.working_dir + "/raw/" + photo + ".jpg")
            contents.remove(photo + '\n')

        f = open(pics_file, "w")
        f.writelines(contents)
        f.close()

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
            contents.insert(p_index + 1, pic + '\n')
            p_index += 1

        f = open(pics_file, "w")
        f.writelines(contents)
        f.close()

    def get_last_photo_names(self):
        pics_file = self.working_dir + '/.pics.ls'
        f = open(pics_file, "r")
        contents = f.readlines()
        f.close()

        last_pics = []
        if len(contents) > 1:
            last_pics = contents[-2:]
        return last_pics
