class Book:
    def __init__(self, author, name, price):
        self.__author = author
        self.__title = name
        self.__price = price

    def set_title(self, title):
        self.__title = title

    def set_author(self, author):
        self.__author = author

    def set_price(self, price):
        self.__price = price

    def get_price(self):
        return self.__price

    def get_author(self):
        return self.__author

    def get_title(self):
        return self.__title
