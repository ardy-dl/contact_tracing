

class Content:
    def __init__(self):
        self.__vaccination_status = None
        self.__symptoms = {}
        self.__exposure = None
        self.__test = None
        self.__exposure_date = None

    def get_vaccination_status(self):
        status = int(input("Select your vaccination status: (1,2,3,4 or 5) \n 1. Not Yet \n 2. 1st Dose \n 3. 2nd Dose(Fully vaccinated) \n 4. 1st Booster Shot \n 5. 2nd Booster Shot \n Answer: " ))
        if status in [1, 2, 3, 4, 5]:
            if status == 1:
                self.__vaccination_status = "Not Yet"
            elif status == 2:
                self.__vaccination_status = "1st Dose"
            elif status == 3:
                self.__vaccination_status = "2nd Dose"
            elif status == 4:
                self.__vaccination_status = "1st Booster Shot"
            else:
                self.__vaccination_status = "2nd Booster Shot"

    def get_symptoms(self):
        print("Are you experiencing any symptoms in the past 7 days such as: ")
        symptoms_list = ["Sore Throat", "Fever", "Cough", "Runny Nose", "Loss of Sense of Smell", "Loss of Sense of Taste", "Abdominal Pain", "Diarrhea"]
        for symptom in symptoms_list:
            while True:
                answer = input(symptom + " (yes/no) ").strip().lower()
                if answer == "yes" or answer == "no":
                    self.__symptoms[symptom] = answer
                    break
                else:
                    raise ValueError("Invalid input. Please answer yes or no only.")

    def get_exposure(self):
        self.__exposure = input("Have you had exposure to a probable or confirmed case in the last 14 days? (yes/no): ").lower()
        if self.__exposure == "yes":
            self.__exposure_date = input("When was your most recent visit to this location? ")
        elif self.__exposure == "no":
            self.__exposure_date = "N/A"
        else:
            raise ValueError("Invalid entry. Please answer yes or no only.")
        
    def get_covid_test(self):
        self.__test = input("Have you been tested for covid-19 in the last 14 days?(yes/no): ").lower()
        if self.__test == "yes":
            result = input("What is the result? ")
            self.__test = result.lower()
        else:
            self.__test = "no"
        
        
    def display(self):
        print("Symptoms:")
        for symptom, answer in self.__symptoms.items():
            print(symptom,":", answer)
        

def main():
    hdf = Content()
    hdf.get_symptoms()
    hdf.get_exposure()
    hdf.get_vaccination_status()
    hdf.covid_test()
    hdf.display()
    

if __name__ == "__main__":
    main()