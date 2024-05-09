import pickle

with open("db.pickle", "rb") as file:
    a = pickle.load(file)

print(a)
for user in a["User"]:
    print(user.role)
