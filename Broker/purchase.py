
class Purchase:
    def __init__(self, price='', taxes='', **kwargs):
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super().display()
        print("PURCHASE DETAILS")
        print(f"selling price: {self.price}")
        print(f"estimated taxes: {self.taxes}")

    def  prompt_init():
        return dict(
            price = input("What is the selling price? "),
            taxes = input("What are the estimated taxes? ")
        )

    prompt_init = staticmethod(prompt_init)