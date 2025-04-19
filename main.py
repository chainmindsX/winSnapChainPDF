# main.py
from listener import start_listener
from shutdown_handler import start_shutdown_listener
import threading

if __name__ == "__main__":
    start_listener()
    shutdown_thread = threading.Thread(target=start_shutdown_listener)
    shutdown_thread.start()
