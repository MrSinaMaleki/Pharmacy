class Test:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        print(instance)
        return instance

