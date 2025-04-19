# listener.py
from pynput import keyboard
from screenshot import take_screenshot

def on_press(key):
    if key == keyboard.Key.ctrl_r:
        take_screenshot()

def start_listener():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    print("[*] Listening for Right Ctrl key...")
