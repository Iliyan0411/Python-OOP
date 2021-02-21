from employee import Employee

class Bussiness:
    def __init__(self, name='', **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.personal = []

    def show(self):
        print("\nBUSSINESS DETAILS")
        print("NAME: " + self.name)

        for employee in self.personal:
            employee.show_employee()

    def hire_employee(self, new_employee):
        self.personal.append(new_employee)

    def fire_employee(self, fired_employee):
        for i in range(0, len(self.personal)):
            if self.personal[i].name == fired_employee.name:
                self.personal.pop(i)
                break

    def prompt_init():
        return dict(
            name = input("Enter the name of bussiness: ")
        )

    prompt_init = staticmethod(prompt_init)
