# -*- coding: utf-8 -*-
from bottle import request
from services.hocrService import HocrService
import services.libhOCR as lib

class TextController:
    def __init__(self, hocr_service):
        self.hocr_service = hocr_service

    def get_text(self, id):
        text_name = self.hocr_service.get_path_file(id)
        print(text_name)
        temp_line = "a"
        result_lines = ""
        number_line = 1
        while(temp_line!=""):
            temp_line = lib.get_line(text_name, number_line)
            number_line+=1
            result_lines += temp_line+"\n"
        return {'text' : result_lines}



    def save_text(self, id):
        data = request.json
        print(data)
        path = self.hocr_service.get_path_file(id)
        status = self.hocr_service.save_hocr_text(path, data['text'])
        lines = data['text'].split("\n")
        number_lines = 1
        for x in range(len(lines)):
            lib.edit_line(path, number_lines, lines[x])
            number_lines+=1
        return {'status' : 'status'}
