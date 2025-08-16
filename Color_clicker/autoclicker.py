import pyautogui as pag
from pynput import keyboard
import time

target_color = None
running = True

def on_press(key):
    global target_color, running
    try:
        if key == keyboard.Key.space:
            x, y = pag.position()
            target_color = pag.pixel(x, y)
            print(f"Target color set to: {target_color}")
        elif key == keyboard.Key.esc:
            running = False
            return False  # stop listener
    except Exception as e:
        print(f"Error: {e}")

def shoot():
    global target_color
    if target_color is None:
        return
    x, y = pag.position()
    if pag.pixel(x, y) == target_color:
        pag.click()
        print(f"Shooting at color: {target_color}")
        time.sleep(0.1)

def main():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    while running:
        shoot()
        time.sleep(0.05)

if __name__ == "__main__":
    main()
 