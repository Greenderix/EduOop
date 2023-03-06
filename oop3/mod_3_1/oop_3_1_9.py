class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 1000

    def __init__(self, a, b, c):
        self.__a = self.__b = self.__c = None
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def __verife_value(cls, value):
        return type(value) in (int, float) and cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.__verife_value(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.__verife_value(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.__verife_value(value):
            self.__c = value

    def __setattr__(self, key, value):
        if key in ("MIN_DIMENSION", "MAX_DIMENSION"):
            raise AttributeError("Менять атрибуты MIN_DIMENSION и MAX_DIMENSION запрещено.")
        super().__setattr__(key, value)
