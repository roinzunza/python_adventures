"""
Entities/objects
- Product
- coin
- vending machine

Actions
- view producuts
- add products
- add coin
- dispense product
- dispense change
- accept payment
"""

class Product:
    def __init__(self, name, cost) -> None:
        self.name = name
        self.cost = cost


class Coin:
    def __init__(self, value) -> None:
        self.value = value



class VendingMachine:
    def __init__(self) -> None:
        self.products = []
        self.coins = []

    def display_products(self):
        pass

    def add_product(self):
        pass

    def add_coin(self):
        pass

    def dispense_product(self):
        pass

    def dispense_change(self):
        pass

    def accept_payment(self):
        pass
