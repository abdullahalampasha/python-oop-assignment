# Task 1 - Person Class

class Person:
    name = ""
    gender = ""
    profession = ""
    study_hour = 0

    def working(self):
        print(self.name, "is working.")

    def study(self):
        print(self.name, "is studying.")


person1 = Person()

person1.name = "Ali"
person1.gender = "Male"
person1.profession = "Student"
person1.study_hour = 3

person1.working()
person1.study()


# Task 2 - Student Class

class Student:
    def __init__(self, name, roll_no, program, marks):
        self.name = name
        self.roll_no = roll_no
        self.program = program
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll_no)
        print("Program:", self.program)
        print("Marks:", self.marks)


student1 = Student("Ali", 101, "BSCS", 85)

student1.display()


# Task 3 - Rectangle Class

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print("Area:", area)


rectangle1 = Rectangle(10, 5)
rectangle2 = Rectangle(8, 4)

rectangle1.calculate_area()
rectangle2.calculate_area()


# Task 4 - Bank Account

class BankAccount:
    def __init__(self, account_holder_name, account_number, balance):
        self.account_holder_name = account_holder_name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance.")

    def display_balance(self):
        print("Account Holder:", self.account_holder_name)
        print("Account Number:", self.account_number)
        print("Balance:", self.balance)


account1 = BankAccount("Ali", "1001", 5000)

account1.display_balance()

account1.deposit(2000)

account1.withdraw(1500)

account1.display_balance()