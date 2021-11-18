# -*- coding: latin-1 -*-

class Person:

    #class level atribute, available on instance and class itself
    race = 'human'

    def __init__(self, name, age):
        #instance atributes, available on instance only
        self.name = name
        self.age = age

    def saudacao(self):
        ola = "I am {} and I have {} years."
        print(ola.format(self.name, self.age))

    #class method, available on instance and class itself
    @classmethod
    def commons(cls):
        return f'Every person belongs to the {cls.race} race'

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
aluno01.welcome()
aluno01.saudacao()
print(aluno01.commons())