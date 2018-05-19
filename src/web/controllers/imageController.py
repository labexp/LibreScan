from jpegtran import JPEGImage
from bottle import HTTPResponse
import os
import glob


class ImageController:
    '''
        Class that manage all the final images of a proyect
    '''

    def __init__(self, image_service):
        self.image_service = image_service

    def get_image(self, p_id):
        '''
            Function that returns a image asociate to a page of the document

            Input:
                p_id  -  Number of the asociated page

            Return a HTTP response with the image in .jpg format
        '''
        path = os.environ["LS_PROJECT_PATH"]+'/processed/'

        l = glob.glob(path + '*.tif')
        l.sort()

        image_name = l[int(p_id)]

        temp = image_name.split('.')
        new_image = temp[0]
        new_image = new_image + ".jpg"

        if not os.path.isfile(new_image):
            self.image_service.convert_image(image_name)

        headers = {
            'Content-Type': 'image/jpg'
        }
        image = JPEGImage(new_image)
        body = image.as_blob()
        return HTTPResponse(body, **headers)

    def get_last_id(self):
        '''
            Function that return the id of the last image on the proyect

            Return a json object with the information
        '''
        last_line = 0
        infile = open(os.environ["LS_PROJECT_PATH"] + '/.pics.ls', 'r')

        for line in infile:
            last_line += 1

        infile.close()

        return {'last_id': last_line}
