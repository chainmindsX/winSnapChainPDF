# shutdown_handler.py
import win32con
import win32api
import win32gui
from pdf_generator import create_pdf_from_screenshots

PBT_APMSUSPEND = 0x0004
WM_POWERBROADCAST = 0x218
WM_QUERYENDSESSION = 0x11

def shutdown_handler(hwnd, msg, wparam, lparam):
    if msg == WM_QUERYENDSESSION:
        print("[!] Shutdown detected. Creating PDF...")
        create_pdf_from_screenshots()
    elif msg == WM_POWERBROADCAST and wparam == PBT_APMSUSPEND:
        print("[!] Sleep detected. Creating PDF...")
        create_pdf_from_screenshots()
    return True

def start_shutdown_listener():
    wc = win32gui.WNDCLASS()
    hinst = wc.hInstance = win32api.GetModuleHandle(None)
    wc.lpszClassName = "ShutdownHandlerWindow"
    wc.lpfnWndProc = shutdown_handler

    class_atom = win32gui.RegisterClass(wc)
    hwnd = win32gui.CreateWindow(wc.lpszClassName, "HiddenWindow", 0, 0, 0, 0, 0, 0, 0, hinst, None)

    print("[*] Listening for shutdown and sleep events...")
    win32gui.PumpMessages()
