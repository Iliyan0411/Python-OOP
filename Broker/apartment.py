from property import Property, get_valid_input

class Apartment(Property):
    valid_balconies = ("yes", "no", "solarium")
    valid_laundries = ("coin", "ensuite", "none")

    def __init__(self, balcony='', laundry='', **kwargs):
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: %s" % self.laundry)
        print("has balcony: %s" % self.balcony)

    def prompt_init():
        parent_init = Property.prompt_init()

        laundry = get_valid_input("What laundry facilities does the property have? ",
                                    Apartment.valid_laundries)

        balcony = get_valid_input("Does the property have a balcony? ",
                                    Apartment.valid_balconies)
        
        parent_init.update({
        "laundry": laundry,
        "balcony": balcony
        })

        return parent_init

    prompt_init = staticmethod(prompt_init)
