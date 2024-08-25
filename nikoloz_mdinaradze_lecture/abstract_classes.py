from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def say_hi(self):
        pass

class French(Human):
    def say_hi(self):
        print("Salut!")

class Georgian(Human):
    def say_hi(self):
        print("გამარჯობა!")


human1 = French("Gio", 10)
human1.say_hi()

human2 = Georgian("Giorgi", 51)
human2.say_hi()