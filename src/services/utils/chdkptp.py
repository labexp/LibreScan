__author__ = 'diugalde'

import subprocess
from subprocess import call
from model.camera import Camera


class Chdkptp:

    # chdkPath to CHDKPTP
    global chdkPath
    chdkPath = '/usr/bin/chdkptp'

    


    @staticmethod
    def shoot(pCam, pSavePath):
        subprocess.call(chdkPath + " -e\"connect -b=" + pCam.usbBus + " -d=" + pCam.usbId + "\" -e\"remoteshoot " + pSavePath + " -tv=1/25\"", shell=True)

    @staticmethod
    def prepare(pCam):
        pCam.usbBus = subprocess.check_output("("+chdkPath+" -elist |" + pCam.pos + " -n1| cut -f4 -d' '| sed -e 's/b\=//g')", shell=True).decode("utf-8")[:-1]
        pCam.usbId = subprocess.check_output("(" + chdkPath + " -elist |" + pCam.pos + " -n1| cut -f5 -d' '| sed -e 's/d\=//g')", shell=True).decode("utf-8")[:-1]
        subprocess.call(chdkPath + " -e\"connect -b=" + pCam.usbBus + " -d=" + pCam.usbId + "\" -e'download orientation.txt /tmp'", shell=True)
        pCam.orientation = subprocess.check_output("(cat /tmp/orientation.txt)", shell=True)
        call("rm -rf /tmp/orientation.txt", shell=True)

    @staticmethod
    def recMode(pCam):
        subprocess.call(chdkPath + " -e\"connect -b=" + pCam.usbBus + " -d=" + pCam.usbId + "\" -erec", shell=True)

    @staticmethod
    def setFlash(pCam):
        subprocess.call(chdkPath + " -e\"connect -b="+pCam.usbBus + " -d=" + pCam.usbId +"\" -e'lua while(get_flash_mode()<2) do click(\"right\") end' ",shell=True)

    @staticmethod
    def setZoom(pCam, pZoomLevel):
        subprocess.call(chdkPath + "-e\"connect -b=" + pCam.usbBus + " -d=" + pCam.usbId + "\" -e'lua while(get_zoom()<" + str(pZoomLevel) + ") do click(\"zoom_out\") end'", shell=True)

