from bottle import request

class ProjectController:

    def __init__(self, env):
        self.env = env

    def home(self):
        return self.env.get_template('home.jade').render()

    def create(self):
        for params in request.params:
            print(request.params[params])

        return self.env.get_template('newProject.jade').render()

    def new(self):
        return self.env.get_template('newProject.jade').render()

    def delete(self, p_id):
        return "ok"

    def get_config(self, p_id):
        return "ok"
