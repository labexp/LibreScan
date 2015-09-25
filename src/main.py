from services.cameraService import CameraService
from PIL import Image
from services.utils.taskManager import TaskManager
from services.queueService import queueSerivice
import threading
'''
cs = CameraService()
cs.prepare_cams()
userInput = input("Presione una tecla para tomar una foto o s para salir: ")
while userInput != "s":
    cs.take_pictures()
    userInput = input("Presione una tecla para tomar una foto o s para salir: ")

# Procesa 6 imagenes, recordar cambiar la ruta en CameraService y en la línea siguiente.
t = TaskManager("/home/diugalde/LibreScanProjects/L1/raw/")
t.process(["1", "2", "3", "4", "5", "6"])
t.generate() '''
def main():
    q = queueSerivice()
    q.push(["010", "012", "013", "014", "015", "016"])
    print(q.get_active_threads())




