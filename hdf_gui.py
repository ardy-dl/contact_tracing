import tkinter as tk
from tkinter import ttk
from app_class import User

class HealthDeclarationFormApp:
    def __init__(self, root):
        self.__root = root
        self.__root.title("Health Declaration Form")
        self.__set_window_position()
        self.content = User()
        self.create_widgets()
        
    def __set_window_position(self): 
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()

        x = int((screen_width - 600) / 2)
        y = int((screen_height - 400) / 2)

        self.__root.geometry(f"600x400+{x}+{y}")

    def create_widgets(self):
        labels = ["Name", "Contact Number", "Address", "Temperature", "Destination"]
        for i, label in enumerate(labels):
            tk.Label(self.__root, text=label + ":").grid(row=i, column=0, padx=10, pady=5, sticky="nsew")
            entry = tk.Entry(self.__root, width=50) 
            entry.grid(row=i, column=1, columnspan=2, padx=10, pady=5, sticky="ew")


        vaccination_status_choices = ["Not Yet", "1st Dose", "2nd Dose", "1st Booster Shot", "2nd Booster Shot"]
        tk.Label(self.__root, text="Vaccination Status:").grid(row=5, column=0, sticky="e")
        self.__vaccination_status_var = tk.StringVar(self.__root)
        self.__vaccination_status_var.set("Not Yet")
        self.__vaccination_status_dropdown = ttk.Combobox(self.__root, state="readonly", textvariable=self.__vaccination_status_var, values=vaccination_status_choices)
        self.__vaccination_status_dropdown.grid(row=5, column=1)


    def run(self):
        self.__root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthDeclarationFormApp(root)
    app.run()
