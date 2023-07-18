

class Content:
    def __init__(self):
        self.__symptoms = {}

    def get_symptoms(self):
        print("Do you have any of the following: (yes/no)")
        symptoms_list = ["Sore Throat ", "Fever ", "Cough ", "Runny Nose ", "Loss of Sense of Smell ", "Loss of Sense of Taste ", "Abdominal Pain ", "Diarrhea "]
        for symptom in symptoms_list:
            while True:
                answer = input(symptom).lower()
                if answer == "yes" or answer == "no":
                    self.__symptoms[symptom] = answer
                    break

    def display(self):
        print("Symptoms:")
        for symptom, answer in self.__symptoms.items():
            print(symptom,":", answer)

def main():
    hdf = Content()
    hdf.get_symptoms()
    hdf.display()

if __name__ == "__main__":
    main()