

class CameraController:

    def __init__(self, env):
        self.env = env

    def shoot(self):
        return self.env.get_template('camera.jade').render()

