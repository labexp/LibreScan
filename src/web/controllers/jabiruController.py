class JabiruController:
    def __init__(self, env):
        self.env = env

    def home(self):
        return self.env.get_template('jabiru.jade').render()
