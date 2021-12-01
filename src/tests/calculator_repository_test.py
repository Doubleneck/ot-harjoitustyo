import unittest
from services.calculator_service import CalculatorService
from repositories.calculator_repository import CalculatorRepository
from database_connection import get_database_connection

class TestCalculatorService(unittest.TestCase):
    
    def setUp(self):
        connection = get_database_connection()
        self.calculator = CalculatorService()
        self.repository = CalculatorRepository(connection)
        self.calculator.set_operand1("16")

    def database_works_and_initialized(self):
        self.assertEqual(self.repository.stats(), (0,0,0,0,0,0,0))    