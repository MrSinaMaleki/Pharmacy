from core.db import DataBase

if __name__ == "__main__":
    db = DataBase("db.pickle")
    db.register()