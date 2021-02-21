from employee import Employee
from hotel import Hotel
from casino import Casino

class Complex(Hotel, Casino):
    def prompt_init():
        parent_init = Hotel.prompt_init()

        slots = int(input("Enter number of slots: "))

        parent_init.update({
            "slots": slots
        })

        return parent_init

    prompt_init = staticmethod(prompt_init)
