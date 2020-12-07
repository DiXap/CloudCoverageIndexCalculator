import numpy as ny
import cv2
from .IPP import ImagePreProcessor as ip

class CloudCoverageIndex():
    """Dedicated class to calculate `Cloud Coverage Index`
    """
    def __init__(self, processed_image):
        self.binary = processed_image


    def CCI(self, as_percentaje=False):
        """Calculates the `Cloud Coverage Index` of a given binary image.

        Args:
          - as_percentaje (`bool`, optional): Obtain the `CCI` as decimal (`False`) or percentaje (`True`). Defaults to `False`.

        Returns:
          - `Cloud Coverage Index`
        """
        cci = self.getClouds() / self.__relevantArea()
        if as_percentaje:
            return ny.round_(cci * 100, decimals=2)
        return cci

    def getClouds(self):
        """Obtains the non-zero (`white`) pixels of the image.

        Returns:
          - Number of non-zero pixels 
        """
        clouds = cv2.countNonZero(self.binary)
        return clouds

    def __relevantArea(self, radius=1324):
        """Gets the relevant area of the image.

        Args:
          - radius (`int`, optional): Radius of the relevant image area. Defaults to 1324.

        Returns:
          - `area`
        """
        area = ny.pi * (radius ** 2)
        return area