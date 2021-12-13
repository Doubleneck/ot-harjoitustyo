from math import sqrt, radians, sin, cos, tan

class OperationsService:
    ''' Laskinpalvelun operaatioista vastaava konstruktoriton luokka '''

    def sum_func(self, number1:str, number2:str):
        return str(float(number1)+float(number2))

    def sub_func(self, number1:str, number2:str):
        return str(float(number1) - float(number2))

    def mul_func(self, number1:str, number2:str):
        return str(float(number1) * float(number2))

    def div_func(self, number1:str, number2:str):
        '''Laskee jakolaskun

            Args:
                number1: merkkijono jaettava
                number2: merkkijono jakaja
            Returns:
                merkkijonomuotoinen laskutoimituksen tulos, tai jos jakaja on 0,
                virheilmoitus.
        '''
        ret = "error div zero"
        if float(number2) != 0.0:
            ret = str(float(number1) / float(number2))
        return ret

    def percent_func(self, number1:str, number2:str):
        '''Laskee kuinka monta prosenttia ensimmäinen operandi on toisesta'''

        return str((float(number2)/100)*float(number1))

    def exp_func(self, number1:str):
        '''Laskee toisen potenssin'''
        return str(float(number1) * float(number1))

    def sqrt_func(self, number1:str):
        '''Laskee neliöjuuren

            Arg:
                number1: merkkijono operandi, josta neliöjuuri lasketaan
            Returns:
                merkkijonomuotoinen laskutoimituksen tulos, tai jos operandi on pienempi kuin 0,
                virheilmoitus.
        '''
        ret = "error sqrt not defined for negative"
        if float(number1) >= 0:
            ret = str(sqrt(float(number1)))
        return ret

    def sin_func(self, number1:str):
        return str(round(sin(radians(float(number1))),8))

    def cos_func(self, number1:str):
        return str(round(cos(radians(float(number1))),8))

    def tan_func(self, number1:str):
        return str(round(tan(radians(float(number1))),8))
