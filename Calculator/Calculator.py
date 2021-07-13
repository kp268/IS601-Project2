from Calculator.Multiplication import multiply
from Calculator.Division import divide
from Calculator.Addition import add
from Calculator.Subtraction import subtract
from Calculator.Square import squarefunc
from Calculator.SquareRoot import squarerootfunc

class Calculator:
    result = 0
    data = []

    def __init__(self):
        pass

    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def divide(self, a, b):
        self.result = round(divide(a, b), 9)
        return self.result

    def add(self, a, b):
        self.result = add(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtract(a, b)
        return self.result

    def square(self, a):
        self.result = squarefunc(a)
        return self.result

    def square_root(self, a):
        self.result = round(squarerootfunc(a), 8)
        return self.result