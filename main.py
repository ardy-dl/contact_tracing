import csv 
from app_class import User

if __name__ == "__main__":
        with open("user_info.csv", "w", newline="") as csvfile:
            writer = csv.writer(csvfile)

            if csvfile.tell() == 0:
                writer.writerow(["Name", "Contact Number", "Address", "Temperature", "Destination","Vaccination Status", "symptoms", "Exposure", "Exposure Date", "Covid-test"])

            while True:
                    print("Health Declaration Form")
                    user = User()
                    user.get_user_info()
                    user.hdf()
                    user.save_info(writer)

                    another_entry = input("Do you want to add another entry? (yes/no): ")
                    if another_entry.lower() != "yes":
                           break

        