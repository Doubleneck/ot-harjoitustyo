from services.operations import Operations

class Calculator:
    # Konstruktori
    def __init__(self):
        pass

    def count(number1: str, operator: str,number2:str):
        operand1=float(number1)
        operand2=float(number2)
        if operator == "+":
            result = Operations.sum_func(operand1,operand2)
        if operator == "-":
            result = Operations.sub_func(number1,number2)
        if operator == "*":
            result = Operations.mul_func(number1,number2)
        if operator == "/":
            result = Operations.div_func(number1,number2) 
            
        else:
            if operator == "e":   
                result = Operations.exp_func(number1)
            if operator == "sq": 
                result = Operations.sqrt_func(number1)    
        return result    