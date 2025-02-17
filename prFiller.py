import keyboard
from pynput.mouse import Button, Controller
import time


mouse = Controller()

#print('The current pointer position is {0}'.format(
#    mouse.position))

print("Press Shift to fill in zeros, Alt for uploads")


while True:
    # Wait for the next event.
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN and event.name == 'shift':
        for i in range(0, 30):
            keyboard.write("100")
            keyboard.press_and_release("tab")  
    if event.event_type == keyboard.KEY_DOWN and event.name == 'alt':
        mouse.position = (508, 631)
        mouse.click(Button.left, 1)   
        #time.sleep(2)
        #mouse.position = (94, 329)
        #mouse.click(Button.left, 1)
        time.sleep(1)
        mouse.position = (778, 187)
        mouse.click(Button.left, 2)
        time.sleep(.5)
        mouse.position = (957, 785)
        mouse.click(Button.left, 1)
        time.sleep(9)
        mouse.position = (947, 529)
        mouse.click(Button.left, 1)
        time.sleep(4)
        mouse.scroll(0, -8)
    if event.event_type == keyboard.KEY_DOWN and event.name == 'esc':
        break

exit(0)
