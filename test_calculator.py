'''
    Unit tests for the calculator library. 
'''
from calculator import add, subtract

class TestCalculator:


    def test_addition(self):
        assert 15 == add(5,10)

    def test_subtraction(self):
        assert 10 == subtract(15,5)