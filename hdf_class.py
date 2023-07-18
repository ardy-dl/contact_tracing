

class Content:
    def __init__(self):
        self.__symptoms = {}
        self.__exposure = ""

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
            when = input("When was your most recent visit to this location? ")
            print(when)
        elif self.__exposure == "no":
            return self.__exposure
        else:
            raise ValueError("Invalid entry. Please answer yes or no only.")
    
    def display(self):
        print("Symptoms:")
        for symptom, answer in self.__symptoms.items():
            print(symptom,":", answer)
        print

   

    #vaccination

def main():
    hdf = Content()
    hdf.get_symptoms()
    hdf.get_exposure()
    hdf.display()

if __name__ == "__main__":
    main()