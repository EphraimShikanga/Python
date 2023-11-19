class Calculator:
    def __init__(self):
        self.num1 = None
        self.num2 = None
        self.operator = None
        self.validOperators = ["+", "-", "*", "/"]

    def get_operator(self):
        while True:
            try:
                self.operator = input("Enter the operator (+, -, *, /): ")
                if self.operator not in self.validOperators:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a valid operator.")
    
    def get_num1(self):
        while True:
            try:
                self.num1 = float(input("Enter the first number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def get_num2(self):
        while True:
            try:
                self.num2 = float(input("Enter the second number: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")


    def get_user_input(self):
        self.get_num1()
        self.get_num2()
        self.get_operator()
        
    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        try:
            return self.num1 / self.num2
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")
            return None

    def calculate(self):
        if self.operator == "+":
            return self.add()
        elif self.operator == "-":
            return self.subtract()
        elif self.operator == "*":
            return self.multiply()
        elif self.operator == "/":
            return self.divide()

    def run(self):
        self.get_user_input()
        print("Answer:", self.calculate())


calculator = Calculator()
calculator.run()