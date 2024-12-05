"""
Unit testing for the Order Class.
"""

import unittest # Imports the unittest module for making tests.
from module.order import Order # Imports the order class from the Order Module.
from module.drink import Drink # Imports the drink class from the Drink Module.

class TestOrder(unittest.TestCase):
    """
    Unit test for the Order class.
    """
    def setUp(self):
        """
        Creates an order and two drinks for testing.
        """
        self.order = Order()
        self.drink1 = Drink(base='sprite', price=3.50, size='small')
        self.drink2 = Drink(base='water', price=5.50, size='mega')
    
    def test_get_items(self):
        """
        Tests the get_items method by adding a drink and adding it to the order.
        """
        self.order.add_item(self.drink1)
        items = self.order.get_items()
        self.assertTrue(self.drink1 in items)
        
    def test_add_item(self):
        """
        Test to make sure drinks are being added to the order.
        """
        self.order.add_item(self.drink1)
        self.assertIn(self.drink1, self.order.get_items())

    def test_get_totals(self):
        """
        Tests both get_total and get_total_with_tax to make sure costs and tax costs are calculated properly.
        """
        self.order.add_item(self.drink1)
        self.order.add_item(self.drink2)
        expected_total = self.drink1.get_total() + self.drink2.get_total()
        self.assertEqual(self.order.get_total(), expected_total)
        expected_total_with_tax = expected_total+ (expected_total * Order.tax_rate)
        self.assertEqual(self.order.get_total_with_tax(), expected_total_with_tax)

    def test_get_num_items(self):
        """
        Tests to see if the drink items are being counted.
        """
        self.order.add_item(self.drink1)
        self.assertEqual(self.order.get_num_items(), "Item Total: 1")

    def test_get_receipt(self):
        """
        A test that makes sure receipt details are implemented properly.
        """
        self.order.add_item(self.drink1)
        self.order.add_item(self.drink2)
        total = self.order.get_total()
        total_with_tax = self.order.get_total_with_tax()
        tax = total_with_tax - total
        expected_receipt = {
            'items': f"{self.drink1}, {self.drink2}",
            'total_before_tax': f"${total:.2f}",
            'tax': f"${tax:.2f}",
            'total_with_tax': f"{total_with_tax:.2f}"
        }
        
if __name__ == '__main__':
    unittest.main()