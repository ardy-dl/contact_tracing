# Requirements:
# user login, store user data, record encounters (bluetooth?? GPS??manual??), store encounters, 
# see exposures

# button for hdf
# button for check exposures
    # date
    # time
# create a form to fill out with the ff: 
class User:
    def __init__(self):
        self.__name = None
        self.__contact_no = None
        
    def get_user_info(self):
        self.__name = input("Enter your name: ")
        self.__contact_no = int(input("Enter your contact number: "))

    def save_info(self, writer):
        with open("user_info.csv", "w") as csvfile:
            writer = csv.writer(csvfile)

            writer.writerow(["Name", "Contact Number"])
            writer.writerow([self.__name, self.__contact_no])

if __name__ == "__main__":
    user = User()
    user.get_user_info()
    user.save_info()
