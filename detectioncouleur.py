# Detection de la couleur d'un point (point apparait aussi en noir et blan, mais algo fontionne)
# "# def distancemap (binary_img):" permet de dessiner un gradient de distance au changement de couleur le plus proche (regarde en 2D et non en 1D)
"""
Created on Sat Apr  8 18:56:31 2023

@author: v.galiay
"""

from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import cv2
import numpy as np
from mss import mss
from PIL import Image


def binary(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Clean up image using Guassian Blur
    img_blur = cv2.GaussianBlur(img_gray,(15,15),0)
    #cv2.imshow('blur', img_blur)
    threshold_value = 140  # adjust this value to vary the amount of black and white
    ret, binary_img = cv2.threshold(img_blur, threshold_value, 255, cv2.THRESH_BINARY)

    return binary_img

def color(image, point):
    x, y = point
    pixel_value = image[y, x]
    if pixel_value == 0:
        return 0
    else:
        return 1
    

bounding_box = {'top': 60, 'left': 100, 'width': 620, 'height': 450}
sct = mss()
point = (310,150)

while True:
    # Capture screenshot of the specified region of the screen
    sct_img = sct.grab(bounding_box)
    # Convert the screenshot to a PIL Image
    img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
    # Convert the PIL Image to a NumPy array
    img_np = np.array(img)

    # call binary function
    binary_image = binary(img_np)

    #call and print color of point
    pointcolor = color(binary_image, point)
    print(pointcolor)

    # Convert the binary image to a color image
    color_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)
    # Draw a circle at the point to indicate it
    cv2.circle(color_image, point, 5, (0, 255, 0), -1)
    # Display the results in a window named "screen"
    cv2.imshow('Point color', color_image)
    
    if (cv2.waitKey(1) & 0xFF) == ord('²'):
        cv2.destroyAllWindows()
        break



bounding_box = {'top': 60, 'left': 100, 'width': 620, 'height': 450}
sct = mss()
point = (310,150)
