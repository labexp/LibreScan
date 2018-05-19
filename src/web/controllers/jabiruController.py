class JabiruController:

    def __init__(self, env):
        self.env = env

    def home(self):
        '''
            Return a Jabiru home page.
        '''
        return self.env.get_template('jabiru.jade').render()
