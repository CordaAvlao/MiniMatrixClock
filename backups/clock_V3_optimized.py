import tkinter as tk
import winreg
from tkinter import colorchooser
from time import strftime
from PIL import ImageGrab
import platform
import json
import os
import sys
import ctypes
from ctypes import wintypes
import time

class MiniClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mini Matrix Clock")
        
        # Remove window decorations (frameless)
        self.root.overrideredirect(True)
        
        # Keep window always on top
        self.root.attributes('-topmost', True)
        
        # Configuration
        if getattr(sys, 'frozen', False):
            self.app_path = os.path.dirname(sys.executable)
        else:
            self.app_path = os.path.dirname(os.path.abspath(__file__))
        self.config_file = os.path.join(self.app_path, "config.json")
        
        # State Variables
        self.startup_var = tk.BooleanVar(value=self.check_startup_status())
        self.persist_var = tk.BooleanVar(value=self.check_persistence_status())
        
        self.font = ("Consolas", 12, "bold")
        self.text_color = "#00FF00"  # Matrix Green
        
        self.normal_bg = "black"     # Store the sampled color
        self.transparent_key = "#000001" # Almost black, used for transparency
        
        # Configure transparency key
        self.root.wm_attributes("-transparentcolor", self.transparent_key)
        
        self.label = tk.Label(
            self.root, 
            font=self.font, 
            fg=self.text_color, 
            bd=0, 
            padx=10, 
            pady=0 
        )
        self.label.pack()
        
        # Setup Context Menu (Right Click)
        self.menu = tk.Menu(self.root, tearoff=0)
        
        # Options Submenu
        self.options_menu = tk.Menu(self.menu, tearoff=0)
        self.options_menu.add_checkbutton(label="Run on Startup", onvalue=True, offvalue=False, variable=self.startup_var, command=self.toggle_startup)
        self.options_menu.add_checkbutton(label="Remember Position", onvalue=True, offvalue=False, variable=self.persist_var, command=self.toggle_persistence)
        
        # Color Submenu
        self.color_menu = tk.Menu(self.options_menu, tearoff=0)
        self.color_menu.add_command(label="Matrix Green", command=lambda: self.change_color("#00FF00"))
        self.color_menu.add_command(label="Cyber Blue", command=lambda: self.change_color("#00FFFF"))
        self.color_menu.add_command(label="Red Alert", command=lambda: self.change_color("#FF0000"))
        self.color_menu.add_command(label="Retro Amber", command=lambda: self.change_color("#FFBF00"))
        self.color_menu.add_command(label="Pure White", command=lambda: self.change_color("#FFFFFF"))
        self.color_menu.add_separator()
        self.color_menu.add_command(label="Custom...", command=self.choose_custom_color)
        
        self.options_menu.add_cascade(label="Text Color", menu=self.color_menu)
        
        self.menu.add_cascade(label="Options", menu=self.options_menu)
        self.menu.add_separator()
        self.menu.add_command(label="Snooze 10m", command=self.snooze)
        self.menu.add_separator()
        self.menu.add_command(label="My GitHub", command=self.open_github)
        self.menu.add_command(label="About", command=self.show_about)
        self.menu.add_separator()
        self.menu.add_command(label="Exit", command=self.root.quit)
        
        self.label.bind("<Button-3>", self.show_menu)
        
        # Setup drag events
        self.label.bind("<Button-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.do_move)
        self.label.bind("<ButtonRelease-1>", self.stop_move)
        
        self.x = 0
        self.y = 0
        self.menu_open = False # Flag to track menu state

        # Initial setup
        self.root.update() 
        
        if not self.load_config():
            self.auto_detect_position()
        else:
            # Check if off-screen (sanity check)
            if self.is_off_screen():
                 self.auto_detect_position()
            else:
                 self.root.after(200, self.refresh_background)
            
        self.update_clock()
        self.check_fullscreen()

    def show_menu(self, event):
        try:
            self.menu_open = True # Pause topmost re-assertion
            # Offset y to ensure menu opens ABOVE the mouse (approx 10px up)
            # This prevents it from being cut off by the taskbar
            self.menu.tk_popup(event.x_root, event.y_root - 10)
        finally:
            self.menu.grab_release()
            self.menu_open = False # Resume topmost re-assertion

    def open_github(self):
        import webbrowser
        webbrowser.open("https://github.com/CordaAvlao")

    def show_about(self):
        from tkinter import messagebox
        messagebox.showinfo(
            "About", 
            "MiniClock v2.2\n\n"
            "Made by CordaAvlao\n"
            "12/12/2025"
        )

    def is_off_screen(self):
        # Basic check to ensure window is visible
        x = self.root.winfo_x()
        y = self.root.winfo_y()
        screen_w = self.root.winfo_screenwidth()
        screen_h = self.root.winfo_screenheight()
        return (x > screen_w or y > screen_h or x < -100 or y < -100)

    def check_fullscreen(self):
        try:
            user32 = ctypes.windll.user32
            
            # Get Active Window
            hWnd = user32.GetForegroundWindow()
            
            # Get Screen Size (Primary)
            # Note: This is imperfect for multi-mon, but we refine with Monitor check below
            screen_w = user32.GetSystemMetrics(0)
            screen_h = user32.GetSystemMetrics(1)
            
            if hWnd:
                rect = wintypes.RECT()
                user32.GetWindowRect(hWnd, ctypes.byref(rect))
                win_w = rect.right - rect.left
                win_h = rect.bottom - rect.top
                
                # 1. Size Check: Is it "Big"?
                is_large = (win_w >= screen_w and win_h >= screen_h)
                
                # 2. Monitor Check: Is it on the SAME screen as us?
                # MONITOR_DEFAULTTONEAREST = 2
                clock_hwnd = self.root.winfo_id()
                monitor_clock = user32.MonitorFromWindow(clock_hwnd, 2)
                monitor_app = user32.MonitorFromWindow(hWnd, 2)
                
                # Logic: Be transparent ONLY if:
                # - The active window is large (Fullscreen-ish)
                # - AND it is on the same monitor as the clock
                if is_large and (monitor_clock == monitor_app):
                    self.set_transparent_mode(True)
                else:
                    self.set_transparent_mode(False)
                    
        except Exception:
            pass
            
        # Check every 1 second
        self.root.after(1000, self.check_fullscreen)

    def set_transparent_mode(self, enabled):
        target_bg = self.transparent_key if enabled else self.normal_bg
        
        # Only update if changed to avoid flickering
        current_bg = self.label.cget("bg")
        if current_bg != target_bg:
            self.root.configure(bg=target_bg)
            self.label.configure(bg=target_bg)

    def load_config(self):
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    data = json.load(f)
                    x, y = data.get('x'), data.get('y')
                    saved_color = data.get('color')
                    
                    if saved_color:
                        self.change_color(saved_color, save=False)
                        
                    if x is not None and y is not None:
                        width = self.label.winfo_reqwidth() + 60
                        height = self.label.winfo_reqheight()
                        self.root.geometry(f'{width}x{height}+{x}+{y}')
                        # Ensure we force an update so winfo_x/y are correct immediately
                        self.root.update()
                        return True
            except Exception as e:
                print(f"Failed to load config: {e}")
        return False

    def save_config(self):
        if not self.persist_var.get():
            return
            
        try:
            data = {
                'x': self.root.winfo_x(),
                'y': self.root.winfo_y(),
                'color': self.text_color
            }
            with open(self.config_file, 'w') as f:
                json.dump(data, f)
        except Exception as e:
            print(f"Failed to save config: {e}")

    def auto_detect_position(self):
        # Fallback to Taskbar Geometry (Robust Logic)
        print("Using Taskbar Geometry fallback...")
        rect = self.get_taskbar_rect()
        
        # Restore the HUGE safety margin that worked in V1
        width = self.label.winfo_reqwidth() + 60
        height = self.label.winfo_reqheight()

        if rect:
            tb_left, tb_top, tb_width, tb_height = rect
            
            # Position at the far right of the taskbar
            final_x = (tb_left + tb_width) - width - 20
            
            # Center vertically relative to taskbar
            final_y = tb_top + (tb_height - height) // 2
            
            # Ensure it doesn't go off-screen at the bottom
            screen_height = self.root.winfo_screenheight()
            if final_y + height > screen_height:
                final_y = screen_height - height
            
            self.root.geometry(f'{width}x{height}+{final_x}+{final_y}')
        else:
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            x = screen_width - 250 
            y = screen_height - 100
            self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # Save this detected position immediately so it persists
        self.root.update()
        self.save_config()
        
        # Defer background refresh slightly 
        self.root.after(200, self.refresh_background)

    def get_taskbar_rect(self):
        try:
            user32 = ctypes.windll.user32
            hWnd_taskbar = user32.FindWindowW("Shell_TrayWnd", None)
            if hWnd_taskbar:
                rect = wintypes.RECT()
                user32.GetWindowRect(hWnd_taskbar, ctypes.byref(rect))
                return (rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top)
        except Exception:
            pass
        return None

    def start_move(self, event):
        self.x = event.x
        self.y = event.y

    def do_move(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.root.winfo_x() + deltax
        y = self.root.winfo_y() + deltay
        self.root.geometry(f"+{x}+{y}")
        
    def stop_move(self, event):
        self.refresh_background()
        self.save_config() # Auto-save on move

    def refresh_background(self):
        try:
            x = self.root.winfo_x()
            y = self.root.winfo_y()
            width = self.label.winfo_reqwidth()
            height = self.label.winfo_reqheight()
            
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            
            # SMART SAMPLING:
            # Instead of sampling the center (where the mouse is triggering hover effects),
            # Sample 10px to the LEFT of the window.
            # This lands on the static taskbar area, avoiding the "Highlight" color of the system clock.
            sample_x = max(0, x - 10)
            
            # Keep Y centered
            sample_y = max(0, min(y + height//2, screen_height - 1))
            
            self.root.withdraw()
            self.root.update()
            
            # Increased delay to capture clean background (Fixes "Thumbnail" look)
            import time
            time.sleep(0.2)
            
            bg_color = self.get_taskbar_color(sample_x, sample_y)
            
            # Avoid accidentally picking the transparent key
            if bg_color == self.transparent_key:
                bg_color = "#000000"
            
            self.normal_bg = bg_color 
            
            self.root.deiconify()
            self.root.update()
            
            self.root.configure(bg=bg_color)
            self.label.configure(bg=bg_color)
        except Exception as e:
            print(f"Error refreshing background: {e}")
            self.root.deiconify()

    def get_taskbar_color(self, x, y):
        try:
            image = ImageGrab.grab(bbox=(x, y, x+1, y+1))
            color = image.getpixel((0, 0))
            return '#{:02x}{:02x}{:02x}'.format(*color)
        except Exception:
            return "black"

    def update_clock(self):
        current_time = strftime('%H:%M')
        if self.label.cget("text") != current_time:
             self.label.config(text=current_time)
        
        # Only assert topmost if menu is NOT open
        # This prevents the clock from popping over the context menu
        if not self.menu_open:
            self.root.attributes('-topmost', True)
            self.root.lift()
            
        self.root.after(50, self.update_clock)

    def run(self):
        self.root.mainloop()

    # --- Helper Feature Methods ---

    def check_persistence_status(self):
        # Default to True
        return True

    def toggle_persistence(self):
        # The variable self.persist_var handles the UI state.
        # Logic uses self.persist_var.get() in save_config
        pass

    def check_startup_status(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_READ)
            winreg.QueryValueEx(key, "MiniClock")
            winreg.CloseKey(key)
            return True
        except WindowsError:
            return False

    def toggle_startup(self):
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        app_name = "MiniClock"
        
        if self.startup_var.get():
            # Enable Startup: Add to Registry
            try:
                import sys
                exe_path = sys.executable if getattr(sys, 'frozen', False) else os.path.abspath(__file__)
                
                target = exe_path
                if not getattr(sys, 'frozen', False):
                    # Script mode: "pythonw.exe" "script.py"
                    python_exe = sys.executable.replace("python.exe", "pythonw.exe")
                    target = f'"{python_exe}" "{os.path.abspath(__file__)}"'
                else:
                    target = f'"{target}"' # Quote path for safety
                    
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
                winreg.SetValueEx(key, app_name, 0, winreg.REG_SZ, target)
                winreg.CloseKey(key)
                print("Registry Startup enabled.")
                
            except Exception as e:
                print(f"Failed to set registry key: {e}")
                self.startup_var.set(False) # Revert UI
        else:
            # Disable Startup: Delete from Registry
            try:
                key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
                winreg.DeleteValue(key, app_name)
                winreg.CloseKey(key)
                print("Registry Startup disabled.")
            except Exception as e:
                print(f"Failed to remove registry key: {e}")

    def snooze(self):
        # Hide window
        self.root.withdraw()
        # Schedule reappearance after 10 minutes (600,000 ms)
        self.root.after(600000, self.wake_up)
        
    def wake_up(self):
        self.root.deiconify()
        self.refresh_background()

    def change_color(self, color, save=True):
        self.text_color = color
        self.label.config(fg=self.text_color)
        if save:
            self.save_config()

    def choose_custom_color(self):
        try:
            # Hide temporarily to show dialog
            # self.root.withdraw() # Optional: keep visible to see effect
            color = colorchooser.askcolor(color=self.text_color, title="Choose Clock Color")
            # self.root.deiconify()
            
            if color[1]: # If a color was chosen (not None)
                self.change_color(color[1])
        except Exception as e:
            print(f"Color chooser failed: {e}")

if __name__ == "__main__":
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(1)
    except Exception:
        pass 
        
    app = MiniClock()
    app.run()
