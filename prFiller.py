import keyboard
from pynput import mouse

def on_click(x, y, button, pressed):
    if pressed:  # Detects when a click happens
        print(f"Mouse clicked at ({x}, {y})")
        return False  # Stops listening after one click

print("Waiting for a mouse click...")
with mouse.Listener(on_click=on_click) as listener:
    listener.join()

print("Mouse clicked! Proceeding...")

for i in range(0, 30):
    keyboard.write("100")
    keyboard.press_and_release("tab")
    
