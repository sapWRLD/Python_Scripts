import pyautogui as pag
from pynput import keyboard
import time

# Convert RGB tuple to HEX string
def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(*rgb)

# Global flag to stop listener
stop_listener = False
last_rgb = None

def on_press(key):
    global stop_listener, last_rgb
    try:
        if key == keyboard.Key.space: 
            x, y = pag.position()
            rgb = pag.pixel(x, y)  
            print(f"Captured color: {rgb} with HEX {rgb_to_hex(rgb)} at position ({x}, {y})")
            last_rgb = rgb
    except AttributeError:
        if key == keyboard.Key.esc:
            print("Exiting...")
            stop_listener = True
            return False  # Stop the listener

def get_color():
    print("Press SPACE to capture the current pixel color or ESC to exit.")
    with keyboard.Listener(on_press=on_press) as listener: 
        while not stop_listener:
            time.sleep(0.1)
        listener.join()
    return last_rgb

if __name__ == "__main__":
    rgb = get_color()
    if rgb:
        hex_value = rgb_to_hex(rgb)
        print(f"Final captured color: {rgb} with HEX value {hex_value}")
    else:
        print("No color captured.")