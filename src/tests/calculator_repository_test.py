import unittest
from services.calculator_service import CalculatorService
from repositories.calculator_repository import CalculatorRepository
from database_connection import get_database_connection

class TestCalculatorRepository(unittest.TestCase):

    def setUp(self):
        connection = get_database_connection()
        self.calculator = CalculatorService()
        self.repository = CalculatorRepository(connection)
        self.repository.delete_all()
        self.calculator.set_operand1("16")

    def test_database_works_and_initialized_ok(self):
        self.assertEqual(self.repository.stats(), (0,0,0,0,0,0,0,0,0,0))

    def test_database_add_operation(self):
        self.repository.add_operation("+")
        self.assertEqual(self.repository.stats(), (1,1,0,0,0,0,0,0,0,0))

    def test_database_sub_operation(self):
        self.repository.add_operation("-")
        self.assertEqual(self.repository.stats(), (1,0,1,0,0,0,0,0,0,0))

    def test_database_div_operation(self):
        self.repository.add_operation("/")
        self.assertEqual(self.repository.stats(), (1,0,0,1,0,0,0,0,0,0))

    def test_database_mul_operation(self):
        self.repository.add_operation("*")
        self.assertEqual(self.repository.stats(), (1,0,0,0,1,0,0,0,0,0))

    def test_database_sqrt_operation(self):
        self.repository.add_operation("sqrt")
        self.assertEqual(self.repository.stats(), (1,0,0,0,0,1,0,0,0,0))

    def test_database_exp_operation(self):
        self.repository.add_operation("exp")
        self.assertEqual(self.repository.stats(), (1,0,0,0,0,0,1,0,0,0))

    def test_delete_all_works(self):
        self.repository.add_operation("exp")
        self.repository.add_operation("sqrt")
        self.repository.delete_all()
        self.assertEqual(self.repository.stats(), (0,0,0,0,0,0,0,0,0,0))

    def test_database_multiple_operations(self):
        self.repository.add_operation("+")
        self.repository.add_operation("+")
        self.repository.add_operation("-")
        self.repository.add_operation("/")
        self.repository.add_operation("/")
        self.repository.add_operation("*")
        self.repository.add_operation("sqrt")
        self.repository.add_operation("exp")
        self.assertEqual(self.repository.stats(), (8,2,1,2,1,1,1,0,0,0))
