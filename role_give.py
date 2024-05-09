import pickle
from models import Role
from core.filehandler import Editor

with Editor("db.pickle", "rb") as file:
    a = pickle.load(file)

# for user in a["User"]:
#     print(user.username)


user_name = input("username: ")
new_role = input("What would be the role of the user").title()

for user in a["User"]:
    if user.username == user_name:
        # print(user.role)
        user.role = new_role
        print("Found The User!")
        break
else:
    print("Didn't find The User! ")

# for user in a["User"]:
#     print("Printing roles")
#     print(user.role)

with Editor("db.pickle", "wb") as file:
    pickle.dump(a,file)
