

class ProjectController:

    def __init__(self, p_env, p_project_service):
        self.env = p_env
        self.project_service = p_project_service

    def home(self):
        return self.env.get_template('home.jade').render()
