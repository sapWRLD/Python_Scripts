import speech_recognition as sr
from pynput import keyboard
import pyaudio
import time
from datetime import datetime

# Start de spraakherkenner en microfoon
recognizer = sr.Recognizer()
mic = sr.Microphone()


stop_listening = None
def on_press(key):
        global stop_listening  
        if key == keyboard.Key.space:
            if stop_listening is None:
                print("spraakherkening gestart. Druk op Esc om te stoppen.")
                with mic as source:
                    recognizer.adjust_for_ambient_noise(source)
                stop_listening = recognizer.listen_in_background(mic, callback)
            else:
                print("Spaakherkenning draait al.")       
        elif key == keyboard.Key.esc:
            if stop_listening is not None:
                stop_listening(wait_for_stop=False)  # Stop background listening
                print("Spraakherkenning gestopt. Programma sluit af.")
            else:
                print("Spraakherkenning was niet actief.")
            return False  # Stop listener
# Callback-functie die automatisch wordt aangeroepen wanneer er spraak wordt gedetecteerd
def callback(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language='nl-NL')
        print(f"Je zei: {text}.")

        with open("speech_log.txt", "a", encoding="utf-8") as log_file:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
            log_file.write(f"{timestamp} - {text}.\n")
    except sr.UnknownValueError:
        print("Sorry, ik kon de audio niet begrijpen.")
    except sr.RequestError as e:
        print(f"Kan geen resultaat aanvragen; {e}")

        
def main():
    print("Druk op SPATIE om spraakherkenning te starten. Druk op ESC om te stoppen.")
    listerner = keyboard.Listener(on_press=on_press)
    listerner.start()
    listerner.join()
if __name__ == "__main__":
    main()
            