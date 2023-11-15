"""
Додамо в клас Animal змінну класу color, значення якої спочатку дорівнює 'white',
і метод change_color, який повинен змінювати значення змінної класу color.

Створіть екземпляри об'єкта: first_animal та second_animal

Викличте функцію change_color("red") для будь-якого екземпляра об'єкту Animal
та змініть значення змінної класу color на "red".
"""

class Animal:
    color = "white"

    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

    def change_color(self, new_color):
        self.color = new_color


first_animal = Animal("Nick1", "white")
second_animal = Animal("Nick2", "white")
first_animal.change_color("red")
Animal.color = "red"

print(first_animal.color)
