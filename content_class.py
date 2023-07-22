import csv

class Content:
    def __init__(self):
        self.__name = None
        self.__contact_no = None
        self.__address = None
        self.__temp = None
        self.__destination = None
        self.__vaccination_status = None
        self.__symptoms = {}
        self.__exposure = None
        self.__test = None
        self.__exposure_date = None

    def set_name(self, name):
        self.__name = name

    def set_contact_no(self, contact_no):
        self.__contact_no = int(contact_no)

    def set_address(self, address):
        self.__address = address

    def set_temp(self, temp):
        self.__temp = float(temp)

    def set_destination(self, destination):
        self.__destination = destination

    def set_vaccination_status(self, status):
        status_choices = ["Not Yet", "1st Dose", "2nd Dose", "1st Booster Shot", "2nd Booster Shot"]
        if status in status_choices:
            self.__vaccination_status = status
        else:
            raise ValueError("Invalid vaccination status.")

    def set_symptoms(self, symptoms):
        self.__symptoms = symptoms

    def set_exposure(self, exposure, exposure_date):
        self.__exposure = exposure.lower()
        if self.__exposure == "yes":
            self.__exposure_date = exposure_date
        elif self.__exposure == "no":
            self.__exposure_date = "N/A"
        else:
            raise ValueError("Invalid entry. Please answer yes or no only.")

    def set_covid_test(self, test, covid_test_result):
        test_choices = ["Yes", "No"]
        if test in test_choices:
            self.__test = test
            if test == "Yes":
                self.__test_result = covid_test_result
            else:
                self.__test_result = "N/A"
        else:
            raise ValueError("Invalid covid test status.")

    def save_to_csv(self, csvfile):
        writer = csv.writer(csvfile)
        writer.writerow([self.__name, self.__contact_no, self.__address, self.__temp, self.__destination,
                         self.__vaccination_status, str(self.__symptoms), self.__exposure, self.__exposure_date,
                         self.__test, self.__test_result])
        
    def to_csv_row(self):
        symptoms_str = ",".join(self.set_symptoms)
        return [self.__name, self.__contact_no, self.__address, self.__temp, self.__destination, self.__vaccination_status,
                symptoms_str, self.__exposure, self.__exposure_date, self.__test, self.__test_result]
