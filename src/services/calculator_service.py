from services.operations_service import OperationsService
from repositories.calculator_repository import CalculatorRepository
from database_connection import get_database_connection

class CalculatorService:
    """Sovelluslogiikasta vastaava luokka."""

    def __init__(self):
        self.operand1 = "0"
        self.calculator_repository = CalculatorRepository(get_database_connection())
        self.memory = "0"

        """Luokan konstruktori. Luo uuden sovelluslogiikasta vastaavan palvelun.

        Args:
            operand1:
                Laskinsovelluksen ensimmäinen operandi, joka tallennetaan laskimeen joko
                laskun tuloksena tai kahden muuttujan operaatiossa ensimmäiseksi operandiksi.
            calculator_repository:
                CalculatorRepository - olio, jolla on luokkaa vastaavat metodit
            memory:
                Laskinsovelluksen sisäinen muistipaikka.
        """

    def get_operand1(self):
        return self.operand1

    def set_operand1(self,number:str):
        self.operand1 = number

    def get_memory(self):
        return self.memory

    def set_memory(self,number:str):
        self.memory = number

    def count_two_operands(self, operator:str, operand2:str):
        """ Suorittaa kaksipaikkaisen laskuoperaation ja lisää operaation tietokantaan.
            Laskimen Operand1 on ensimmäinen argumentti.

        Args:
            operator:
                Merkkijono tai merkki, joka kuvaa operaatiota.
            operand2:
                Jälkimmäinen operandi.
        """

        if self.operand1 == "":
            self.operand1 = 0
        self.calculator_repository.add_operation(operator)
        if operator == "+":
            self.operand1 = OperationsService.sum_func(self,self.operand1,operand2)
        if operator == "-":
            self.operand1 = OperationsService.sub_func(self,self.operand1,operand2)
        if operator == "*":
            self.operand1 = OperationsService.mul_func(self,self.operand1,operand2)
        if operator == "/":
            self.operand1 = OperationsService.div_func(self,self.operand1,operand2)
        return self.operand1

    def count_one_operands(self, operator:str):
        """ Suorittaa yksipaikkaisen laskuoperaation ja lisää operaation tietokantaan.
            Laskimen operand1 toimii argumenttina.

        Args:
            operator:
                Merkkijono tai merkki, joka kuvaa operaatiota.
        """

        if self.operand1 == "":
            self.operand1 = 0
        self.calculator_repository.add_operation(operator)
        if operator == "exp":
            self.operand1 = OperationsService.exp_func(self,self.operand1)
        if operator == "sqrt":
            self.operand1 = OperationsService.sqrt_func(self,self.operand1)
        if operator == "sin":
            self.operand1 = OperationsService.sin_func(self,self.operand1)
        if operator == "cos":
            self.operand1 = OperationsService.cos_func(self,self.operand1)
        if operator == "tan":
            self.operand1 = OperationsService.tan_func(self,self.operand1)
        return self.operand1

    def get_stats(self):
        calculator_repository = CalculatorRepository(get_database_connection())
        return calculator_repository.stats()
