"""
Створіть клас NumberString, успадкуйте його від класу UserString,
визначте для нього метод number_count(self), який буде рахувати кількість цифр у рядку.
"""

from collections import UserString


class NumberString(UserString):

    def __init__(self, data_str):
        self.data_str = data_str

    def number_count(self):
        return sum(c.isdigit() for c in self.data_str)


num = NumberString('akjrhg285tjhergwfg')

print(num.number_count())
 