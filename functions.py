import csv 

from app_class import User

if __name__ == "__main__":
    user = User()
    user.get_user_info()
    with open("user_info.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        user.save_info(writer)