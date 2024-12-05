class IceStorm:
    """
    IceStorm class with ice cream flavors and toppings.
    """
    _flavor_price = {
        "mint chocolate chip": 4.00,
        "chocolate": 3.00,
        "vanilla bean": 3.00,
        "banana": 3.50,
        "butter pecan": 3.50,
        "s'more": 4.00
    } # Flavor prices with a list of ice cream flavors.
    _topping_price = {
        "cherry": 0.00,
        "whipped cream": 0.00,
        "caramel sauce": 0.50,
        "storios": 1.00,
        "dig dogs": 1.00,
        "t&t's": 1.00,
        "cookie dough": 1.00,
        "pecans": 0.50
    } # Toppings prices with a list of various add-ons.

    def __init__(self, flavor, price=None):
        """
        Initializes IceStorm with a flavor and base price.

        Args:
            flavor (str): The ice cream flavor.
            price (float, optional): The ice cream price.. Defaults to None.

        Raises:
            ValueError: Invalid flavor choice.
        """
        if flavor.lower() not in self._flavor_price:
            raise ValueError("Invalid Flavor.")
        self._flavor = flavor.lower()
        self._toppings = set()
        self._base_price = self._flavor_price[self._flavor] if price is None else price
        self._total_price = self._base_price

    def get_flavors(self):
        """
        Makes the base flavor for the ice cream.

        Returns:
            str: The ice cream flavor.
        """
        return self._flavor
    
    def add_flavor(self, flavor):
        """
        Adds flavors to the ice storm.

        Args:
            flavor (str): A new base flavor.

        Raises:
            ValueError: Invalid flavor choice.
        """
        if flavor.lower() not in self._flavor_price:
            raise ValueError("Invalid Flavor.")
        self._base_price = self._flavor_price[self._flavor]
        self._total_price = self._base_price + sum(self._topping_price[topping] for topping in self._toppings)

    def get_base(self):
        """
        Grabs the current base flavor of the ice cream.

        Returns:
            str: The base flavor of the ice cream.
        """
        return self._flavor
    
    def get_total(self):
        """
        Calculates the total of ice cream and toppings together.

        Returns:
            float: The total price of everything together.
        """
        return self._total_price
    
    def get_num_flavors(self):
        """
        Gets the number of toppings added.

        Returns:
            int: The mount of toppings.
        """
        return len(self._toppings) 
    
    def add_topping(self, topping):
        """
        Adds toppings to the ice cream.

        Args:
            topping (str): Toppings that are going to be added.

        Raises:
            ValueError: Invalid topping choice.
        """
        if topping.lower() not in self._topping_price:
            raise ValueError("Invalid Topping.")
        self._toppings.add(topping.lower())
        self._total_price += self._topping_price[topping.lower()]
    
    def __str__(self):
        """
        Converts everything into a representable receipt.

        Returns:
            str: String representation fo the ice storm.
        """
        return f'IceStorm Flavor: {self._flavor}, Toppings: {self._toppings}, Price: ${self.get_total():.2f}'
