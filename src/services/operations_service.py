from math import sqrt

class OperationsService:
    """ Laskinpalvelun operaatioista vastaava konstruktoriton luokka"""

    def sum_func(self, number1:str, number2:str):
        return str(float(number1)+float(number2))

    def sub_func(self, number1:str, number2:str):
        return str(float(number1) - float(number2))

    def mul_func(self, number1:str, number2:str):
        return str(float(number1) * float(number2))

    def div_func(self, number1:str, number2:str):
        ret = "error div zero"
        if number2 != "0":
            ret = str(float(number1) / float(number2))
        return ret

    def exp_func(self, number1:str):
        return str(float(number1) * float(number1))

    def sqrt_func(self, number1:str):
        ret = "error sqrt not defined for negative"
        if float(number1) >= 0:
            ret = str(sqrt(float(number1)))
        return ret
