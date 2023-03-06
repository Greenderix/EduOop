class Car:
    def __init__(self):
        self.__model = None

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if type(value) == str and 2 <= value <= 100:
            self.__model = value
