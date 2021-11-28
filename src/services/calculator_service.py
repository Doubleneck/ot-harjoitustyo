from services.operations_service import OperationsService
from repositories.calculator_repository import CalculatorRepository
from database_connection import get_database_connection

class CalculatorService:
    def __init__(self):
        self.operand1 = "0"
        self.calculator_repository = CalculatorRepository(get_database_connection())

    def get_operand1(self):
        return str(self.operand1)

    def set_operand1(self,number:str):
        self.operand1 = number

    def count_two_operands(self, operator:str, operand2:str):
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
        if self.operand1 == "":
            self.operand1 = 0
        self.calculator_repository.add_operation(operator)
        if operator == "exp":
            self.operand1 = OperationsService.exp_func(self,self.operand1)
        if operator == "sqrt":
            self.operand1 = OperationsService.sqrt_func(self,self.operand1)
        return self.operand1

    def get_stats(self):
        calculator_repository = CalculatorRepository(get_database_connection())
        return calculator_repository.stats()
