
import subprocess
from subprocess import call
from model.camera import Camera
from utils.cameraDriver import CameraDriver


class Chdkptp(CameraDriver):

    # chdk_path to CHDKPTP
    global chdk_path
    chdk_path = '/usr/bin/chdkptp'

    @staticmethod
    def string_maker(p_usb_bus, p_usb_id, p_extra):
        chdk_string = "%s  -e\"connect -b=%s -d=%s%s" \
            % (chdk_path, p_usb_bus, p_usb_id, p_extra)
        print(chdk_string)
        return chdk_string

    @staticmethod
    def connect_string(p_cam):
        bus_string = "(%s -elist | %s -n1| cut -f4 -d' '| sed -e 's/b\=//g')" \
            % (chdk_path, p_cam.pos)
        
        id_string = "(%s -elist | %s -n1| cut -f5 -d' '| sed -e 's/d\=//g')" \
            % (chdk_path, p_cam.pos)

        p_cam.usb_bus = subprocess.check_output(bus_string, shell=True).decode("utf-8")[:-1]
        p_cam.usb_id = subprocess.check_output(id_string, shell=True).decode("utf-8")[:-1]
        
        return p_cam
        
    @staticmethod
    def shoot(p_cam, p_save_path):
        extra = "\" -e\"remoteshoot " + p_save_path + " -tv=1/25\""
        call(Chdkptp.string_maker(p_cam.usb_bus, p_cam.usb_id, extra), shell=True)

    @staticmethod
    def prepare(p_cam):
        p_cam = Chdkptp.connect_string(p_cam)
        extra = "\" -e'download orientation.txt /tmp'"
        call(Chdkptp.string_maker(p_cam.usb_bus, p_cam.usb_id, extra), shell=True)
        p_cam.orientation = subprocess.check_output("(cat /tmp/orientation.txt)", shell=True)
        call("rm -rf /tmp/orientation.txt", shell=True)

    @staticmethod
    def recMode(p_cam):
        extra = "\" -erec"
        call(Chdkptp.string_maker(p_cam.usb_bus, p_cam.usb_id, extra), shell=True)

    @staticmethod
    def setFlash(p_cam):
        extra = "\" -e'lua while(get_flash_mode()<2) do click(\"right\") end' "
        call(Chdkptp.string_maker(p_cam.usb_bus, p_cam.usb_id, extra), shell=True)

    @staticmethod
    def setZoom(p_cam, pZoomLevel):
        extra = "\" -e'lua while(get_zoom()<" + str(pZoomLevel) + ") do click(\"zoom_out\") end'"
        call(Chdkptp.string_maker(p_cam.usb_bus, p_cam.usb_id, extra), shell=True)
