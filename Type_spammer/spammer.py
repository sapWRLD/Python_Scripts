import pyautogui as pag
from pynput import keyboard
import time

text_to_spam = ""
spamming = False

def start_spamming():
    global spamming, text_to_spam
    print("spamming started")
    for i in range(20):
        if not spamming:
            break
        pag.write(text_to_spam)
        pag.press('enter')
        time.sleep(0.2)
    print("spamming stopped!")
    spamming = False    


def on_press(key):
    global spamming
    try: 
        if key == keyboard.Key.space and not spamming:
            spamming = True
            start_spamming()
        elif key == keyboard.Key.esc:
            print("Exiting..")
            spamming = False
            return False
    except Exception as e:
        print(f"error {e}")       


    time.sleep(0.05)
def main():
    global text_to_spam
    text_to_spam = input("Enter the text you want to spam: ")
    print("Press SPACE to start spamming, Esc to stop.")
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()
    
if __name__ == "__main__":
    main()