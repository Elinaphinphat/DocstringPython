"""
Unit testing for the Food Class.
"""

import unittest # Imports the unittest module for making tests.
from food import Food # Food class imported from the food module.

class TestFood(unittest.TestCase):
    """
    Sets up a Food instance.
    """
    def setUp(self):
        self.food = Food(type='onion rings') # Testing one of the food from Food.py.

    def test_initilization(self):
        """
        Tests the food initilization process and then verifies the food price and status.
        """
        self.assertEqual(self.food.get_type(), 'onion rings') # Grabbing onion rings from the list.
        self.assertEqual(self.food.get_total(), 1.75) # Testing to make sure the correct price is added.

    def test_add_topping(self):
        """
        Testing the add topping process and makes sure that price and status are valid.
        """
        self.food.add_topping('whipped cream') # The topping added is whipped cream.
        self.assertIn('whipped cream', self.food.get_toppings()) # Pushes whipped cream into the order.
        self.assertEqual(self.food.get_total(), 1.75) # Validates the price of the topping.

if __name__ == '__main__':
    unittest.main()