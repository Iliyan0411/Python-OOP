class Student:
    def __init__(self, name, fn, grade) -> None:
        self.name = name
        self.fn = fn
        self.grade = grade

    def print_student(self):
        print(f'{self.name}\t{self.fn}\t{self.grade}')

    def good_student(self):
        return self.grade >= 3

