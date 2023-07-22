import tkinter as tk
from tkinter import ttk
from app_class import User

class HealthDeclarationFormApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Health Declaration Form")
        self.set_window_position()
        self.content = User()

    def set_window_position(self):
        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Calculate the x and y position for the window to be centered
        x = int((screen_width - 100) / 2)
        y = int((screen_height - 600) / 2)

        # Set the window's geometry to center it on the screen
        self.root.geometry(f"100x600+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthDeclarationFormApp(root)
    root.mainloop()
