from house_rental import HouseRental, HousePurchase
from apartment_rental import ApartmentRental, ApartmentPurchase
from property import  get_valid_input

class Agent:
    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for prop in self.property_list:
            prop.display()

    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def add_property(self):
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")
        ).lower()

        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")
        ).lower()

        PropertyClass = self.type_map[
            (property_type, payment_type)]

        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))


agent = Agent()
agent.add_property()
# agent.add_property()
agent.display_properties()