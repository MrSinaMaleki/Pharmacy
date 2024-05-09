from models import Drug
from models import User
from core.filehandler import Editor


def add_drug(route):
    name = input('enter drug name: ')
    number = int(input('enter drug number: '))
    takeble = input("Is it takebale? (y/n)")
    Drug(name, number, True if takeble.lower() == "y" else False)


def list_drug(route):
    for counter, drug in enumerate(Drug.store, start=1):
        print(drug, end='\n')


def take_drugs(route):
    with Editor("funcs/current.txt", "r") as file:
        content = file.readline()
    print("Here is the list of drugs we have: \n")
    for drag in Drug.store:
        print(drag)
    desired_drug = input("which one would you like to choose? ")
    for drug in Drug.store:
        if drug.name == desired_drug:
            for user in User.store:
                if user.username == content:
                    user.my_drugs = desired_drug
                    print("success!")



