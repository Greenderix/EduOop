class Money:
    def __init__(self, mn):
        self.__money = 0
        if self.__check_money(mn):
            self.__money = mn

    @classmethod
    def __check_money(cls, mn):
        return type(mn) == int and mn >= 0

    def set_money(self, money):
        if __check_money(money):
            self.__money = money

    def get_money(self):
        return self.__money

    def add_money(self, mn):
        self.__money += mn.get_money()
