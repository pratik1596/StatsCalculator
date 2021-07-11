from Calculator.Addition import addition
from Calculator.Subtraction import subtraction
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Square import square
from Calculator.SquareRoot import sroot

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, value1, value2):
        self.result = addition(value1, value2)
        return self.result

    def sub(self, value1, value2):
        self.result = subtraction(value1, value2)
        return self.result

    def mul(self, value1, value2):
        self.result = multiplication(value1, value2)
        return self.result

    def div(self, value1, value2):
        self.result = division(value1, value2)
        return self.result

    def sq(self, value1):
        self.result = square(value1)
        return self.result

    def sqroot(self, value1):
        self.result = sroot(value1)
        return self.result
