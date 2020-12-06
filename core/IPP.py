import cv2
import numpy as ny

class NotAnImagePath(Exception):
    pass

class ImagePreProcesor():
    """[summary]
    """
    def __init__(self, image_path: str):
        if not image_path:
            raise NotAnImagePath
        
        image = cv2.imread(image_path)
        self.image = image
        self.__images = {
            'rgb': cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
            'hls': cv2.cvtColor(image, cv2.COLOR_BGR2HLS), 
            'hsv': cv2.cvtColor(image, cv2.COLOR_BGR2HSV),
            'gray': cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
            'b&w': None
        }


    def display(self, image='clean', resolution = (1920,1080)):
        img = self.fetchImageType(image)
        cv2.namedWindow('otput', cv2.WINDOW_AUTOSIZE)
        display = cv2.resize(img, resolution)
        cv2.imshow('output', display)
        cv2.waitKey(0)


    def write(self, name: str, image='b&w', path='dump/'):
        img = self.fetchImageType(image)
        try:
            cv2.imwrite(path + name + '-seg.jpg', img)
        except:
            raise NotADirectoryError


    def _dayMask(self):
        low, high = ny.array([0, 192, 0]), ny.array([180, 255, 71])
        hls, rgb = self.fetchImageType(type='hls'), self.fetchImageType(type='rgb')
        mask = cv2.inRange(hls, low, high)
        return cv2.bitwise_and(rgb, rgb, mask= mask)


    def _nightMask(self):
        image = self.image
        ret, mask = cv2.threshold(image[:, :,1], 200, 255, cv2.COLOR_BGR2HLS)
        mask3 = ny.zeros_like(image)
        mask3[:,:,2] = mask3[:,:,2] = mask3[:,:,1] = mask   

        orange = cv2.bitwise_and(image, mask3)
        gray = self.fetchImageType('gray') 
        image = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
        gray = cv2.bitwise_and(image, 255 - mask3)
        out = gray + orange
        return out


    def __setResult(self, key, result):
        self.__images[key] = result


    def process(self, night_shift= False):
        if night_shift == True:
            mask = self._nightMask()
            central_channel = 70
        else:
            mask = self._dayMask()
            central_channel = 100

        gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        (thresh, black_white) = cv2.threshold(gray, central_channel, 255, cv2.THRESH_BINARY)

        self.__setResult('b&w', black_white)
        return self.fetchImageType(type='b&w')
    

    def fetchImageType(self, type= 'clean'):
        try:
            return self.__images[type]
        except KeyError:
            return self.image
