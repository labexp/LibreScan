import subprocess
import datetime
from subprocess import call

import rotateImages
import renImages

# Path to CHDKPTP
CHDKPTP= '/usr/bin/chdkptp'

CAM1_USBBUS = ""
CAM1_USBSID = ""
CAM1_ORIENTATION = ""

CAM2_USBBUS = ""
CAM2_USBSID = ""
CAM2_ORIENTATION = ""

scanDir = ""
#Crear folder



# Create directories for saving the pictures.
def createScanDir():
    global scanDir
    timestamp = datetime.datetime.now().strftime("%A_%d_%B_%Y_%I:%M%p")
    scanDir = "libroEscaneado_" + timestamp
    subprocess.call("mkdir -p " + scanDir,shell=True)
    subprocess.call("mkdir -p " + scanDir + "/left",shell=True)
    subprocess.call("mkdir -p " + scanDir + "/right",shell=True)





# Funciones del CHDKPTP
def detectCams():
    global CAM2_USBBUS
    global CAM2_USBSID
    global CAM1_USBBUS
    global CAM1_USBSID
    global CAM1_ORIENTATION
    global CAM2_ORIENTATION
    
    CAM1_USBBUS = subprocess.check_output("("+CHDKPTP +" -elist |head -n1| cut -f4 -d' '| sed -e 's/b\=//g')", shell=True).decode("utf-8")[:-1]
    CAM1_USBSID = subprocess.check_output("("+CHDKPTP +" -elist|head -n1| cut -f5 -d' '| sed -e 's/d\=//g')", shell=True).decode("utf-8")[:-1]
    call(CHDKPTP + " -e\"connect -b=" + CAM1_USBBUS + " -d=" + CAM1_USBSID+ "\" -e'download orientation.txt /tmp'", shell = True)
    CAM1_ORIENTATION  = subprocess.check_output("(cat /tmp/orientation.txt)", shell=True).decode("utf-8")
    call( "rm -rf /tmp/orientation.txt",shell=True)

    CAM2_USBBUS = subprocess.check_output("("+CHDKPTP +" -elist |tail -n1| cut -f4 -d' '| sed -e 's/b\=//g')", shell=True).decode("utf-8")[:-1]
    CAM2_USBSID = subprocess.check_output("("+CHDKPTP +" -elist|tail -n1| cut -f5 -d' '| sed -e 's/d\=//g')", shell=True).decode("utf-8")[:-1]
    call(CHDKPTP + " -e\"connect -b=" + CAM2_USBBUS + " -d=" + CAM2_USBSID+ "\" -e'download orientation.txt /tmp'", shell = True)
    CAM2_ORIENTATION  = subprocess.check_output("(cat /tmp/orientation.txt)", shell=True).decode("utf-8")
    call( "rm -rf /tmp/orientation.txt",shell=True)

    #CAM1_ORIENTATION = CAM1_ORIENTATION.strip()
    #CAM2_ORIENTATION = CAM2_ORIENTATION.strip()
    print(CAM1_ORIENTATION)
    print(CAM2_ORIENTATION)
    print("Cams detected.")

def recMode():
    call(CHDKPTP +" -e\"connect -b="+CAM2_USBBUS+" -d="+CAM2_USBSID +"\" -erec", shell=True)
    call(CHDKPTP +" -e\"connect -b="+CAM1_USBBUS+" -d="+CAM1_USBSID +"\" -erec", shell=True)
    print("Rec mode set.")

def shoot():
    call(CHDKPTP + " -e\"connect  -b=" + CAM2_USBBUS + " -d=" + CAM2_USBSID +"\" -e\"remoteshoot " + scanDir + "/" + str(CAM1_ORIENTATION) + " -tv=1/25\"", shell=True)
    call(CHDKPTP + " -e\"connect  -b=" + CAM1_USBBUS + " -d=" + CAM1_USBSID +"\" -e\"remoteshoot " + scanDir + "/" + str(CAM2_ORIENTATION) + " -tv=1/25\"", shell=True)
    print("Shooting done.")

def setFlash():
    call(CHDKPTP + " -e\"connect -b="+CAM1_USBBUS +" -d="+CAM1_USBSID +"\" -e'lua while(get_flash_mode()<2) do click(\"right\") end' ",shell=True)
    print("Flash set")

def setZoom(pZoomLevel):
    call(CHDKPTP + "-e\"connect -b="+CAM1_USBBUS +" -d="+CAM1_USBSID+"\" -e'lua while(get_zoom()<"+str(pZoomLevel)+") do click(\"zoom_in\") end'",shell=True)
    call(CHDKPTP + "-e\"connect -b="+CAM1_USBBUS +" -d="+CAM1_USBSID+"\" -e'lua while(get_zoom()<"+str(pZoomLevel)+") do click(\"zoom_out\") end'",shell=True)

    call(CHDKPTP + "-e\"connect -b="+CAM2_USBBUS +" -d="+CAM2_USBSID +"\" -e'lua while(get_zoom()<"+str(pZoomLevel)+") do click(\"zoom_in\") end'",shell=True)
    call(CHDKPTP + "-e\"connect -b="+CAM2_USBBUS+" -d="+CAM2_USBSID +"\" -e'lua while(get_zoom()<"+str(pZoomLevel)+") do click(\"zoom_out\") end'",shell=True)
    print("Zoom set at " + str(pZoomLevel))


def makeBook():
    print("Making book...")
   
    call("mkdir "+scanDir + "/renamed",shell=True)
    call("mkdir "+scanDir + "/rotated",shell=True)    


    print("Renaming...")
    renImages.rename(scanDir,"left")
    renImages.rename(scanDir,"right")
    print("Rotating...")
    rotateImages.rotateImages(scanDir)


    call("cd "+scanDir + "/rotated",shell=True)
    call("mkdir patata",shell=True)

    
    print("Creating pdf...")
    call("scantailor-cli -l=1.5 --threshold=4 --margins-top=2.5 --margins-right=2.5 --margins-bottom=2.5 --margins-left=2.5 "+scanDir+"/rotated/*.jpg "+scanDir,shell=True)
    call("parallel tesseract -l spa {} {.} hocr ::: "+ scanDir+"/rotated/*.tif ",shell=True)
    call("pdfbeads "+ scanDir +"/rotated/*.tif > "+ scanDir +"/out.pdf",shell=True)
    print("Done!")

#detectCams()


#createScanDir()
#detectCams()
#recMode()
#setFlash()
#setZoom(3)
#shoot()
#makeBook()
