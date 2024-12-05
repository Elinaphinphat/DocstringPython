"""
This module is used to handle drink details like the size, base, and flavor.
"""

from enum import Enum # Imports Enm from enum to create enumerations.
class Size(Enum): 
    SMALL = 1.50 # Price for a small drink.
    MEDIUM = 1.75 # Price for a medium drink.
    LARGE = 2.05 # Price for a large drink.
    MEGA = 2.50 # Price for a mega drink.

class Drink:
    """
    Class that displays the list of bases, flavors, and sizes.

    Attributes:
        valid_bases (list): List of drink bases.
        valid_flavors (list): List of drink flavors.
        _size_costs (dict): Dictionary of various sizes.
    """
    valid_bases = ['water', 'sprite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    valid_flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']
    _size_costs = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.50,
    }

    def __init__(self, base, price, size): 
        """
        Creates a drink object for the base, price, and size.

        Args:
            base (str): The drink base.
            price (float): The drink price.
            size (str): The drink size.

        Raises:
            ValueError: If the base is not valid, a value error is raised.
        """
        if base not in Drink.valid_bases:
            raise ValueError("Invalid.")
        self.__base = base 
        self.__flavors = []
        self.price = price
        self._size = None
        self._cost = 0.0
        self.set_size(size)

    def get_flavors(self):
        """
        Gets the list of flavors to add to the drink.

        Returns:
            list: The list of flavors.
        """
        return list(self.__flavors)

    def get_num_flavors(self):
        """
        Gets the number of flavors that are added to the drink.

        Returns:
            int: The amount of flavors added.
        """
        return len(self.__flavors)

    def get_base(self):
        """
        Gets the base of the drink.

        Returns:
            str: The drink base.
        """
        return self.__base

    def set_base(self, base):
        """
        Sets the base of the drink.

        Args:
            base (str): The chosen drink base.

        Raises:
            ValueError: If a valid base from the list is not picked.
        """
        if base in Drink.valid_bases:
            self._base = base
        else:
            raise ValueError("Pick a valid base using {self._valid_Bases}.")
        
    def get_total(self):
        """
        Gets the total cost of the drink.

        Returns:
            float: The drink's total price.
        """
        return self._cost

    def add_flavors(self, flavor):
        """
        Adds flavors to the drink.

        Args:
            flavor (str): The flavor that's going to be added.

        Raises:
            ValueError: If the flavor chosen is not from the valid list.
        """
        if flavor in Drink.valid_flavors:
            if flavor not in self.__flavors:
                if flavor not in self.__flavors:
                    self._cost += 0.15
                self.__flavors.append(flavor)
        else:
            raise ValueError("Invalid flavor, pick a flavor from {self._valid_flavors}")

    def set_flavors(self, flavors): 
        """
        Sets flavors for the drink.

        Args:
            flavors (list): A list of flavors that can be added.

        Raises:
            ValueError: If the flavor picked is not from the valid list.
        """
        new_flavors = set(flavors) - set(self.__flavors)
        self._cost += 0.15 * len(new_flavors)
        for flavor in flavors:
            if flavor not in Drink.valid_flavors:
                raise ValueError("Invalid flavor, pick a flavor from {self._valid_flavors}")
        self.__flavors = list(set(flavors))

    def set_size(self, size):
        """
        Sets the drink size.

        Args:
            size (str): The size that is going to be set.

        Raises:
            ValueError: If a size not picked from the valid list.
        """
        size = size.lower()
        if size in self._size_costs:
            self._size = size
            self._cost = self._size_costs[size] + 0.15 * len(self.__flavors)
        else:
            raise ValueError(f"Hey, pick the right size.. {size} Choose from {list(self._size_costs.keys())}.")
        
    def get_size(self):
        """
        Gets the drink size.

        Returns:
            str: The size of the drink.
        """
        return self._size

    def __str__(self):
        """
        Gets a string of the drink.

        Returns:
            str: The string representation of the drink.
        """
        return f'Drink base: {self.__base}, Size: {self._size} [+ ${self._size_costs[self._size]:.2f}], Flavors: {self.__flavors} + [$0.15], Price: ${self.get_total():.2f}' 