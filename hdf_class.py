

class Content:
    def __init__(self):
        self.__symptoms = []

    def get_symptoms(self):
        print("Do you have any of the following: (yes/no)")
        symptoms_list = ["Sore Throat", "Fever", "Cough", "Runny Nose", "Loss of Sense of Smell", "Loss of Sense of Taste", "Abdominal Pain", "Diarrhea"]
        for i in symptoms_list:
            while True:
                answer = input(i).lower
                if answer == "yes" or answer == "no":
                    self.__symptoms[i] = answer

    def display(self):
        print("Symptoms:")
        for i, answer in self.__symptoms.items():
            print("{i} : {answer}")

hdf = Content
hdf.get_symptoms()
hdf.display()
