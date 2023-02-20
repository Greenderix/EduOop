class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        self.goods.pop(indx)

    def get_list(self):
        return [f"{smth.name}: {smth.price}" for smth in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
gd1 = TV('bLOOP', 50000);
gd2 = TV('APPLE', 65999)
gd3 = Notebook('MACBOOK', 76000);
gd4 = Notebook('Lenovo', 56000)
gd5 = Table('not chair', 150000);
gd6 = Cup('with cats', 2500)
cart.add(gd1)
cart.add(gd2)
cart.add(gd3)
cart.add(gd4)
cart.add(gd5)
cart.add(gd6)
