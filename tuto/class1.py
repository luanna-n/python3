# -*- coding: latin-1 -*-

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def saudacao(self):
        ola = "I am {} and I have {} years."
        print(ola.format(self.name, self.age))

class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.year = year
    def welcome(self):
        print("Welcome", self.name, "to the class of", self.year)

aluno01 = Student("Maria", 25, 2024)
aluno02 = Student("João", 24, 2020)

print(aluno01.age)
print(aluno01.name)
#print(aluno01.saudacao)
#print(aluno01.welcome)
print(aluno02.age)
print(aluno02.name)
#print(aluno02.saudacao)
#print(aluno02.welcome)
aluno02.welcome()
aluno02.saudacao()