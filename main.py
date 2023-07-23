import csv 
import tkinter as tk
from hdf_gui import HealthDeclarationFormApp
from content_class import Content

if __name__ == "__main__":
    content = Content()
    Content.write_header_if_not_exists("user_info.csv")

    with open("user_info.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)

        root = tk.Tk()
        app = HealthDeclarationFormApp(root, writer)
        root.mainloop()
