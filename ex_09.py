"""
У четвертому модулі ми реалізували функцію lookup_key для пошуку всіх ключів за значенням у словнику.
Першим параметром у функцію ми передавали словник, а другим – значення, яке хотіли знайти.
Результатом був список ключів або порожній список, якщо ми нічого не знаходили.

def lookup_key(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)
    return keys
Створіть клас LookUpKeyDict, батьком якого буде клас UserDict. Зробіть функцію lookup_key методом класу LookUpKeyDict.
"""

from collections import UserDict


class LookUpKeyDict(UserDict):
    
    def __init__(self, data):
        self.data = data
    
    def lookup_key(self, value):
        keys = []
        for key in self.data:
            if self.data[key] == value:
                keys.append(key)
        return keys
        

look = LookUpKeyDict({'F': 1, 'FX': 2, 'E': 3, 'D': 3, 'C': 4, 'B': 5, 'A': 5})

print(look.lookup_key(5))
  