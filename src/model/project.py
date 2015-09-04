__author__ = 'diugalde'


class Project:

    def __init__(self, pId, pName, pDescription, pLang, pCamConfig, pOutputFormats):
        self.id = pId
        self.name = pName
        self.description = pDescription
        self.lang = pLang
        self.camConfig = pCamConfig
        self.outputFormats = pOutputFormats
