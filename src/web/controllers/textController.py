# -*- coding: utf-8 -*-
from bottle import request
from services.hocrService import HocrService
from services.libhOCR import libhOCR as lib


class TextController:
    '''
        Class that manage text processes of Jabiru
    '''
    def __init__(self, hocr_service):
        self.hocr_service = hocr_service
        self.lib = lib()

    def get_text(self, id):
        '''
            Function that get a string of a .hocr file

            Input:
                id  -  Number associated of the .hocr file

            Returns a josn object with the string of the .hocr file
        '''
        text_name = self.hocr_service.get_path_file(id)
        print(text_name)
        self.lib.process(text_name)
        temp_line = "a"
        result_lines = ""
        number_line = 1
        while(temp_line != ""):
            temp_line = self.lib.get_line(text_name, number_line)
            number_line += 1
            result_lines += temp_line+"\n"
        return {'text': result_lines}

    def save_text(self, id):
        '''
            Function that save the edited text into the associated .hocr file

            Input:
                id  -  Number associated of the .hocr file

            Return a json object with the status of the operation

        '''
        data = request.json
        print(data)
        path = self.hocr_service.get_path_file(id)
        lines = data['text'].split("\n")
        number_lines = 1
        for x in range(len(lines)):
            self.lib.edit_line(path, number_lines, lines[x])
            number_lines += 1
        return {'status': 'status'}
