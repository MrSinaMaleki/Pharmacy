import pickle
from .filehandler import Editor


class DataBase:
    __store = {}
    __models = {}

    def __init__(self, path: str) -> None:
        self.path = path

    def __getitem__(self, item):
        return self.__store[item]

    def load(self):
        try:
            with Editor(self.path, "rb") as file:
                self.__store = pickle.load(file)

                for model in self.__models.values():
                    model.store = self.__store.get(model.__name__, [])
        except (FileNotFoundError, EOFError):
            pass

    def save(self):
        with Editor(self.path, "wb") as file:
            for model in self.__models.values():
                self.__store[model.__name__] = model.store

            pickle.dump(self.__store, file)

    def register(self, model):
        self.__class__.__models[model.__name__] = model
        self.__class__.__store.setdefault(model.__name__, model.store)
