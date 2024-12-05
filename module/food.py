class Food:
    #Defines food.
    _food_price = {
        "hotdog": 2.30,
        "corndog": 2.00,
        "ice cream": 3.00,
        "onion rings": 1.75,
        "french fries": 1.50,
        "tator tots": 1.70,
        "nacho chips": 1.90
    } #Defines toppings.
    _topping_prices = {
        "cherry": 0.00,
        "whipped cream": 0.00,
        "caramel sauce": 0.50,
        "chocolate sauce": 0.50,
        "nacho cheese": 0.30,
        "chili": 0.60,
        "bacon bits": 0.30,
        "ketchup": 0.00,
        "mustard": 0.00
    }

    def __init__(self, type, price=None):
        """
        Food object is initialized with a type and base price.

        Args:
            type (str): Type of food.
            price (float, optional): Base price of the food. Defaults to None.

        Raises:
            ValueError: If the food type is not valid.
        """
        if type.lower() not in self._food_price:
            raise ValueError("Invalid food type.")
        self._type = type.lower()
        self._toppings = set()
        self._base_price = self._food_price[self._type] if price is None else price
        self._total_price = self._base_price

    def get_base_price(self):
        """
        Gets the food's base price.

        Returns:
            float: The base price of the food.
        """
        return self._base_price
    
    def get_type(self):
        """
        Gets the type of food.

        Returns:
            str: Food type.
        """
        return self._type
    
    def add_topping(self, topping):
        """
        Allows toppings to be added to the food.

        Args:
            topping (str): Adds a topping to the food.

        Raises:
            ValueError: If the topping is not valid.
        """
        if topping.lower() not in self._topping_prices:
            raise ValueError("Invalid Topping.")
        self._toppings.add(topping.lower())
        self._total_price += self._topping_prices[topping.lower()]

    def get_toppings(self):
        """
        Gets a list of toppings that could be added.

        Returns:
            list: The list of toppings.
        """
        return list(self._toppings)
    
    def get_num_toppings(self):
        """
        Gets the number of toppings.

        Returns:
            int: The number of toppings available.
        """
        return len(self._toppings)
    
    def get_total(self):
        """
        Calculates the total price of food and toppings.

        Returns:
            float: Price of food and toppings together.
        """
        toppings_cost = sum(self._topping_prices[topping] for topping in self._toppings)
        return self._base_price + toppings_cost
    
    def __str__(self):
        """
        Provides a string that represents the food item.

        Returns:
            str: A string that showcases the food item.
        """
        return f'Food Type: {self._type}, Toppings: {self._toppings}, Price: ${self.get_total():.2f}'