#Kinda works (def on_run_step() is the "main" try write pgrm under "if _time == 1")
#original from TMInterface restore_state.py exemple (server name forced to server name in server_info cmd)

from tminterface.interface import TMInterface  # Import the TMInterface class
from tminterface.client import Client, run_client  # Import the Client and run_client functions
import sys  # Import the sys module
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
import win32gui
import win32con
import ctypes


class MainClient(Client):
    def __init__(self) -> None:
        self.state = None  # Initialize the state variable to None
        super(MainClient, self).__init__()  # Call the constructor of the Client class

    def on_registered(self, iface: TMInterface) -> None:
        print(f'Registered to {iface.server_name}')  # Print a message when registered to the server


    def on_run_step(self, iface: TMInterface, _time: int):

        if _time == 1000:  # If the time is 10 milliseconds
            iface.set_input_state(accelerate=True)   

            def binary(image):
                # Convert image to grayscale
                img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                # Clean up image using Guassian Blur
                img_blur = cv2.GaussianBlur(img_gray,(15,15),0)
                #cv2.imshow('blur', img_blur)
                threshold_value = 70  # (140works on testmap)adjust this value to vary the amount of black and white
                ret, binary_img = cv2.threshold(img_blur, threshold_value, 255, cv2.THRESH_BINARY)

                # Display the binary image
                #cv2.imshow('Binary Image', binary_img)
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
            point = (310,200)
            pointDroit = (350,190)
            pointGauche = (270,190)
            DotSize = 5
            DotSizeDroit = 5
            DotSizeGauche = 5
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
                pointDroitColor = color(binary_image, pointDroit)
                pointGaucheColor = color(binary_image, pointGauche)
                #print(pointcolor)
                if pointcolor == 0:
                    iface.set_input_state(accelerate=False)
                    iface.set_input_state(brake=True)
                    DotSize = 15
                    iface.set_input_state(brake=False)
                else:
                    iface.set_input_state(accelerate=True) 
                    iface.set_input_state(accelerate=True)  
                    iface.set_input_state(accelerate=True) 
                    iface.set_input_state(accelerate=True) 
                    iface.set_input_state(accelerate=True)  
                    iface.set_input_state(accelerate=True)                                                           
                    iface.set_input_state(brake=False)
                    DotSize = 5 
                    iface.set_input_state(accelerate=False) 


                if pointDroitColor == 0 and pointGaucheColor == 1:
                    iface.set_input_state(left=True)  
                    DotSizeDroit = 15                   
                if pointGaucheColor == 0 and pointDroitColor == 1:
                    iface.set_input_state(right=True)
                    DotSizeGauche = 15            
                if pointDroitColor == 1:
                    iface.set_input_state(left=False) 
                    DotSizeDroit = 5 
                if pointGaucheColor == 1:
                    iface.set_input_state(right=False)
                    DotSizeGauche = 5


                # Convert the binary image to a color image
                color_image = cv2.cvtColor(binary_image, cv2.COLOR_GRAY2BGR)

                # Draw a circle at the point to indicate it
                cv2.circle(color_image, point, DotSize, (255, 0, 0), -1)
                cv2.circle(color_image, pointDroit, DotSizeDroit, (0, 0, 255), -1)
                cv2.circle(color_image, pointGauche, DotSizeGauche, (0, 255, 0), -1)
                # Display the results in a window named "screen"
                cv2.imshow('Point color', color_image)
                
                if (cv2.waitKey(1) & 0xFF) == ord('²'):
                    cv2.destroyAllWindows()
                    break

def main():
    server_name = 'TMInterface0'  # Set the name of the TMInterface server to connect to
    print(f'Connecting to {server_name}...')  # Print a message indicating which server is being connected to
    run_client(MainClient(), server_name)  # Create a new client and connect it to the specified server


if __name__ == '__main__':
    main()  # Call the main function if this module is being run as the main program
