

class CameraController:

    def __init__(self, p_env, p_camera_service, p_queue_service):
        self.env = p_env
        self.camera_service = p_camera_service
        self.queue_service = p_queue_service

    def shoot(self):
        return self.env.get_template('camera.jade').render()

