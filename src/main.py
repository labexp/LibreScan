from services.cameraService import CameraService
from services.queueService import QueueService
from services.utils.taskManager import TaskManager


def main():
    project_path = "/home/sd/LibreScanProjects/L3/raw/"
    cs = CameraService(project_path)
    cs.prepare_cams()
    t = TaskManager(project_path)
    q = QueueService(t)
    user_input = input("Presione una tecla para tomar una foto o s para salir: ")
    while user_input != "s":
        taken_pictures = cs.take_pictures()
        q.push(taken_pictures)
        user_input = input("Presione una tecla para tomar una foto o s para salir: ")
    print(q.get_active_threads())

    q.wait_process()
    t.generate()

main()
