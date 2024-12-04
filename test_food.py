import unittest
from food import Food

class TestFood(unittest.TestCase):
    def setUp(self):
        self.food = Food(type='onion rings')

    def test_initilization(self):
        self.assertEqual(self.food.get_type(), 'onion rings')
        self.assertEqual(self.food.get_total(), 1.75)

    def test_add_topping(self):
        self.food.add_topping('whipped cream')
        self.assertIn('whipped cream', self.food.get_toppings())
        self.assertEqual(self.food.get_total(), 1.75)

if __name__ == '__main__':
    unittest.main()