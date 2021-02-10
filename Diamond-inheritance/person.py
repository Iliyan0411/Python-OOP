

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print(self):
        print(f'{self.name}\t{self.age}')


class Young(Person):
    def tell_cond(self):
        print('I am young!')

class Old(Person):
    def tell_cond(self):
        print('I am old!')

class Worker(Old, Young):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)
        self.salary = salary

    def print(self):
        Person.print(self)
        print('\t', self.salary)

    def tell_cond(self):
        if self.age < 55:
            Young.tell_cond(self)
        else:
            Old.tell_cond(self)