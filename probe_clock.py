import ctypes
from ctypes import wintypes

user32 = ctypes.windll.user32

def find_clock():
    # 1. Shell_TrayWnd
    hwnd_tray = user32.FindWindowW("Shell_TrayWnd", None)
    print(f"Shell_TrayWnd: {hwnd_tray}")
    if not hwnd_tray: return

    # 2. TrayNotifyWnd
    hwnd_notify = user32.FindWindowExW(hwnd_tray, 0, "TrayNotifyWnd", None)
    print(f"TrayNotifyWnd: {hwnd_notify}")
    if not hwnd_notify: return

    # 3. TrayClockWClass (Standard Win10)
    hwnd_clock = user32.FindWindowExW(hwnd_notify, 0, "TrayClockWClass", None)
    print(f"TrayClockWClass: {hwnd_clock}")
    
    # 4. If not found, check secondary path (SysPager -> Toolbar? No, that's icons)
    # Windows 11 might put it elsewhere.
    
    if hwnd_clock:
        rect = wintypes.RECT()
        user32.GetWindowRect(hwnd_clock, ctypes.byref(rect))
        print(f"Clock Rect: ({rect.left}, {rect.top}) - ({rect.right}, {rect.bottom})")
    
if __name__ == "__main__":
    find_clock()
