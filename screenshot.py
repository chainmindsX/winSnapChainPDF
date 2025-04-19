# screenshot.py
import pyautogui
import os
from datetime import datetime

screenshot_folder = "screenshots"
os.makedirs(screenshot_folder, exist_ok=True)

def take_screenshot():
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(screenshot_folder, f"{timestamp}.png")
    screenshot = pyautogui.screenshot()
    screenshot.save(filepath)
    print(f"[+] Screenshot taken: {filepath}")
