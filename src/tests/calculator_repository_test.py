import unittest
from services.calculator_service import CalculatorService
from repositories.calculator_repository import CalculatorRepository
#from repositories.calculator_repository import calculator_repository
from test_database_connection import get_test_database_connection
#import sqlite3 

class TestCalculatorRepository(unittest.TestCase):

    def setUp(self):
        connection = get_test_database_connection()
#        self.repository(connection)
#        self.calculator = CalculatorService()
#        connection = sqlite3.connect(":memory:")
        self.repository = CalculatorRepository(connection)
        self.repository.create_table_operations()
        self.repository.delete_all()
        self.calculator = CalculatorService()
        self.calculator.set_operand1("16")

    def test_database_works_and_initialized_ok(self):
        self.assertEqual(self.repository.stats(), (0,0,0,0,0,0,0,0,0,0,0))

    def test_database_add_operation(self):
        repository.add_operation("+")
        self.assertEqual(repository.stats(), (1,1,0,0,0,0,0,0,0,0,0))

    def test_database_sub_operation(self):
        repository.add_operation("-")
        self.assertEqual(repository.stats(), (1,0,1,0,0,0,0,0,0,0,0))

    def test_database_div_operation(self):
        repository.add_operation("/")
        self.assertEqual(repository.stats(), (1,0,0,1,0,0,0,0,0,0,0))

    def test_database_mul_operation(self):
        repository.add_operation("*")
        self.assertEqual(repository.stats(), (1,0,0,0,1,0,0,0,0,0,0))

    def test_database_sqrt_operation(self):
        repository.add_operation("sqrt")
        self.assertEqual(repository.stats(), (1,0,0,0,0,1,0,0,0,0,0))

    def test_database_exp_operation(self):
        repository.add_operation("exp")
        self.assertEqual(repository.stats(), (1,0,0,0,0,0,1,0,0,0,0))

    def test_delete_all_works(self):
        repository.add_operation("exp")
        repository.add_operation("sqrt")
        repository.delete_all()
        self.assertEqual(repository.stats(), (0,0,0,0,0,0,0,0,0,0,0))

    def test_database_multiple_operations(self):
        repository.add_operation("+")
        repository.add_operation("+")
        repository.add_operation("-")
        repository.add_operation("/")
        repository.add_operation("/")
        repository.add_operation("*")
        repository.add_operation("sqrt")
        repository.add_operation("exp")
        self.assertEqual(repository.stats(), (8,2,1,2,1,1,1,0,0,0,0))
