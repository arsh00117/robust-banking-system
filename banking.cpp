#include <iostream>
#include <string>
#include <vector>

using namespace std;

class AccountInterface {
public:
    virtual void deposit(double amount) = 0;       
    virtual void withdraw(double amount) = 0;      
    virtual void displayBalance() const = 0;       
    virtual ~AccountInterface() {}                 
};

class BankAccount : public AccountInterface {
private:
    string accountHolder;
    string pin;

protected:
    double balance; 

public:
    BankAccount(string name, string userPin, double initialBalance) {
        accountHolder = name;
        pin = userPin;
        balance = initialBalance;
    }

    bool validatePIN(const string& inputPin) const {
        return pin == inputPin;
    }

    string getAccountHolder() const {
        return accountHolder;
    }

    void deposit(double amount) override {
        if (amount > 0) {
            balance += amount;
            cout << "\n[Success] Successfully deposited ₹" << amount << endl;
        } else {
            cout << "\n[Error] Invalid deposit amount!" << endl;
        }
    }
};

class SavingsAccount : public BankAccount {
private:
    double interestRate;

public:
    SavingsAccount(string name, string userPin, double initialBalance, double rate)
        : BankAccount(name, userPin, initialBalance), interestRate(rate) {}

    void withdraw(double amount) override {
        if (amount <= 0) {
            cout << "\n[Error] Invalid withdrawal amount!" << endl;
        } else if (amount > balance) {
            cout << "\n[Error] Insufficient funds! Current balance: ₹" << balance << endl;
        } else {
            balance -= amount;
            cout << "\n[Success] Successfully withdrew ₹" << amount << endl;
        }
    }

    void displayBalance() const override {
        cout << "\n--- Savings Account Summary ---" << endl;
        cout << "Account Holder: " << getAccountHolder() << endl;
        cout << "Current Balance: ₹" << balance << endl;
        cout << "Interest Rate: " << interestRate << "% annually" << endl;
        cout << "-------------------------------" << endl;
    }
};

class CurrentAccount : public BankAccount {
private:
    double overdraftLimit;

public:
    CurrentAccount(string name, string userPin, double initialBalance, double limit)
        : BankAccount(name, userPin, initialBalance), overdraftLimit(limit) {}

    void withdraw(double amount) override {
        if (amount <= 0) {
            cout << "\n[Error] Invalid withdrawal amount!" << endl;
        } else if (amount > (balance + overdraftLimit)) {
            cout << "\n[Error] Overdraft limit exceeded! Max available: ₹" << (balance + overdraftLimit) << endl;
        } else {
            balance -= amount;
            cout << "\n[Success] Successfully withdrew ₹" << amount << endl;
        }
    }

    void displayBalance() const override {
        cout << "\n--- Current Account Summary ---" << endl;
        cout << "Account Holder: " << getAccountHolder() << endl;
        cout << "Current Balance: ₹" << balance << endl;
        cout << "Overdraft Limit: ₹" << overdraftLimit << endl;
        cout << "-------------------------------" << endl;
    }
};

int main() {
    AccountInterface* myAccount = nullptr;
    
    string inputPin;
    int trials = 3;
    bool isAuthenticated = false;

    cout << "========================================" << endl;
    cout << "      WELCOME TO ARSH BANKING SYSTEM    " << endl;
    cout << "========================================" << endl;

    int accType;
    cout << "\nSelect Account Type to Access:\n1. Savings Account\n2. Current Account\nChoice: ";
    cin >> accType;

    if (accType == 1) {
        myAccount = new SavingsAccount("Arshdeep Singh", "2508", 5000.0, 4.0);
    } else if (accType == 2) {
        myAccount = new CurrentAccount("Arshdeep Singh", "2508", 10000.0, 2000.0);
    } else {
        cout << "\n[Error] Invalid account type choice." << endl;
        return 0;
    }

    BankAccount* basePtr = dynamic_cast<BankAccount*>(myAccount);

    while (trials > 0) {
        cout << "\nPlease enter your 4-digit PIN (Attempts remaining: " << trials << "): ";
        cin >> inputPin;

        if (basePtr && basePtr->validatePIN(inputPin)) {
            isAuthenticated = true;
            break;
        } else {
            cout << "[Access Denied] Incorrect PIN structure or value." << endl;
            trials--;
        }
    }

    if (!isAuthenticated) {
        cout << "\n[ALERT] Too many failed attempts. Your account has been temporarily locked." << endl;
        delete myAccount;
        return 0; 
    }

    int choice;
    do {
        cout << "\n========= MAIN MENU =========" << endl;
        cout << "1. Check Balance" << endl;
        cout << "2. Deposit Funds" << endl;
        cout << "3. Withdraw Funds" << endl;
        cout << "4. Exit Application" << endl;
        cout << "Enter choice (1-4): ";
        cin >> choice;

        switch (choice) {
            case 1:
                myAccount->displayBalance();
                break;
            case 2: {
                double depAmount;
                cout << "Enter amount to deposit: ₹";
                cin >> depAmount;
                myAccount->deposit(depAmount);
                break;
            }
            case 3: {
                double witAmount;
                cout << "Enter amount to withdraw: ₹";
                cin >> witAmount;
                myAccount->withdraw(witAmount);
                break;
            }
            case 4:
                cout << "\nThank you for choosing Apex Banking. Goodbye!" << endl;
                break;
            default:
                cout << "\n[Error] Invalid choice! Please select an option between 1 and 4." << endl;
        }
    } while (choice != 4);

    delete myAccount;
    return 0;
}
