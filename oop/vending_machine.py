"""

 structural pattern (facade)
 - contains VendingMachine class to contain logic
 - SnackMachien class for snacks
 - allows for other types of machines as well that use same logic as a vending machine


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

example:

id: 1, Chips, inventory: 1 cost: $3.00
id: 2, Candy, inventory: 2 cost: $1.00
payment: 2.0 total: 2.15
Payment accepted
Enjoy: Candy
here is your change:
 0.25
 0.25
 0.25

"""



from typing import Dict, List


class Product:
    next_product_id = 1

    def __init__(self, name: str, cost: int, quantity: int) -> None:
        self.product_id = Product.next_product_id
        self.name : str = name
        self.cost : float = cost
        self.quantity : int = quantity
        Product.next_product_id +=1

class Coin:
    def __init__(self, value: float) -> None:
        self.value: float = value

class VendingMachine:
    def __init__(self) -> None:
        self.products: Dict[int, Product] = {}
        self.coins: List[Coin] = []

    def display_products(self):
        """ Display all products and details within the vending machine """
        for product_id, product in self.products.items():
            print(f"id: {product_id}, {product.name}, inventory: {product.quantity} cost: ${product.cost}.00")

    def add_product(self, product: Product):
        """ 
        add product to all products
         - if its a new product assign a new key
         - existing product update the quantity
        """
        if product.product_id not in self.products:
             self.products[product.product_id] = product
        else:
            self.products[product.product_id].quantity += 1
        

    def add_coin(self, coin: Coin, quantity: int):
        """ add coin to vending machine """
        for _ in range(quantity):
            self.coins.append(coin)

    def dispense_product(self,  id: int, amount: float):
        """ update quantity if product exists """
        if id in self.products:
            # subtract quantity from total product count
            if self.products[id].quantity > 0 and self.products[id].cost <= amount:
                self.products[id].quantity -=1
                return self.products[id]
        
        return None

    def dispense_change(self, amount: float):
        """ remove amount for total coins stored """
        change: List[Coin]= []
        remaining_change: float = amount

        for coin in self.coins:
             while remaining_change >= coin.value:
                 change.append(coin)
                 remaining_change -= coin.value
                 self.coins.remove(coin)

        return change


    def accept_payment(self, payment: float):
        """ confirm that there are enough coins to dispense change before allowing payment """
        
        total : float = sum(coin.value for coin in self.coins )
        print(f"payment: {payment} total: {total}")
        if total >= payment:
            return True
        else:
            return False


class SnackMachine:

    def __init__(self, vending_machine: VendingMachine) -> None:
        self.vending_machine: VendingMachine = vending_machine

    def display_products(self):
        return self.vending_machine.display_products()

    def add_product(self, product: Product):
        return self.vending_machine.add_product(product)

    def add_coin(self, coin: Coin, quantity: int):
        return self.vending_machine.add_coin(coin, quantity)

    def dispense_product(self, id: int, amount: float):
        return self.vending_machine.dispense_product(id, amount)

    def dispense_change(self, amount: float):
        return self.vending_machine.dispense_change(amount)

    def accept_payment(self, amount: float):
        return self.vending_machine.accept_payment(amount)


if __name__ == "__main__":
    print("###########################################################################################")
    print("\t\t\t VENDING MACHINE")
    print("###########################################################################################")
    # create coins to store in vending machine
    quarter = Coin(.25)
    dime = Coin(.10)
    nickel = Coin(.05)

    # name: str, cost: int, quantity: int
    chips: Product = Product(name="Chips", cost=3, quantity=1)
    candy: Product = Product(name="Candy", cost=1, quantity=1)
    vending_machine = VendingMachine()
    snack_machine = SnackMachine(vending_machine)

    snack_machine.add_coin(quarter, 4)
    snack_machine.add_coin(dime, 10)
    snack_machine.add_coin(nickel, 1)

    snack_machine.add_product(product=chips)
    snack_machine.add_product(product=candy)
    snack_machine.add_product(product=candy)
    snack_machine.display_products()

    amount = 2.00
    product_requested= 1

    if snack_machine.accept_payment(amount=amount):
        print("Payment accepted")

        # dispense product
        # assume customer wants to purchase item 2 which is candy
        product_dispensed: Product = snack_machine.dispense_product(product_requested, amount)
        if product_dispensed:
            print(f"Enjoy: {product_dispensed.name}")
            change: List[Coin] = snack_machine.dispense_change(amount - product_dispensed.cost)
            print(f"here is your change:")
            for coin in change:
                print(f" {coin.value}")
        else:
            print(f"insufficient amount..... {amount}")


    else:
        print("Payment not accepted due to insufficient change")

