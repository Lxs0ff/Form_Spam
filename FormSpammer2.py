import subprocess as sp
sp.run("pip install pynput")
from pynput.mouse import Controller,Button,Listener
import keyboard
import time

pos = []
idx = 0
count = 0
num = 1
t1 = 0
t2 = 0
delay = 0.4
_ = False

mouse = Controller()

def on_click(x, y, button, pressed):
    global pos
    if button.name == 'left' and pressed:
        pos.append(mouse.position)
        print(f"Click #{len(pos)} is now set")
    if len(pos)-pos.count("v") == num+2: 
        listener.stop()
    
def on_key_event(event):
    global _,pos
    if event.name == 'v' and keyboard.is_pressed('ctrl') and _ == False:
        _ = True
        pos.append("v")

def ctrl_release(a):
    global _
    _= False

keyboard.on_release(ctrl_release)
keyboard.hook(on_key_event)

with Listener(on_click=on_click) as listener:
    listener.join()

print("Starting in 3 seconds ...")

time.sleep(3)

t1 = time.time()
running = True          
while running:
    t2 = time.time()
    if t2-t1>=delay:
        t1 = time.time()
        if 0 < idx >= len(pos):
            idx = 0
            count+=1
            print(f"Cycle #{count}")
        if type(pos[idx]) != str:
            mouse.position = pos[idx]
            mouse.click(Button.left,1)
        else:
            keyboard.press_and_release("ctrl+v")
        idx+=1
    if keyboard.is_pressed('escape'):running=False
