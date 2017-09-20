import xml.etree.ElementTree as ET
import os
import glob


class HocrService:
    def __init__(self):
        pass

    def get_path_file(self, id):
        path = os.environ["LS_PROJECT_PATH"]+'/processed/' #este va a ser el path de la imagen
        
        l = glob.glob(path + '*.hocr')
        l.sort()
        
        text_name = l[int(id)]
        return text_name
