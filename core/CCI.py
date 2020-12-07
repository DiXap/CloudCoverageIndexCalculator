import numpy as ny
import cv2
from .IPP import ImagePreProcesor as ip

class CloudCoverageIndex():
    def __init__(self, processed_image):
        self.binary = processed_image


    def CCI(self, as_percentaje=False):
        cci = self.getClouds() / self.__relevantArea()
        if as_percentaje:
            return ny.round_(cci * 100, decimals=2)
        return cci

    def getClouds(self):
        clouds = cv2.countNonZero(self.binary)
        return clouds

    def __relevantArea(self, radius=1324):
        area = ny.pi * (radius * radius)
        return area