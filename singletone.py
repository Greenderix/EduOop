class SingletonFive:
    __instance = None
    __count = 0

    def __new__(cls, *args, **kwargs):
        if cls.__count < 5:
            cls.__instance = super().__new__(cls)
            cls.__count += 1
        return cls.__instance

    def __init__(self, name):
        self.name = name


# objs = [SingletonFive(str(n)) for n in range(10)]  # эту строчку не менять
objs = SingletonFive(str(2))
objs2 = SingletonFive(str(3))
objs3 = SingletonFive(str(45))
objs4 = SingletonFive(str(43))
objs5 = SingletonFive(str(43))
objs6 = SingletonFive(str(43))
print(id(objs), id(objs2), id(objs5), id(objs6))
