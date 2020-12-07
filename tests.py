import core.ArgsParser as args
from core.IPP import ImagePreProcessor
from core.CCI import CloudCoverageIndex
import sys
import cv2 as cv
import os

IMG = cv.imread('images/11773.JPG')

def test1():
    """Function to test if error handling is working for `ImagePreProcessor.__init__()`.  
        It's expected for the `__init__` function to initialize with a default image.  

    Returns:
      - `1` : If the error is handled as expected
      - `0` : In other case
    """
    dummy = "error.jpg"
    response = ImagePreProcessor(dummy)
    if response:
        return 1
    return 0

def test2():
    """Function to test if error handling is working for `CloudCoverageIndex.__init__()`.  
        
    Returns:
      - `1` : If the error is handled as expected
      - `0` : In other case
    """
    newsize = (100, 100)
    output = cv.resize(IMG, newsize)
    cv.imwrite("res.jpg", output)
    dummy = "res.jpg"
    response = CloudCoverageIndex(dummy)
    print("Relevant area: ", response._CloudCoverageIndex__relevantArea())
    os.remove("res.jpg")
    if response.binary == "res.jpg" and response._CloudCoverageIndex__relevantArea() != 0:
        return 1
    else:
        return 0

def test3():
    """Function to test if error handling is working for `ImagePreProcessor.fetchImageType()`.  
        It's expected for the function to return a default image if it couldn't find the requested one.  
        
    Returns:
      - `1` : If the error is handled as expected
      - `0` : In other case
    """
    image = ImagePreProcessor('images/11773.JPG')
    dummy = image.fetchImageType(type='')
    if (dummy).any():
        return 1
    return 0

def test4(*args):
    """Function to test if error handling is working for `ImagePreProcessor.__init__()`.  
        It's expected for the `__init__` function to initialize with a default image.  
        
    Returns:
      - `1` : If the error is handled as expected
      - `0` : In other case
    """
    try:
        args.initialize()
        return 0
    except Exception:
        return 1


if __name__ == '__main__':
    e1 = cv.getTickCount()

    print ("\nPlaying with file's name...")
    if test1() == 1:
        print ("Succesfull!")
    else : print ("* failure *")

    print ("\nJust changing extremely the size of the image...")
    if test2() == 1:
        print("Succesfull!")
    else: print("* failure *")

    print ("\nTrying to fetch a non-existent image type...")
    if test3() == 1:
        print("Succesfull!")
    else: print("* failure *")

    e2 = cv.getTickCount()
    time = (e2 - e1) / cv.getTickFrequency()
    print("\n\nExecution time: ", time)
