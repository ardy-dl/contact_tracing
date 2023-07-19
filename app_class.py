# Requirements:
# user login, store user data, record encounters (bluetooth?? GPS??manual??), store encounters, 
# see exposures

# button for check exposures
    # date
    # time
# create a form to fill out with the ff: 
from hdf_class import Content
import csv

class User:
    def __init__(self):
        self.__name = None
        self.__contact_no = None
        self.__address = None
        self.__temp = None
        self.__destination = None
        self.__content = Content() 
        
    def get_user_info(self):
        self.__name = input("Enter your name: ")
        self.__contact_no = int(input("Enter your contact number: "))
        self.__address = input("Enter your current address: ")
        self.__temp = float(input("Enter your temperature: "))
        self.__destination = input("Enter your Destination: ")

    def hdf(self):
        self.__content.get_vaccination_status()
        self.__content.get_symptoms()
        self.__content.get_exposure()
        self.__content.get_covid_test()

    def save_info(self, writer):
        with open("user_info.csv", "a", newline="") as csvfile:
            writer = csv.writer(csvfile)
            if csvfile.tell() == 0:
                writer.writerow(["Name", "Contact Number", "Address", "Temperature", "Destination","Vaccination Status", "symptoms", "History", "Covid-test", "Exposure Date"])
            
            writer.writerow([self.__name, self.__contact_no, self.__address, self.__temp, self.__destination, self.__content._Content__vaccination_status, self.__content._Content__symptoms, "", self.__content._Content__exposure, self.__content._Content__exposure_date, self.__content._Content__test])

