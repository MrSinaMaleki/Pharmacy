from abc import ABC, abstractmethod


class Model(ABC):
    @classmethod
    @property
    @abstractmethod
    def store(cls): # noqa
        raise NotImplemented("'store' attr is required ! ")

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print("instance: ", instance)
        cls.store.append(instance) # noqa
        return instance



