from services.operations import Operations

class Calculator:
    def __init__(self):
        self.operand1 = "0"

    def get_operand1(self):
        return str(self.operand1)

    def set_operand1(self,number:str):
        self.operand1 = number

    def count_two_operands(self, operator:str, operand2:str):
        if operator == "+":
            self.operand1 = Operations.sum_func(self,self.operand1,operand2)
        if operator == "-":
            self.operand1  = Operations.sub_func(self,self.operand1,operand2)
        if operator == "*":
            self.operand1  = Operations.mul_func(self,self.operand1,operand2)
        if operator == "/":
            self.operand1  = Operations.div_func(self,self.operand1,operand2)
        return self.operand1

    def count_one_operands(self,operator: str):
        if operator == "e":
            self.operand1 = Operations.exp_func(self,self.operand1)
        if operator == "sq":
            self.operand1 = Operations.sqrt_func(self,self.operand1)
        return self.operand1
