
class Employee:
    def __init__(self, name='', salary=''):
        self.name = name
        self.salary = salary

    def show_employee(self):
        print(f"{self.name}\t{self.salary}")