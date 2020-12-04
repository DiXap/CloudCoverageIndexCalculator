import cv2
import numpy as ny

class NotAnImagePath(Exception):
    print('This is not a valid image path')

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
            'gray': cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        }


    def display(self, resolution = (1920,1080)):
        cv2.namedWindow('otput', cv2.WINDOW_AUTOSIZE)
        display = cv2.resize(self.image, resolution)
        cv2.imshow('output', display)
        cv2.waitKey(0)


    def __dayMask(self):
        low, high = ny.array([0, 192, 0]), ny.array([180, 255, 71])
        hls, rgb = self.fetchImageType(type='hls'), self.fetchImageType(type='rgb')
        mask = cv2.inRange(hls, low, high)
        return cv2.bitwise_and(rgb, rgb, mask= mask)

    def __nightMask(self):
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


    def process(self, night_shift= False):
        if night_shift == True:
            mask = self.__nightMask()
            central_channel = 70
        else:
            mask = self.__dayMask()
            central_channel = 100

        gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        (thresh, black_white) = cv2.threshold(gray, central_channel, 255, cv2.THRESH_BINARY)

        return black_white
    

    def fetchImageType(self, type= 'clean'):
        try:
            return self.__images[type]
        except KeyError:
            return self.image

if __name__ == "__main__":
    
    try:
        image = ImagePreProcesor('images/11773.JPG')
    except:
        image = ImagePreProcesor('images/control.jpg')
    
    img_b = image.process(night_shift=True)



    cv2.namedWindow("output", cv2.WINDOW_AUTOSIZE)
    imS = cv2.resize(img_b, (1920, 1080))
    cv2.imshow("output", imS)
    cv2.waitKey(0)