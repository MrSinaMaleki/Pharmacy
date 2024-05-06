import pickle


class DataBase:
    __store = {}
    __models = set()

    def __init__(self, path: str) -> None:
        self.path = path

    def __getitem__(self, item):
        return self.__store[item]

    def load(self):
        pass

    def save(self):
        pass

    def register(self, model):
        self.__class__.__models[model.__name__] = model
        self.__class__.__store.setdefault(model.__name__, model.store)
