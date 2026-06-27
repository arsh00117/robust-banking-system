class Account:
    def __init__(self,account_no: int,full_name: str, balance: int, mobile_no: int, email: str, pin: int):
       
        """ Helps to store variables """

        # Public variables
        self.account_no = account_no
        self.full_name = full_name
        self.mobile_no = mobile_no
        self.email = email
        
        # Truly Private variables
        self.__balance = balance
        self.__pin = pin

    def get_valid_amt(self, prompt: str) -> int:

        """ This helps to fix input errors """

        # Repeates till get valid amount input
        while True:
            try: 
                input_amount = int(input(prompt))

                if input_amount<=0:
                    print("Amount should be more than 0")
                    continue
                return input_amount
            
            except Exception as e:
                print(f"Error : {e}")
    
    def show_details(self) -> None :
        """ Displays account details in breif """

        # Display only details
        print("\n--ACCOUNT DETAILS--")
        print(f"Account No: {self.account_no}")
        print(f"Full Name: {self.full_name}")
        print(f"Mobile No: {self.mobile_no}")
        print(f"Email Id: {self.email}\n")
    
    def deposit(self):

        """ This function helps to deposit amount in Account """

        print("\n--DEPOSIT--")
        deposit_amount = self.get_valid_amt("Enter Amount: ")
        self.__balance += deposit_amount
        print(f"Amount Deposited\nCurrent Balance: ₹{self.__balance}")

    def get_bal(self) -> int:

        """ This returns balance """

        # Not editable
        return self.__balance

    def withdraw(self):

        """ This withdraw money from account. """
        
        print("\n--WITHDRAW--")
        withdraw_amount = self.get_valid_amt("Enter Amount: ")
        if self.__balance < withdraw_amount:
            print("INSUFFICIENT BALANCE")
            return
        self.__balance -= withdraw_amount
        print(f"Amount withdrawn\nBalance Left: ₹{self.__balance}")


    def login(self)->bool:
        
        attempt = 0
        """ This enter login screen """
            
        while True:
            print("\n--LOGIN--")
            if attempt >= 3:
                print("Attempt Exceeded..")
                return False
            try:
                input_pin = int(input("Enter PIN: "))
                pin_size = len(str(input_pin))
                attempt += 1

                if pin_size != 4:
                    print("Pin should be of 4 digits")
                    continue
                
                if self.__pin == input_pin:
                    return True
                else:
                    print("INCORRECT PIN")
                    continue

                
            except ValueError:
                print("Error: PIN must be digits only")

            except Exception as e:
                print(f"Error: {e}")
    
def main_menu():

    """ This displays main menu for this account """

    print("\n--MAIN MENU--")
    print("1.Display Details\n2.Deposit\n3.Withdraw\n4.Check Balance\n5.Logout")

def menu_return() -> bool :

    """ Helps to choose user to return to main menu or not """
    while True:
        exit_choice = input("Return to Main Menu? (y/n): ").lower()
        if exit_choice == "y" or exit_choice == "yes":
            return True
        elif exit_choice == "n" or exit_choice == "no":
            print("Thanks for using System @ Code by ARSH")
            return False
        else:
            print("INVALID INPUT")

if __name__ == "__main__" :
    ac = Account(5001037423,"Arshdeep Singh", 89000, 9988776655, "abc@xyz.com", 9833)
    if ac.login():
        while True:
            main_menu()
            try:
                op = int(input("Enter Choice[1-5]: "))
                if op == 1:
                    ac.show_details()
                    if not menu_return():
                        break

                elif op == 2:
                    ac.deposit()
                    if not menu_return():
                        break

                elif op == 3:
                    ac.withdraw()
                    if not menu_return():
                        break

                elif op == 4:
                    print(f"\nCurrent Balance: ₹{ac.get_bal()}")
                    if not menu_return():
                        break

                elif op == 5:
                    print("Thanks for using System @ Code by ARSH")
                    break

                else:
                    print("Enter Valid Input")
            except ValueError:
                print("Input should be digit only")
                            
            except Exception as e:
                print(f"Error: {e}")
