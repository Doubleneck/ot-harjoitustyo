import unittest
from services.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()
        self.calculator.set_operand1(16)

    def test_hello_world(self):
        self.assertEqual("Hello world", "Hello world")

    def test_add_positive_integer(self):        
        self.assertEqual(self.calculator.count_two_operands("+",5), "21.0")    

    def test_sub_positive_integer(self):        
        self.assertEqual(self.calculator.count_two_operands("-",5), "11.0")  

    def test_div_positive_integer(self):        
        self.assertEqual(self.calculator.count_two_operands("/",8), "2.0")     

    def test_sq(self):        
        self.assertEqual(self.calculator.count_one_operands("sq"), "4.0")      