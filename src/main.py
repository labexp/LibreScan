from model.project import Project
from services.cameraService import CameraService
from services.projectService import ProjectService
from services.queueService import QueueService
from utils.taskManager import TaskManager


def main():

    # Project service in charge of creating the new project
    ps = ProjectService()
    project = Project(None, 'Marcos Ramírez', 'Libro sobre Marcos Ramírez, esrito porLucho Fallas', 'spa', None, ['pdfbeads'])
    project_path = ps.create(project)

    # TaskManager instance will be used in the threads queue and it will generate the final product.
    t = TaskManager(project_path)
    q = QueueService(t)

    print("Preparing cameras....")
    cs = CameraService(project_path)
    cs.prepare_cams()

    # The next code will take pictures until the user enters an s.
    user_input = input("Presione una tecla para tomar una foto o s para salir: ")
    while user_input != "s":
        taken_pictures = cs.take_pictures()
        q.push(taken_pictures)
        user_input = input("Presione una tecla para tomar una foto o s para salir: ")

    # Blocks the program until the queue threads finish their job.
    q.wait_process()

    # Generates the final products and place them in the new project path's root.
    t.generate()

main()
