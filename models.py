from core.model import Model
import enum


class Role(enum.Enum):
    Doctor = 'Doctor'
    Staff = 'Staff'
    Admin = 'Admin'
    Patient = 'patient'


class User(Model):
    store = []

    def validate_username(self, username: str) -> None:
        assert isinstance(username, str) and len(username) >= 4, "Username must be str type and length >= 4"
        for user in self.__class__.store:
            if hasattr(user, "username"):
                assert user.username != username, "Username already exists !"

    @staticmethod
    def validate_password(password: str) -> None:
        assert isinstance(password, str) and len(password) >= 4, "Password must be str type and length >= 4"

    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

        self._role = "patient"
        self._my_drugs = []

    @property
    def my_drugs(self):
        return self._my_drugs

    @my_drugs.setter
    def my_drugs(self, new_val):
        self._my_drugs.append(new_val)

    @property
    def role(self):
        return self._role

    @role.setter
    def role(self, new_val):
        self._role = new_val

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, new_username: str) -> None:
        self.validate_username(new_username)
        self.__username = new_username

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, new_password: str) -> None:
        self.validate_password(new_password)
        self.__password = new_password


class Drug(Model):
    store = []

    def validate_quantity(self):
        ...

    def validate_name(self, new_name):
        for drug in self.__class__.store:
            if hasattr(self, 'name'):
                if new_name == drug.name:
                    raise Exception('name must be unique!')
        return True

    def __init__(self, name, quantity, takable: bool):
        self.name = name
        self.quantity = quantity
        self._takeble = takable

    @property
    def takeble(self):
        return self._takeble

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if self.validate_name(new_name):
            self._name = new_name

    def __add__(self, other):
        return self.quantity + other.quantity

    def __repr__(self):
        return f"Drug(name:{self.name!r}, quantity:{self.quantity!r}, takeable:{self.takeble})"
