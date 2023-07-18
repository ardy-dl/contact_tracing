# Requirements:
# user login, store user data, record encounters (bluetooth?? GPS??manual??), store encounters, 
# see exposures

# button for hdf
# button for check exposures
    # date
    # time
# create a form to fill out with the ff: 
import csv

class User:
    def __init__(self):
        self.__name = None
        self.__contact_no = None
        self.__address = None
        self.__temp = None
        self.__destination = None
        
    def get_user_info(self):
        self.__name = input("Enter your name: ")
        self.__contact_no = int(input("Enter your contact number: "))
        self.__address = input("Enter your current address: ")
        self.__temp = float(input("Enter your temperature: "))
        self.__destination = input("Enter your Destination: ")

    def save_info(self, writer):
        with open("user_info.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(["Name", "Contact Number", "Address", "Temperature", "Destination"])
            writer.writerow([self.__name, self.__contact_no, self.__address, self.__temp, self.__destination])

if __name__ == "__main__":
    user = User()
    user.get_user_info()
    with open("user_info.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        user.save_info(writer)
