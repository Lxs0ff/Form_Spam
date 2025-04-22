import os
import sys
import time

def checkInstalled(library):
    try:
        __import__(library)
        print(f"{library} is installed")
    except ImportError:
        print(f"{library} is not installed")
        print(f"Installing {library}...")
        os.system(f'cmd /c "pip install {library}"')
        print(f"{library} has been installed")
checkInstalled("keyboard")
import keyboard
checkInstalled("opencv-python")
import cv2
checkInstalled("pyautogui")
import pyautogui
checkInstalled("numpy")
import numpy as np
checkInstalled("pyscreeze")
import pyscreeze
import pyautogui

Treshold = 0.9

detect_Image = []
found = []
images_dir = os.path.join(os.getcwd(), "images")

for image in os.listdir(images_dir):
    if image.endswith(".png"):
        detect_Image.append(image)
        print(f"Added {image} to the list of images to detect")


time.sleep(10)

cpos = pyautogui.position()

print("Hold 'q' to quit, starting in 10 seconds")

time.sleep(10)

click_count = 0
counter = 0
while True:
    if counter  == 27: exit()
    for image in detect_Image:
        try:
            location = pyautogui.locateCenterOnScreen(os.path.join(images_dir, image), grayscale=True, confidence=Treshold)
            if location is None:
                print(f"{image} not found")
                continue
            x, y = location
        except:
            print(f"{image} not found")
            continue
        if click_count < 7 and image not in found:
            found.append(image)
            pyautogui.click(x, y)
            print(f"{image} found")
        elif click_count == 7:
            pyautogui.click(cpos)
        if image == "again.png":
            found = []
            counter += 1
            print(f"Counter = {counter}")

    if keyboard.is_pressed('q'):
        break

print(f"Forms submitted: {counter}")
print("Quitting...")