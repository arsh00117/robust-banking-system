"""
Bank Account System
Author: Arsh
Description: CLI-based Bank Account System demonstrating OOP concepts.
"""


class Account:
    """Demonstrates OOP — encapsulation, private attributes, and methods."""

    def __init__(self, account_no: int, full_name: str, balance: int, mobile_no: int, email: str, pin: int) -> None:
        self.account_no: int = account_no
        self.full_name: str = full_name
        self.mobile_no: int = mobile_no
        self.email: str = email

        self.__balance: int = balance
        self.__pin: int = pin

    def _get_valid_amount(self, prompt: str) -> int:
        """Loops until a valid positive integer amount is entered."""
        while True:
            try:
                amount = int(input(prompt))
                if amount <= 0:
                    print("Amount must be greater than 0.")
                    continue
                return amount
            except ValueError:
                print("Invalid input. Please enter a number.")

    def show_details(self) -> None:
        print("\n---- ACCOUNT DETAILS ----")
        print(f"{'Account No':<12} {self.account_no}")
        print(f"{'Full Name':<12} {self.full_name}")
        print(f"{'Mobile No':<12} {self.mobile_no}")
        print(f"{'Email':<12} {self.email}")

    def deposit(self) -> None:
        print("\n---- DEPOSIT ----")
        amount: int = self._get_valid_amount("Enter amount: ₹")
        self.__balance += amount
        print(f"Deposited ₹{amount} | Current Balance: ₹{self.__balance}")

    def withdraw(self) -> None:
        print("\n---- WITHDRAW ----")
        amount: int = self._get_valid_amount("Enter amount: ₹")
        if amount > self.__balance:
            print("Insufficient balance.")
            return
        self.__balance -= amount
        print(f"Withdrawn ₹{amount} | Balance Left: ₹{self.__balance}")

    def get_balance(self) -> int:
        return self.__balance

    def login(self) -> bool:
        """Allows 3 PIN attempts before locking out. Returns True on success."""
        attempts: int = 0

        while attempts < 3:
            print("\n---- LOGIN ----")
            try:
                pin: int = int(input("Enter PIN: "))
                if len(str(pin)) != 4:
                    print("PIN must be exactly 4 digits.")
                    attempts += 1
                    continue
                if pin == self.__pin:
                    print("Login successful.")
                    return True
                else:
                    print(f"Incorrect PIN. {2 - attempts} attempt(s) remaining.")
                    attempts += 1
            except ValueError:
                print("PIN must be digits only.")
                attempts += 1

        print("Too many failed attempts. Access denied.")
        return False


def show_menu() -> None:
    print("\n---- MAIN MENU ----")
    options: list[tuple[int, str]] = [
        (1, "Display Details"),
        (2, "Deposit"),
        (3, "Withdraw"),
        (4, "Check Balance"),
        (5, "Logout"),
    ]
    for option, action in options:
        print(f"{option}. {action}")


def ask_return_to_menu() -> bool:
    """Returns True to continue, False to exit."""
    while True:
        choice: str = input("\nReturn to Main Menu? (y/n): ").strip().lower()
        if choice in ("y", "yes"):
            return True
        elif choice in ("n", "no"):
            print("Goodbye! — Made by Arsh")
            return False
        else:
            print("Invalid input. Enter y or n.")


def main() -> None:
    account = Account(
        account_no=5001037423,
        full_name="Arshdeep Singh",
        balance=89000,
        mobile_no=9988776655,
        email="abc@xyz.com",
        pin=9833
    )

    if not account.login():
        return

    while True:
        show_menu()
        try:
            choice: int = int(input("Enter choice (1-5): "))

            if choice == 1:
                account.show_details()
            elif choice == 2:
                account.deposit()
            elif choice == 3:
                account.withdraw()
            elif choice == 4:
                print(f"\nCurrent Balance: ₹{account.get_balance()}")
            elif choice == 5:
                print("Thanks for using! — Made by Arsh")
                break
            else:
                print("Invalid option. Please choose between 1 and 5.")
                continue

            if not ask_return_to_menu():
                break

        except ValueError:
            print("Input must be a number.")


if __name__ == "__main__":
    main()
