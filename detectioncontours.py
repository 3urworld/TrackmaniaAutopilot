#Detection de contours avec Canny (bien mais inutilisable)
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

def sketch(image):
    # Convert image to grayscale
    img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('bnw', img_gray)
    # Clean up image using Guassian Blur
    img_gray_blur = cv2.GaussianBlur(img_gray,(5,5),0)
    
    # Extract edges with canny
    canny_edges = cv2.Canny(img_gray_blur, 10, 250)
    
    # Dilate the edges to close gaps
    kernel = np.ones((3,3),np.uint8)
    dilated_edges = cv2.dilate(canny_edges, kernel, iterations=1)

    return dilated_edges

bounding_box = {'top': 100, 'left': 0, 'width': 400, 'height': 300}
sct = mss()

while True:
    # Capture screenshot of the specified region of the screen
    sct_img = sct.grab(bounding_box)
    # Convert the screenshot to a PIL Image
    img = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')
    # Convert the PIL Image to a NumPy array
    img_np = np.array(img)
    # Apply edge detection to the captured image
    edges = sketch(img_np)
    # Find contours of the edges
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Draw the contours on the original image
    cv2.drawContours(img_np, contours, -1, (0, 255, 0), 3)
    # Display the results in a window named "screen"
    cv2.imshow('screen', img_np)
    
    if (cv2.waitKey(1) & 0xFF) == ord('²'):
        cv2.destroyAllWindows()
        break
