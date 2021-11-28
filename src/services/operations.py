from math import sqrt

class Operations:

    def sum_func(self, number1:str, number2:str):
        return str(float(number1)+float(number2))

    def sub_func(self, number1:str, number2:str):
        return str(float(number1) - float(number2))

    def mul_func(self, number1:str, number2:str):
        return str(float(number1) * float(number2))

    def div_func(self, number1:str, number2:str):
        try:
            return str(float(number1) / float(number2))
        except ZeroDivisionError:
            return "error div zero"

    def exp_func(self, number1:str):
        return str(float(number1) * float(number1))

    def sqrt_func(self, number1:str):
        try:
            return str(sqrt(float(number1)))
        except ValueError:
            return "error sqrt not defined for negative"
        

