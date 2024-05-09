import atexit
import signal

from core.db import DataBase
from models import User
from core.hook import Hook, Mode
from core.lifecycle import LifeCycle

from routes import router

if __name__ == "__main__":
    db = DataBase("db.pickle")
    db.register(User)

    atexit.register(db.save)
    signal.signal(signal.SIGTERM, lambda signum, frame: exit())

    Hook(Mode.INITIAL, db.load)
    Hook(Mode.FINISH, lambda: db.save() or atexit.unregister(db.save))

    with LifeCycle() as lifecycle:
        router()
