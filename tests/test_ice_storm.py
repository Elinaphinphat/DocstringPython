"""
Unit testing for the IceStorm Class.
"""

import unittest # Imports the unittest module for making tests.
from module.ice_storm import IceStorm # Fice_storm ood class imported from the IceStorm module.

class TestIceStorm(unittest.TestCase):
    """
    sets up a IceStorm instance.
    """
    def setUp(self):
        self.ice_storm_mint = IceStorm("mint chocolate chip") # Creating a flavor to add toppings to.
    
    def test_flavors_toppings(self):
        self.assertEqual(self.ice_storm_mint.get_flavors(), "mint chocolate chip") # Added the flavor.
        self.assertEqual(self.ice_storm_mint.get_total(), 4.00) # Making sure the base price is set.

        self.ice_storm_mint.add_topping('dig dogs') 
        self.ice_storm_mint.add_topping('pecans')
        # Added both toppings to the ice cream.

        self.assertEqual(self.ice_storm_mint.get_total(), 5.50) 
        # Final price is verified to ensure toppings are implemented.

if __name__ == '__main__':
    unittest.main()