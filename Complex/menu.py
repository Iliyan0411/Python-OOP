from employee import Employee
from complex import Complex
import sys

class Menu:
    def __init__(self):
        self.complexes = []
        self.choice = {
            1: self.create_complex,
            2: self.delete_complex,
            3: self.hire_employer,
            4: self.fire_employer,
            5: self.search,
            6: self.quit
        }

    def display_menu(self):
        print("""
                1. Create complex
                2. Delete complex
                3. Hire employee
                4. Fire employee
                5. Search complex
                6. Quit""")

    def run(self):
        while True:
            self.display_menu()

            ch = int(input("Enter option: "))

            action = self.choice.get(ch)
            action()

    def _locate(self, complex_name):
        for complex in self.complexes:
            if complex.name == complex_name:
                return complex

    def create_complex(self):
        args = Complex.prompt_init()
        new_complex = Complex(**args)

        self.complexes.append(new_complex)

    def delete_complex(self):
        name_complex = input("Enter name of complex: ")

        old_complex = self._locate(name_complex)
        self.complexes.remove(old_complex)

    def hire_employer(self):
        complex_name = input("Complex name: ")

        new_emp_name = input("Employee's name: ")
        new_emp_salary = int(input("Employee's salary: "))
        new_employee = Employee(new_emp_name, new_emp_salary)

        for complex in self.complexes:
            if complex.name == complex_name:
                complex.hire_employee(new_employee)
                break

    def fire_employer(self):
        complex_name = input("Complex name: ")

        fired_emp_name = input("Employee's name: ")
        fired_emp_salary = int(input("Employee's salary: "))
        fired_employee = Employee(fired_emp_name, fired_emp_salary)

        for complex in self.complexes:
            if complex.name == complex_name:
                complex.fire_employee(fired_employee)
                break

    def search(self):
        complex_name = input("Complex name: ")

        complex = self._locate(complex_name)

        complex.show()

    def quit(self):
        sys.exit(0)




menu = Menu()
menu.run()