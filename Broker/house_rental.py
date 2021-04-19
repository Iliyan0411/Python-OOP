from house import House
from rental import Rental
from purchase import Purchase

class HouseRental(Rental, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)



class HousePurchase(Purchase, House):
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())

        return init

    prompt_init = staticmethod(prompt_init)
