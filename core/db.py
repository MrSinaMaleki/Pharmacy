import pickle


class DataBase:
    __store = {}
    __models = set()

    def __init__(self, path: str) -> None:
        self.path = path

    def __getitem__(self, item):
        return self.__store[item]
