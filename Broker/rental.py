from property import get_valid_input

class Rental:
    def __init__(self, furnished='', utilities='',
                rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent
 
    def display(self):
        super().display()
        print("\nRENTAL DETAILS")
        print(f"rent: {self.rent}")
        print(f"estimated utilities: {self.utilities}")
        print(f"furnished: {self.furnished}")

    def prompt_init():
        return dict(
            rent = input('What is the monthly rent? '),
            utilities = input(
                "What are the estimated utilities? "
            ),
            furnished = get_valid_input(
                "Is the property furnished? ",
                ("yes", "no")
            )
        )

    prompt_init = staticmethod(prompt_init)