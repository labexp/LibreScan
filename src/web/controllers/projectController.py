

class ProjectController:

    def __init__(self, env):
        self.env = env

    def home(self):
        return self.env.get_template('home.jade').render()

    def create(self):
        pass

    def new(self):
        pass

    def get_config(self):
        pass
