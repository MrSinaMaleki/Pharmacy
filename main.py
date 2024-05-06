import atexit

from core.db import DataBase
from models import User

if __name__ == "__main__":
    db = DataBase("db.pickle")
    db.register(User)

    atexit.register(db.save)
