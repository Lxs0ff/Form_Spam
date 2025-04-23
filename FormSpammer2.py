import subprocess as sp
sp.run("pip install pynput")
from pynput.mouse import Controller,Button,Listener
import keyboard
import time

pos = []
idx = 0
count = 0
num = 4
t1 = 0
t2 = 0
delay = 0.4

mouse = Controller()

def on_click(x, y, button, pressed):
    global pos
    if button.name == 'left' and pressed:
        pos.append(mouse.position)
        print(f"Click #{len(pos)} is now set")
    if len(pos) == num+2: 
        listener.stop()

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
        try:
            mouse.position = pos[idx]
        except:
            idx = 0
            count+=1
            mouse.position = pos[idx]
            print(f"Cycle #{count}")
        mouse.click(Button.left,1)
        idx+=1
    if keyboard.is_pressed('escape'):running=False
