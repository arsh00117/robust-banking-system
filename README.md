# 🏦 Robust Banking Account Management System

> A secure and robust **console-based banking application** built using **C++ (C++17/20)** and **Object-Oriented Programming (OOP)** principles to simulate real-world banking operations through a modular and maintainable architecture.

![C++](https://img.shields.io/badge/C++-17%20%7C%2020-blue?style=for-the-badge&logo=c%2B%2B)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-success?style=for-the-badge)
![OOP](https://img.shields.io/badge/OOP-Implemented-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![CLI](https://img.shields.io/badge/Application-CLI-lightgrey?style=for-the-badge)
![Made By](https://img.shields.io/badge/Made%20By-Arshdeep%20Singh-red?style=for-the-badge)

---

# 📖 Overview

The **Robust Banking Account Management System** is a command-line banking application developed in **C++** to demonstrate real-world software engineering concepts using **Object-Oriented Programming (OOP)**.

The project emphasizes secure authentication, encapsulation of sensitive account data, inheritance, runtime polymorphism, exception-safe programming practices, and modular software design while providing essential banking functionalities through an interactive command-line interface.

### Core Concepts Implemented

- Object-Oriented Programming (OOP)
- Abstraction
- Encapsulation
- Inheritance
- Runtime Polymorphism
- Authentication System
- Input Validation
- Modular Programming
- Clean & Maintainable Code

---

# ✨ Features

✅ Secure 4-Digit PIN Authentication

✅ Maximum 3 Login Attempts

✅ Savings & Current Account Support

✅ Deposit Funds

✅ Withdraw Funds

✅ Check Account Balance

✅ Display Account Information

✅ Runtime Polymorphism using Virtual Functions

✅ Dynamic Account Selection

✅ Strong Input Validation

✅ Interactive CLI Menu

---

# 🛠 Technologies Used

- **C++17 / C++20**
- Object-Oriented Programming (OOP)
- Runtime Polymorphism
- Inheritance
- Encapsulation
- Exception-Safe Programming
- Command Line Interface (CLI)

---

# 📂 Project Structure

```text
Banking-System/
│
├── banking.cpp
├── README.md
└── LICENSE (Optional)
```

---

# 🧩 Object-Oriented Design

This project demonstrates the practical implementation of the four fundamental OOP principles.

| Principle | Implementation |
|-----------|----------------|
| **Abstraction** | Abstract interface (`AccountInterface`) defines common banking operations. |
| **Encapsulation** | Account balance and PIN are protected using private and protected members. |
| **Inheritance** | `SavingsAccount` and `CurrentAccount` inherit from `BankAccount`. |
| **Polymorphism** | Virtual functions allow runtime selection of account-specific behavior. |

---

# 🔄 Workflow

```text
                +----------------+
                |    Start App   |
                +-------+--------+
                        |
                        ▼
             +----------------------+
             | Select Account Type  |
             +----------+-----------+
                        |
                        ▼
              +------------------+
              |    Login (PIN)   |
              +---------+--------+
                        |
          +-------------+-------------+
          |                           |
      Correct PIN               Wrong PIN
          |                           |
          ▼                           ▼
 +------------------+         Attempts < 3 ?
 |    Main Menu     |              |
 +------------------+              |
 | 1. Balance       |              |
 | 2. Deposit       |              |
 | 3. Withdraw      |              |
 | 4. Exit          |              |
 +--------+---------+              |
          |                        |
          ▼                        ▼
 Perform Banking           Account Locked
   Operations                     |
          |                       |
          +-----------+-----------+
                      |
                      ▼
                    Exit
```

---

# 📊 Application Modules

- Authentication
- Savings Account
- Current Account
- Deposit Management
- Withdrawal Management
- Balance Inquiry
- Input Validation
- Runtime Polymorphism

---

# 🔒 Security Features

- Secure PIN Authentication
- Maximum Login Attempt Limit
- Protected Account Information
- Input Validation
- Invalid Transaction Prevention
- Runtime Type Safety using `dynamic_cast`

---

# 💻 Sample Menu

```text
========== APEX BANKING SYSTEM ==========

1. Check Balance
2. Deposit Funds
3. Withdraw Funds
4. Exit

Enter Choice:
```

---

# 📚 Concepts Covered

- Classes & Objects
- Constructors
- Abstract Classes
- Virtual Functions
- Function Overriding
- Inheritance
- Encapsulation
- Runtime Polymorphism
- Dynamic Casting (`dynamic_cast`)
- Input Validation
- Conditional Statements
- Loops
- Modular Programming

---

# 🚀 Future Improvements

- File-Based Data Persistence
- Transaction History
- Account Number Generation
- Interest Calculation
- Change PIN Feature
- Password Encryption
- Multi-User Support
- SQLite / MySQL Integration
- GUI Version using Qt
- REST API Backend
- Web Version

---

# 🎯 Learning Outcomes

This project helped strengthen practical knowledge of:

- C++ Programming
- Object-Oriented Programming
- Software Design
- Runtime Polymorphism
- Inheritance
- Encapsulation
- CLI Application Development
- Problem Solving
- Modular Code Organization

---

# 👨‍💻 Author

## **Arshdeep Singh (ARSH)**

**Computer Science Engineering Student**

**C++ Developer | Aspiring Software Engineer**

> *"Learning by Building Real Projects."*

---

# ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub.

---

<div align="center">

### Made with ❤️ by **Arshdeep Singh**

</div>
