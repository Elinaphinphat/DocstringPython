"""
Module is used to handle items, calculate prices, and make receipts.
"""

class Order: 
    """
     Order class that represents the drink items.
    """
    tax_rate = 0.0725 # Tax rate that is added to the order cost.

    def __init__(self): 
        """
        Initializes empty order.
        """
        self.__items = [] 

    def get_items(self): 
        """
        Gets the list of items.

        Returns:
            List: The list of drinks items in the order.
        """
        return self.__items
    
    def add_item(self, item):
        """
        This adds drinks to to the order using append.

        Args:
            drink (Drink): Drink item chosen to be added.
        """
        self.__items.append(item)

    def get_total(self):
        """
        Calculates the total price without tax.

        Returns:
            float: Total price of the order.
        """
        total = sum(item.get_total() for item in self.__items)
        return total

    def get_total_with_tax(self):
        """
        Calculates the total cost of all drinks ordered with tax.

        Returns:
            float: The total cost of the order with tax.
        """
        total = self.get_total()
        tax = total * self.tax_rate
        return total + tax

    def get_num_items(self):
        """
        Gets the total amount of items in the order.

        Returns:
            str: The total amount of items.
        """
        num_items = len(self.__items) 
        return f"Item Total: {num_items}"

    def get_receipt(self):
        """
        Creates a receipt for the entire order.

        Returns:
            dict: Receipt details.
        """
        receipt = "\n".join([str(item) for item in self.__items])
        total = self.get_total()
        total_with_tax = self.get_total_with_tax()
        tax = total_with_tax - total
        return {
            'items': receipt,
            'num_items': len(self.__items),
            'total_before_tax': f"${total:.2f}",
            'tax': f"${tax:.2f}",
            'total_with_tax': f"${total_with_tax:.2f}"

        }

    def remove_item(self, index):
        """
        Removes an item from the order.

        Args:
            Self (Order): The instance of the Order class.
            index (int): The index of the item being removed.

        Raises:
            IndexError: If index can't be removed.
        """
        if 0 <= index < len(self.__items):
            self.__items.pop(index)
        else:
            raise IndexError("Invalid, can't be removed.")

    def __str__(self):
        """
        Gets a represtentation of the order.

        Returns:
            str: That represents the order.
        """
        return f'Order(items={self.__items})'
