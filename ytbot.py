# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 22:51:41 2020

@author: v.galiay
"""


from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(1)
print("version 1.2 - 05/12/2020 \n\nOk donc cet app 'ytbot.exe' va cliquer sur 'passer les annonces' ou sur les pubs popup de yt quand tu la lance, une fenetre noire s'ouvre si tu la fermes ça quitte l'app. \nAutre moyen de quitter l'app, la touche '²' en haut a gauche du clavier. \n\nSI JAMAIS L'ORDI SE MET A CLIQUER PARTOUT APPUYER SUR '²' \n\nVictor\n")

def click(buttonLocation):
    if buttonLocation != None :
            x, y = pyautogui.center(buttonLocation)
        
            print("Détruite !\n")            
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            time.sleep(0.1) 
    
while keyboard.is_pressed('²') == False:
    
    if pyautogui.locateOnScreen('passerLesAnnonces.png', region=(850,750,1080,350), grayscale=True, confidence=0.9) != None:
        buttonLocation = pyautogui.locateOnScreen('passerLesAnnonces.png', region=(850,750,1080,350), grayscale=True, confidence=0.9)
        print("Double pub ...") 
        click(buttonLocation)
    if pyautogui.locateOnScreen('anonce.png', region=(850,750,1080,350), grayscale=True, confidence=0.9) != None:
        buttonLocation = pyautogui.locateOnScreen('anonce.png', region=(850,750,1080,350), grayscale=True, confidence=0.9)
        print("Simple pub ...") 
        click(buttonLocation)
    if pyautogui.locateOnScreen('passer.png', region=(850,750,1080,350), grayscale=True, confidence=0.9) != None:
        buttonLocation = pyautogui.locateOnScreen('passer.png', region=(850,750,1080,350), grayscale=True, confidence=0.9)
        print("Pub ...") 
        click(buttonLocation)
    if pyautogui.locateOnScreen('croixb.png', region=(850,750,1080,350), grayscale=True, confidence=0.9) != None:
        buttonLocation = pyautogui.locateOnScreen('croixb.png', region=(850,750,1080,350), grayscale=True, confidence=0.9)
        print("Popup noir ...") 
        click(buttonLocation)
    if pyautogui.locateOnScreen('croix.png', region=(850,750,1080,350), grayscale=True, confidence=0.9) != None:
        buttonLocation = pyautogui.locateOnScreen('croix.png', region=(850,750,1080,350), grayscale=True, confidence=0.9)
        print("Popup blanc ...") 
        click(buttonLocation)        
            
    # else:
    #     print("I am unable to see it")
    #     time.sleep(0.1)