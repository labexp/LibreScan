import base64


class TaskController:

    def __init__(self, p_env, p_output_service):
        self.env = p_env
        self.output_service = p_output_service

    def generate_output(self):
        self.output_service.generate()
        self.output_service.wait_process()  # wait for generating process to end
        working_dir = self.output_service.working_dir
        output_name = self.output_service.output_name
        output_file = open(working_dir + '/' + output_name + '.pdf', "rb")
        encoded_string = base64.b64encode(output_file.read())
        output_file.close()
        return encoded_string.decode(encoding="UTF-8")  # convert it to string
