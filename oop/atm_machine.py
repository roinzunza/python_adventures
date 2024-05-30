"""
entities
- atm machine
- user
- bank

Actions
- view balance
- withdraw money
- desposit money
- authenticate user

"""

class User:

    def __init__(self, name, account_number, pin) -> None:
        self.name = name
        self.account_number = account_number
        self.pin = pin


class Bank:
    def __init__(self) -> None:
        self.accounts =  {"123456": {"user": "Alice", "pin": "1234", "balance": 1000},
                         "654321": {"user": "Bob", "pin": "4321", "balance": 2000}}
    def authenticate_user(self, account_number, pin):
        """Authenticate user with provided account number & PIN."""
        if account_number in self.accounts:
            if  self.accounts[account_number]['pin'] == pin:
                return True
            
        return False

    def view_balance(self, account_number):
        """Get the account balance of the authenticated user."""
        return self.accounts[account_number]['balance']

    def deposit_money(self, account_number, amount):
        """ Add to the existing balance of the authenticated user"""
        self.accounts[account_number]["balance"] += amount
        return amount

    def withdraw_money(self, account_number, amount):
        """ withdraw from the existing balance of the authenticated user"""
        self.accounts[account_number]["balance"] -= amount
        return amount


class Atm:
    def __init__(self, bank) -> None:
        self.bank = bank

    def authenticate_user(self, account_number, pin):
        return self.bank.authenticate_user(account_number, pin)

    def view_balance(self, account_number):
        return self.bank.view_balance(account_number)

    def deposit_money(self, account_number, amount):
        return self.bank.deposit_money(account_number, amount)

    def withdraw_money(self, account_number, amount):
         return self.bank.withdraw_money(account_number, amount)


if __name__ == "__main__":
    bank = Bank()
    atm = Atm(bank)

    user = User("Alice", "123456", "1234")

    if atm.authenticate_user(user.account_number, user.pin):
        print("user authenticated")

        print("viewing balance")
        balance = atm.view_balance(user.account_number)
        print(f"current balance {balance}")

        print("deposit")
        deposit = atm.deposit_money(user.account_number, 500)

        print("current balance")
        balance = atm.view_balance(user.account_number)
        print(f"current balance {balance} after deposit: {deposit}")

        print("withdraw")
        withdraw = atm.withdraw_money(user.account_number, 100)

        balance = atm.view_balance(user.account_number)
        print(f"current balance {balance} after withdraw: {withdraw}")
    else:
        print("authentication failed")

