
class Property:
    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("================")
        print("square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths))
        print()

    def prompt_init():
        return dict(square_feet=int(input('Enter the square feet: ')),
                    beds=int(input('Enter number of bedrooms: ')),
                    baths=int(input('Enter number of baths: ')))

    prompt_init = staticmethod(prompt_init)

    
def get_valid_input(input_string, valid_options):
    input_string += "({})".format(", ".join(valid_options))

    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)

    return response
