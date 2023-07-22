import csv 
import tkinter as tk
from hdf_gui import HealthDeclarationFormApp

if __name__ == "__main__":
    with open("user_info.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)

        if csvfile.tell() == 0:
            writer.writerow(["Name", "Contact Number", "Address", "Temperature", "Destination", "Vaccination Status", "Symptoms", "Exposure", "Exposure Date", "Covid-test"])

        while True:
            print("Health Declaration Form")

            root = tk.Tk()
            app = HealthDeclarationFormApp(root, writer)
            root.mainloop()

            another_entry = input("Do you want to add another entry? (yes/no): ")
            if another_entry.lower() != "yes":
                break
