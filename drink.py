from enum import Enum 
class Size(Enum): 
    SMALL = 1.50 
    MEDIUM = 1.75 
    LARGE = 2.05 
    MEGA = 2.50

class Drink:
    valid_bases = ['water', 'sprite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine']
    valid_flavors = ['lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime']
    _size_costs = {
        "small": 1.50,
        "medium": 1.75,
        "large": 2.05,
        "mega": 2.50,
    }
# List of bases and flavors for the drinks.

    def __init__(self, base, price, size): # This is the constructor for the Drink class.
        if base not in Drink.valid_bases:
            raise ValueError("Invalid.")
        self.__base = base # Sets the drink base.
        self.__flavors = [] # Creates an empty list for flavors, hence the empty brackets '[]'.
        self.price = price # Sets the price for drinks.
        self._size = None
        self._cost = 0.0
        self.set_size(size)

    def get_flavors(self):
        return list(self.__flavors)
    # Returns get_flavors, or the list of flavors.

    def get_num_flavors(self):
        return len(self.__flavors)
    # Returns the number of flavors in the drink.

    def get_base(self, base):
        if base in Drink.valid_bases:
            self._base = base
        else:
            raise ValueError("Pick a valid base using {self._valid_Bases}.")
        
    def get_total(self):
        return self._cost

    def add_flavors(self, flavor):
        if flavor in Drink.valid_flavors:
            if flavor not in self.__flavors:
                if flavor not in self.__flavors:
                    self._cost += 0.15
                self.__flavors.append(flavor)
        else:
            raise ValueError("Invalid flavor, pick a flavor from {self._valid_flavors}")
    # This whole method will add flavors to the drinks instead, and will raise a Value error if invalid.

    def set_flavors(self, flavors): 
        new_flavors = set(flavors) - set(self.__flavors)
        self._cost += 0.15 * len(new_flavors)
        for flavor in flavors:
            if flavor not in Drink.valid_flavors:
                raise ValueError("Invalid flavor, pick a flavor from {self._valid_flavors}")
        self.__flavors = list(set(flavors))
    # This whole method will set the flavors for the drinks, and will raise a Value error if invalid.

    def set_size(self, size):
        size = size.lower()
        if size in self._size_costs:
            self._size = size
            self._cost = self._size_costs[size] + 0.15 * len(self.__flavors)
        else:
            raise ValueError(f"Hey, pick the right size.. {size} Choose from {list(self._size_costs.keys())}.")
        
    def get_size(self):
        return self._size

    def __str__(self):
        return f'Drink base: {self.__base}, Size: {self._size} [+ ${self._size_costs[self._size]:.2f}], Flavors: {self.__flavors} + [$0.15], Price: ${self.get_total():.2f}' 