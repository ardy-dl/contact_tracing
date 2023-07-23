import tkinter as tk
from tkinter import ttk
import csv
from hdf_gui import HealthDeclarationFormApp
from content_class import Content

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Main Window")
    
    def open_hdf_form():
        content = Content()
        Content.write_header_if_not_exists("user_info.csv")

        with open("user_info.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)

        hdf_form_window = tk.Toplevel()
        hdf_form_app = HealthDeclarationFormApp(hdf_form_window, writer)  
        hdf_form_app.run()      
        root.mainloop()

    fill_up_hdf_button = ttk.Button(root, text="Fill up hdf", command=open_hdf_form)
    fill_up_hdf_button.pack(pady=10)

root.mainloop()
