import tkinter as tk
from tkinter import ttk
import csv

class SearchApp:
    def __init__(self, root):
        self.__root = root
        self.__root.title("Search Entries")
        self.__set_window_position()
        self.create_widgets()

    def __set_window_position(self): 
        screen_width = self.__root.winfo_screenwidth()
        screen_height = self.__root.winfo_screenheight()

        x = int((screen_width - 600) / 2)
        y = int((screen_height - 600) / 2)

        self.__root.geometry(f"600x600+{x}+{y}")

    def create_widgets(self):
        self.search_entry_var = tk.StringVar()
        tk.Label(self.__root, text="Enter Name(in ALL CAPS) or Date/Time(MM-DD):").grid(row=0, column=0, padx=10, pady=5, sticky="w")
        search_entry = tk.Entry(self.__root, textvariable=self.search_entry_var, width=50)
        search_entry.grid(row=0, column=1, columnspan=2, padx=10, pady=5, sticky="ew")

        tk.Button(self.__root, text="Search", command=self.search_data).grid(row=1, column=0, columnspan=3, padx=10, pady=5)

def search_data(search_criteria):
    with open("user_info.csv", newline="") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)

        matching_entries = []
        for row in reader:
            if search_criteria in row[0] or search_criteria in row[-1]:
                matching_entries.append(row)

    return matching_entries

if __name__ == "__main__":
    search_criteria = input("Enter the name or date/time to search: ")
    results = search_data(search_criteria)

    if results:
        for header in ["Name", "Contact Number", "Address", "Temperature", "Destination",
                       "Vaccination Status", "Symptoms", "Exposure", "Exposure Date", "Covid-test", "Result",
                       "Date/Time"]:
            print(f"{header: <20}", end="")  
        print()  

        for row in results:
            for value in row:
                print(f"{value: <20}", end="")  
            print()  
    else:
        print("No matching entries found for the given search criteria.")
