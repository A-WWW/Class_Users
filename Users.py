
#Для уменьшения кода решил использовать насовсем стандартное решения, пользователей заводить как подклассы,
# это дало возможность использовать стандартные методы, вроде все работает.

import csv

class Users:
    registry = {}
    fail = "registry.csv"

    def __init__(self, first_name, last_name, age, citi='Kiev'):
        self.change(first_name, last_name, age, citi)

    def change(self, first_name, last_name, age, citi):
        self.__last_name = last_name
        self.__first_name = first_name
        self.__age = age
        self.__citi = citi
        a = {self.__first_name: (self)}
        self.registry.update(a)

    def __str__(self):
        return f" {self.__first_name} {self.__last_name}: age - {self.__age}, citi - {self.__citi}"

    @staticmethod
    def search(value):
        for val in dict.items(Users.registry):
            if val[1].__last_name == value:
                print(val[1].__last_name, val[1].__first_name, val[1].__age, val[1].__citi)
            if val[1].__first_name == value:
                print(val[1].__last_name, val[1].__first_name, val[1].__age, val[1].__citi)
            if val[1].__age == value:
                print(val[1].__last_name, val[1].__first_name, val[1].__age, val[1].__citi)
            if val[1].__citi == value:
                print(val[1].__last_name, val[1].__first_name, val[1].__age, val[1].__citi)

    def print_registry():
        for val in Users.registry.values():
            print(val)

    # Можно было не вставлять так как прямой вызов подкласса  благодаря __str__
    # принтует тоже, но  оставил так как возможно понадобится для киви
    def print_user(self):
        print(self.__first_name, self.__last_name, ':' " " 'age', self.__age, ',', "citi", self.__citi)

    def del_user(self):
        del Users.registry[self.__first_name]
        del self
    # сохраняется в каталог проэкта и открывается оттуда  Excel.
    def save():
        with open(Users.fail, "w", newline='') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(['first_name', 'last_name', 'age', 'citi'])
            for val in dict.items(Users.registry):
                writer.writerow([val[1].__first_name, val[1].__last_name, val[1].__age, val[1].__citi])


Vova = Users('Vova', 'Ivanov', 15, 'Kiev')
Vasy = Users('Vasy', 'Ivanov', 19, 'Kiev')
Maria = Users('Maria', 'Vasileva', 21, 'Kiev')
Vlasa = Users('Vlasa', 'Serova', 25, 'Kiev')

print(Vlasa)
print(Users.registry)
Users.print_registry()

Users.search('Ivanov')

print(Vlasa)
Vlasa.change('Vlasa', 'Garsia', 19, 'Kiev')
print(Vlasa)
Users.print_registry()

Gigo = Users('Gigo', 'Serco', 25, 'Kiev')
Users.print_registry()
Gigo.del_user()
Users.print_registry()

Maria.print_user()
Users.save()
