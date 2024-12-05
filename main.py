from module.drink import Drink # Drink class imported from the drink module.
from module.order import Order # Order class imported from the order module.
from module.food import Food # Food class imported from the food module.
from module.ice_storm import IceStorm

drink1 = Drink(base='sprite', price=3.50, size='small') 
# First drink object is created with the base, price, and size.
drink1.add_flavors('lemon') # Lemon flavor added, which also adds a $0.15 increase in price.

drink2 = Drink(base='water', price=6.50, size='large')
# Second drink created with a base, price, and size.
drink2.add_flavors('cherry') # Cherry flavor added which adds a $0.15 increase.
drink2.add_flavors('strawberry') # Strawberry flavor added which adds a $0.15 increase.

# The rest of these are to test the order class to make sure flavors aren't repeated.
drink2.add_flavors('strawberry')
drink2.add_flavors('strawberry')
drink2.add_flavors('strawberry')

# Food order that will print the item and price on the receipt.
food1 = Food(type='onion rings') # Added onions rings which should be $1.75.
food2 = Food(type='nacho chips') # Added nacho chips which should be $1.90.
# Whipped cream as the toppings which should be free.
food1.add_topping('whipped cream') 
food2.add_topping('whipped cream')

ice_storm1 = IceStorm(flavor="mint chocolate chip") # Main flavor is mint chocolate chip.
ice_storm1.add_topping("dig dogs") # dig dogs topping on the side.
ice_storm1.add_topping("pecans") # pecans topping on the side.


order = Order() # Creates an order object for drinks to be added to.
order.add_item(drink1) # Drink1 added to the order.
order.add_item(drink2) # Drink 2 added to the order.
order.add_item(food1) # food 1 added to the order.
order.add_item(food2) # food 2 added to the order.
order.add_item(ice_storm1) # ice_storm 1 added to the order.

print("Item Order:") 
for item in order.get_items():
# Prints the header for the item order.
    print(item) # Prints the item to the console.

print("\nTotal Items:", order.get_num_items())
# Prints the total number of items in the order.

receipt = order.get_receipt() # Main command that will print receipt details.
print("\nReceipt:") # The Receipt Header.
print(f"Items:\n{receipt['items']}") # List of items.
print(f"Number of Items: {receipt['num_items']}") # Number of items.
print(f"Total Before Tax: {receipt['total_before_tax']}") # Total amount before tax.
print(f"Tax: {receipt['tax']}") # Tax amount.
print(f"Total With Tax: {receipt['total_with_tax']}") # Total amount including tax.