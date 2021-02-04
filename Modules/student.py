

class Student:
    def __init__(self, name, fn, grade):
        self.name = name
        self.fn = fn
        self.grade = grade

    def name(self):
        return self.name
    
    def fn(self):
        return self.fn

    def grade(self):
        return self.grade

    def print_student(self):
        print(f'{self.name}\t{self.fn}\t{self.grade}')