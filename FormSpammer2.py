import subprocess as sp
sp.run("pip install pynput")
from pynput.mouse import Controller,Button,Listener
import pynput
import time

pos = []
idx = 0
count = 0
num = 4

mouse = Controller()

time.sleep(1)

def on_click(x, y, button, pressed):
    global pos
    if button.name == 'left' and pressed:
        pos.append(mouse.position)
    if len(pos) == 9: 
        listener.stop()

with Listener(on_click=on_click) as listener:
    listener.join()

time.sleep(3)


while count < num+2:
    mouse.position = pos[idx]
    mouse.click(Button.left,1)
    idx+=1
    if idx > len(pos) - 1 : idx = 0;count+=1;
    if pynput.keyboard.Controller.pressed(pynput.keyboard.Key.tab):exit()
