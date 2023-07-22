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

        symptoms_list = ["Sore Throat", "Fever", "Cough", "Runny Nose", "Loss of Sense of Smell", "Loss of Sense of Taste", "Abdominal Pain", "Diarrhea", "None of the Above"]
        self.__symptoms_vars = {symptom: tk.BooleanVar() for symptom in symptoms_list}
        tk.Label(self.__root, text="Are you experiencing any symptoms in the past 7 days such as:").grid(row=6, column=1, sticky="e")
        for idx, symptom in enumerate(symptoms_list):
            tk.Checkbutton(self.__root, text=symptom, variable=self.__symptoms_vars[symptom]).grid(row=7+idx, column=1, sticky="w") 

        tk.Label(self.__root, text="Do you have any exposure to a probable or confirmed covid case:").grid(row=7+len(symptoms_list), column=1, sticky="e")
        self.__exposure_var = tk.StringVar(self.__root)
        self.__exposure_var.set("No")
        exposure_choices = ["Yes", "No"]
        self.__exposure_dropdown = ttk.Combobox(self.__root, state="readonly", textvariable=self.__exposure_var, values=exposure_choices)
        self.__exposure_dropdown.grid(row=8+len(symptoms_list), column=1)

        self.__exposure_date_label = tk.Label(self.__root, text="Exposure Date:")
        self.__exposure_date_entry = tk.Entry(self.__root, state="disabled")
        self.__exposure_date_label.grid(row=9+len(symptoms_list), column=0, sticky="e")
        self.__exposure_date_entry.grid(row=9+len(symptoms_list), column=1)

        self.__exposure_dropdown.bind("<<ComboboxSelected>>", self.toggle_exposure_date)

        self.__covid_test_var = tk.StringVar(self.__root)
        self.__covid_test_var.set("No")
        covid_test_choices = ["Yes", "No"]
        self.__covid_test_dropdown = ttk.Combobox(self.__root, textvariable=self.__covid_test_var, values=covid_test_choices)
        self.__covid_test_dropdown.grid(row=10+len(symptoms_list), column=1)

        self.__covid_test_result_label = tk.Label(self.__root, text="Covid Test Result:")
        self.__covid_test_result_entry = tk.Entry(self.__root, state="disabled")
        self.__covid_test_result_label.grid(row=11+len(symptoms_list), column=0, sticky="e")
        self.__covid_test_result_entry.grid(row=11+len(symptoms_list), column=1)

        self.__covid_test_dropdown.bind("<<ComboboxSelected>>", self.toggle_covid_test_result)

    def toggle_exposure_date(self, event):
        if self.__exposure_var.get() == "Yes":
            self.__exposure_date_entry.config(state="normal")
        else:
            self.__exposure_date_entry.delete(0, tk.END)
            self.__exposure_date_entry.config(state="disabled")

    def toggle_covid_test_result(self, event):
        if self.__covid_test_var.get() == "Yes":
            self.__covid_test_result_entry.config(state="normal")
        else:
            self.__covid_test_result_entry.delete(0, tk.END)
            self.__covid_test_result_entry.config(state="disabled")

    


    def run(self):
        self.__root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = HealthDeclarationFormApp(root)
    app.run()
