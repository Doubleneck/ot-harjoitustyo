from services.operations import Operations
from repositories.calculator_repository import CalculatorRepository
from database_connection import get_database_connection

class Calculator:
    def __init__(self):
        self.operand1 = "0"
        self.calculator_repository = CalculatorRepository(get_database_connection())
    def get_operand1(self):
        return str(self.operand1)

    def set_operand1(self,number:str):
        self.operand1 = number

    def count_two_operands(self, operator:str, operand2:str):
        
        self.calculator_repository.add_operation(operator)
        if operator == "+":            
            self.operand1 = Operations.sum_func(self,self.operand1,operand2)
        if operator == "-":
            self.operand1  = Operations.sub_func(self,self.operand1,operand2)
        if operator == "*":
            self.operand1  = Operations.mul_func(self,self.operand1,operand2)
        if operator == "/":
            self.operand1  = Operations.div_func(self,self.operand1,operand2)
        return self.operand1

    def count_one_operands(self, operator:str):
        self.calculator_repository.add_operation(operator)
        if operator == "exp":
            self.operand1 = Operations.exp_func(self,self.operand1)
        if operator == "sqrt":
            self.operand1 = Operations.sqrt_func(self,self.operand1)
        return self.operand1

    def get_stats(self):
        calculator_repository = CalculatorRepository(get_database_connection())
        calculator_repository.stats()
        
        