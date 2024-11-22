"""
Unit tests for the Drink class.
"""

import unittest # Imports from unittest for making tests.
from drink import Drink # Imports the drink class from the Drink Module.

class TestDrink(unittest.TestCase):
    """
    Unit test class for the Drink Class.
    """
    def setUp(self):
        """
        Sets up the test by adding in drink attributes.
        """
        self.drink = Drink(base='sprite', price=3.50, size='small')
        
    def test_add_and_get_flavors(self): 
        """
        Tests the add flavors and get flavors methods by adding flavors.
        """
        self.drink.add_flavors('strawberry') 
        self.assertEqual(self.drink.get_flavors(), ['strawberry'])

    def test__get_num_flavors(self):
        """
        A test to make sure flavors are being counted.
        """
        self.drink.add_flavors('strawberry') 
        self.assertEqual(self.drink.get_num_flavors(), 1)

    def test_get_base(self):
        """
        Test to make sure the base is being added correctly.
        """
        self.assertEqual(self.drink.get_base(), 'sprite')

    def test_get_total(self):
        """
        Tests the get_total method by making sure the flavor cost is being implemneted.
        """
        self.assertEqual(self.drink.get_total(), 1.50)
        self.drink.add_flavors('strawberry') 
        self.assertEqual(self.drink.get_total(), 1.65)

    def test_set_and_get_size(self):
        """
        Tests the set_size and get_size by adding the size and cost of size.
        """
        self.drink.set_size('mega')
        self.assertEqual(self.drink.get_total(), 2.50)

if __name__ == '__main__':
    unittest.main()
