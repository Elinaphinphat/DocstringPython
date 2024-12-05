"""
Unit testing for the IceStorm Class.
"""

import unittest # Imports the unittest module for making tests.
from module.ice_storm import IceStorm # Fice_storm ood class imported from the IceStorm module.

class TestIceStorm(unittest.TestCase):
    def setUp(self):
        self.ice_storm_mint = IceStorm("mint chocolate chip")
    
    def test_flavors_toppings(self):
        self.assertEqual(self.ice_storm_mint.get_flavors(), "mint chocolate chip")
        self.assertEqual(self.ice_storm_mint.get_total(), 4.00)

        self.ice_storm_mint.add_topping('dig dogs')
        self.ice_storm_mint.add_topping('pecans')

        self.assertEqual(self.ice_storm_mint.get_total(), 5.50)



if __name__ == '__main__':
    unittest.main()