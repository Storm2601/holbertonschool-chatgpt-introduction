#!/usr/bin/python3

class Checkbook:
    """
    Cette classe représente un carnet de chèques permettant de déposer,
    retirer de l'argent
    et consulter le solde actuel.

    Attributes:
        balance (float): Le solde actuel du carnet de chèques.
    """
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        """
        Dépose un montant spécifié sur le carnet de chèques.

        Args:
            amount (float): Le montant à déposer.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Retire un montant spécifié du carnet de chèques, si les fonds
        sont suffisants.

        Args:
            amount (float): Le montant à retirer.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """Affiche le solde actuel du carnet de chèques."""
        print("Current Balance: ${:.2f}".format(self.balance))


def main():
    """
    Fonction principale pour interagir avec le carnet de chèques.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do?
                       (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            amount = float(input("Enter the amount to deposit: $"))
            cb.deposit(amount)
        elif action.lower() == 'withdraw':
            amount = float(input("Enter the amount to withdraw: $"))
            cb.withdraw(amount)
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
