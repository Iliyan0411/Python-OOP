from employee import Employee
from bussiness import Bussiness

class Casino(Bussiness):
    def __init__(self, slots='', **kwargs):
        super().__init__(**kwargs)
        self.slots = slots

    def show(self):
        super().show()
        print("\nCASINO DETAILS")
        print(f"slots: {self.slots}")

    def prompt_init():
        parent_init = Bussiness.prompt_init()

        slots = int(input("Enter number of slots: "))

        parent_init.update({
            "slots": slots
        })

        return parent_init

    prompt_init = staticmethod(prompt_init)
