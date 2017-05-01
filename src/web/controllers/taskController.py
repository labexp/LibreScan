from bottle import HTTPResponse


class TaskController:

    def __init__(self, p_env, p_output_service):
        self.env = p_env
        self.output_service = p_output_service

    def generate_output(self):
        self.output_service.generate()
        self.output_service.wait_process()  # wait for generating process to end
        return {'status': 1}

    def get_pdf(self):
        working_dir = self.output_service.working_dir
        output_name = self.output_service.output_name
        output_file = open(working_dir + '/' + output_name + '.pdf', "rb")
        headers = {
            'Content-Type': 'application/pdf'
        }
        body = output_file
        return HTTPResponse(body, **headers)
