from employee import Employee
from bussiness import Bussiness

class Hotel(Bussiness):
    def __init__(self, rooms='', **kwargs):
        super().__init__(**kwargs)
        self.rooms = rooms

    def show(self):
        super().show()
        print("\nHOTEL DETAILS")
        print(f"rooms: {self.rooms}")

    def prompt_init():
        parent_init = Bussiness.prompt_init()

        rooms = int(input("Enter number of rooms: "))

        parent_init.update({
            "rooms": rooms
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)