"""Instantiating A Class."""

# This is where we instantiate the class we defined in classes.py
# In other words, we're creating objects that belong to that class.

# import the class
# from <file_name>.<module_name> import <class_
from lessons.classes.pizza import Pizza

my_pizza: Pizza = Pizza("large", 10, True) # CONSTRUCTOR

# accessing/setting attributes (use this syntax to modify attributes. 
# If variable of class Pizza doesn't include any parameters and the __init__ function is not defined in the class,
# then can also use this syntax to set the attribute values
# my_pizza.size = "large"
# my_pizza.toppings = 10
# my_pizza.gluten_free = True

print("Size Attribute:")
print(my_pizza.size)

print("Toppings:")
print(my_pizza.toppings)

#sals_pizza size "medium, 5 toppings, NOT GF"
sals_pizza: Pizza = Pizza("medium", 5, False)
print(sals_pizza.size)

def price(input_pizza: Pizza) -> float:
    """Function to Calculate Price of Pizza."""
    if input_pizza.size == "large":
        price: float = 6.25
    else:
        price: float = 5.00
    price += .75 * input_pizza.toppings
    if input_pizza.gluten_free: # rememebr gluten_free is a bool so this will only proceed if it's true
        price += 1.00
    return price

# Calling price function
print(price(sals_pizza))
print(price(my_pizza))

# Calling price method
print(sals_pizza.price())
print(my_pizza.price())

my_other_pizza: Pizza = my_pizza.make_new_pizza_add_toppings(2)
print(my_other_pizza.toppings)
print(my_pizza.toppings)
