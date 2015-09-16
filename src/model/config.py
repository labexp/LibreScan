__author__ = 'labexp'

class Config:

    def __init__(self, pZoom, pFocusDistance, pShutterSpeed, pDpi, pSensibility, pRaw, pMonochromatic, pFlip):
        self.zoom = pZoom
        self.focusDistance = pFocusDistance
        self.shutterSpeed  = pShutterSpeed
        self.dpi = pDpi
        self.sensibility = pSensibility
        self.raw = pRaw
        self.monochromatic = pMonochromatic
        self.flip = pFlip

    