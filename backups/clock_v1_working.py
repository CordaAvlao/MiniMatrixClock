import tkinter as tk
from time import strftime
from PIL import ImageGrab
import platform

class MiniClock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mini Matrix Clock")
        
        # Remove window decorations (frameless)
        self.root.overrideredirect(True)
        
        # Keep window always on top
        self.root.attributes('-topmost', True)
        
        # Initial configuration
        self.font = ("Consolas", 12, "bold")
        self.text_color = "#00FF00"  # Matrix Green
        
        self.label = tk.Label(
            self.root, 
            font=self.font, 
            fg=self.text_color, 
            bd=0, 
            padx=10,  # Increased internal padding
            pady=2
        )
        self.label.pack()
        
        # Setup close event
        self.label.bind("<Double-Button-1>", lambda e: self.root.quit())
        
        # Setup drag events
        self.label.bind("<Button-1>", self.start_move)
        self.label.bind("<B1-Motion>", self.do_move)
        self.label.bind("<ButtonRelease-1>", self.stop_move)
        
        self.x = 0
        self.y = 0

        # Initial setup: update events to ensure we have geometry
        self.root.update()
        self.update_position_and_color()
        self.update_clock()
        
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
        # Update background color based on new position
        self.refresh_background()

    def refresh_background(self):
        try:
            x = self.root.winfo_x()
            y = self.root.winfo_y()
            width = self.label.winfo_reqwidth()
            height = self.label.winfo_reqheight()
            
            # Sample center of the clock window
            # Clamp to screen bounds
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            
            sample_x = max(0, min(x + width//2, screen_width - 1))
            sample_y = max(0, min(y + height//2, screen_height - 1))
            
            # Temporarily hide window to grab what's behind it
            self.root.withdraw()
            self.root.update() # Force update to ensure it's hidden
            
            bg_color = self.get_taskbar_color(sample_x, sample_y)
            
            # Show window again
            self.root.deiconify()
            self.root.update()
            
            self.root.configure(bg=bg_color)
            self.label.configure(bg=bg_color)
        except Exception as e:
            print(f"Error refreshing background: {e}")
            self.root.deiconify() # Ensure we come back if error

    def get_taskbar_color(self, x, y):
        try:
            # Capture a 1x1 pixel image at the specified coordinates
            image = ImageGrab.grab(bbox=(x, y, x+1, y+1))
            color = image.getpixel((0, 0))
            # Convert RGB to Hex
            return '#{:02x}{:02x}{:02x}'.format(*color)
        except Exception as e:
            print(f"Error grabbing color: {e}")
            return "black" # Fallback

    def update_position_and_color(self):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Update pending geometry to get correct size
        self.root.update_idletasks() # Ensure label has calculated its size
        
        # Get requested size but add a significant safety margin
        width = self.label.winfo_reqwidth() + 60 # +60px safety buffer (Huge margin)
        height = self.label.winfo_reqheight()
        
        # Position: SAFE INITIAL POSITION
        # 120px from right, 80px from bottom.
        x = screen_width - 180 
        y = screen_height - 80
        
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        # We need to manually call this because the window isn't logically "drawn" yet for withdrawal to matter
        # But actually update_position is called after init update() so it should work.
        self.refresh_background()
        
    def update_clock(self):
        # Remove seconds as requested
        current_time = strftime('%H:%M')
        self.label.config(text=current_time)
        
        # Re-assert always on top every second and lift to top of stack
        self.root.attributes('-topmost', True)
        self.root.lift()
        
        self.root.after(1000, self.update_clock)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MiniClock()
    app.run()
