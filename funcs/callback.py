from models import Drug


def add_drug(route):
    name = input('enter drug name: ')
    number = int(input('enter drug number: '))
    takeble = input("Is it takebale? (y/n)")
    Drug(name, number, True if takeble.lower() == "y" else False)


def list_drug(route):
    for counter, drug in enumerate(Drug.store, start=1):
        print(drug, end='\n')

