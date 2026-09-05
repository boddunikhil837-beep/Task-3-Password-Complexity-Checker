# 🔐 Password Complexity Checker

## 📌 Project Overview

**Password Complexity Checker** is a Python-based cybersecurity project that checks how strong or weak a password is.

The program analyzes a password based on different security rules such as **length, uppercase letters, lowercase letters, numbers, and special characters**.

## 🎯 Objectives

* Understand password security.
* Check the strength of a password.
* Identify weak password characteristics.
* Encourage users to create stronger passwords.
* Learn basic Python string validation.

## 🛠️ Technologies Used

* **Python 3**
* **Regular Expressions (re)**

## 📂 Project Structure

```text
Password-Complexity-Checker/
│
├── password_checker.py
└── README.md
```

## ⚙️ How It Works

The program checks whether the password contains:

* ✅ Minimum required length
* ✅ Uppercase letters (`A-Z`)
* ✅ Lowercase letters (`a-z`)
* ✅ Numbers (`0-9`)
* ✅ Special characters (`@, #, $, %, !`, etc.)

### Password Strength

The password is classified as:

```text
Weak
Medium
Strong
```

## 🔄 Working Process

```text
Enter Password
      ↓
Check Password Length
      ↓
Check Uppercase Letter
      ↓
Check Lowercase Letter
      ↓
Check Number
      ↓
Check Special Character
      ↓
Calculate Strength
      ↓
Display Result
```

## 📥 Installation

Make sure **Python 3** is installed on your computer.

No external libraries are required because the project uses Python's built-in `re` module.

## ▶️ How to Run

Open the project folder in a terminal and run:

```bash
python password_checker.py
```

## 💻 Example Output

```text
Enter your password: Hello@123

Password Strength: Strong
```

Another example:

```text
Enter your password: hello

Password Strength: Weak
```

## 🔒 Security Features

* Checks password length.
* Detects uppercase characters.
* Detects lowercase characters.
* Detects numbers.
* Detects special characters.
* Provides a simple strength rating.

## 🚀 Future Improvements

* Add a password generator.
* Detect commonly used passwords.
* Check passwords against leaked-password databases.
* Add a graphical user interface (GUI).
* Provide suggestions for improving weak passwords.

## 👨‍💻 Author

**Nikhil Boddu**

## 📄 License

This project is created for **educational and cybersecurity learning purposes**.
