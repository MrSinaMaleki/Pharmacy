from abc import ABC, abstractmethod


class Model(ABC):
    @classmethod
    @property
    @abstractmethod
    def store(cls):
        raise NotImplemented("'store' attr is required ! ")

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.store.append(instance)
        return instance
