import cv2
import numpy as ny

class NotAnImagePath(Exception):
    """Custom `Exception` class
    """
    pass

class ImagePreProcessor():
    """ ### ImagePreProcessor  
    Class created to pre-process and image before attempting to calculate its `Cloud Coverge Index`
    """
    def __init__(self, image_path: str):
        """Initializes a `ImagePreProcessor` `object`

        Args:
          - image_path (`str`): Complete path to source image.

        Raises:
          - NotAnImagePath: If no arguments are passed.
        """
        if not image_path:
            raise NotAnImagePath
        
        try:
          image = cv2.imread(image_path)
        except Exception:
          pass
        finally:
          image = cv2.imread('dump/11773-seg.jpg')

        self.image = image
        self.__images = {
            'rgb': cv2.cvtColor(image, cv2.COLOR_BGR2RGB),
            'hls': cv2.cvtColor(image, cv2.COLOR_BGR2HLS), 
            'hsv': cv2.cvtColor(image, cv2.COLOR_BGR2HSV),
            'gray': cv2.cvtColor(image, cv2.COLOR_BGR2GRAY),
            'b&w': None
        }


    def display(self, image='clean', resolution = (1920,1080)):
        """Resizes an image and displays it in an external window

        Args:  
          - image (`str`, optional): Indicate what type of image to show. Defaults to 'clean'.
            - 'rgb', 'hls', 'hsv', 'gray', 'b&w'
          - resolution (`tuple`, optional): Size to display the image at. Defaults to (1920,1080).
        """
        img = self.fetchImageType(image)
        cv2.namedWindow('otput', cv2.WINDOW_AUTOSIZE)
        display = cv2.resize(img, resolution)
        cv2.imshow('output', display)
        cv2.waitKey(0)


    def write(self, name: str, image='b&w', path='dump/'):
        """Writes a certain image type of a `ImagePreProcessor` `object` to a certain 
            directory

        Args:
          - name (`str`): the name of the image
          - image (`str`, optional): Indicate the type of image to write. Defaults to 'b&w'.
            - 'rgb', 'hls', 'hsv', 'gray', 'clean'
          - path (`str`, optional): Comple path of the directory to write the image on. Defaults to local project 'dump/' folder.

        Raises:
            NotADirectoryError: Raise an `Exception` if directory not found.
        """
        img = self.fetchImageType(image)
        try:
            cv2.imwrite(path + name + '-seg.jpg', img)
        except:
            raise NotADirectoryError


    def _dayMask(self):
        """Obtains a 'day-time' mask of the image

        Returns:
            opencv type `mask`
        """
        low, high = ny.array([0, 192, 0]), ny.array([180, 255, 71])
        hls, rgb = self.fetchImageType(type='hls'), self.fetchImageType(type='rgb')
        mask = cv2.inRange(hls, low, high)
        return cv2.bitwise_and(rgb, rgb, mask= mask)


    def _nightMask(self):
        """Obtains a 'night-time' mask of the image

        Returns:
            opencv type `mask`
        """
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


    def __setImage(self, key: str, result):
        """Sets a new value for an image type of the `object`'s `dict`.  

        Args:
          - key (`str`): Key for the images `dict`
          - result:  New image
        """
        self.__images[key] = result


    def process(self, night_shift= False):
        """Process the image into a binary so its easier to calculate its Cloud Coverge Index.

        Args:
          - night_shift (`bool`, optional): Specify if the image to be processed is a night-time picture. Defaults to False.

        Returns:
          - Binary processed image:
            - clouds: `white`
            - sky: `black`
        """
        if night_shift == True:
            mask = self._nightMask()
            central_channel = 70
        else:
            mask = self._dayMask()
            central_channel = 100

        gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
        (thresh, black_white) = cv2.threshold(gray, central_channel, 255, cv2.THRESH_BINARY)

        self.__setImage('b&w', black_white)
        return self.fetchImageType(type='b&w')
    

    def fetchImageType(self, type= 'clean'):
        """Retrieves from `object`'s image `dict`

        Args:
          - type (`str`, optional): Indicate the type of image to write. Defaults to 'clean'.
            - 'rgb', 'hls', 'hsv', 'gray', 'b&w'. 

        Returns:
          - image
        """
        try:
            return self.__images[type]
        except KeyError:
            return self.image
