
from abc import ABCMeta, abstractmethod


class CameraDriver(metaclass=ABCMeta):

    @abstractmethod
    def detect(self, params):
        pass

    @abstractmethod
    def prepare(self, p_cam_config):
        pass

    @abstractmethod
    def shoot(self, p_save_path, p_pic_names):
        pass

    @abstractmethod
    def rec_mode(self):
        pass

    @abstractmethod
    def set_zoom(self, p_zoom_level):
        pass

    @abstractmethod
    def set_quality(self):
        pass

    @abstractmethod
    def devices_list(self):
        pass

    @abstractmethod
    def calibrate(self):
        pass

    @abstractmethod
    def set_focus(self, p_focus_distance):
        pass
