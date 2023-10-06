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

Treshold = 0.8

detect_Image = []
images_dir = os.path.join(os.getcwd(), "images")

for image in os.listdir(images_dir):
    if image.endswith(".png"):
        detect_Image.append(image)
        print(f"Added {image} to the list of images to detect")

print("Hold 'q' to quit, starting in 10 seconds")

time.sleep(10)

counter = 0
while True:
    for image in detect_Image:
        try:
            location = pyautogui.locateCenterOnScreen(os.path.join(images_dir, image), grayscale=True, confidence=Treshold)
            if location is None:
                print(f"{image} not found")
                continue
            x, y = location
        except TypeError:
            print(f"{image} not found")
            continue
        pyautogui.click(x, y)
        print(f"{image} found")
        if image == "again.png":
            counter += 1
            print(f"Counter = {counter}")

    if keyboard.is_pressed('q'):
        break

print(f"Forms submitted: {counter}")
print("Quitting...")