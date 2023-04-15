# tentative de pilotage avec pyautogui, win32api, even mouse clicks to the visual keybaord...
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
import win32gui
import win32con
import ctypes

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

# def click(x,y):
#     if x != None :
                                    
#             win32api.SetCursorPos((x,y))
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#             time.sleep(0.1) 
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def press_keys(keys,x,y,timeclicked):


    for key in keys:
        if key == 'z':
            pyautogui.moveTo(x, y)  
            print ('UP')
        elif key == 'q':
            click(1016,1025)
        elif key == 's':
            click(1095,1035)
        elif key == 'd':
            click(1172,1032)






# Find the handle of the window you want to bring to the foreground
window_handle = win32gui.FindWindow(None, 'TmForever')
# Bring the window to the foreground and give it focus²²²²²²²²²²
win32gui.ShowWindow(window_handle, win32con.SW_SHOW)
# win32gui.ShowWindow(window_handle, win32con.SW_RESTORE)

hold_time = 2


while keyboard.is_pressed('²') == False:
        start = time.time()
        while time.time() - start < hold_time:
            # example usage:
            press_keys('z',1090,975,1)
            print ("z1")
           


