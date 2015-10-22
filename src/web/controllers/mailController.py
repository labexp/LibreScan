

class MailController:

    def __init__(self, p_env, p_mail_service):
        self.env = p_env
        self.mail_service = p_mail_service

    def home(self):
        return self.env.get_template('home.jade').render()
