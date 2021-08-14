"""
Primitive Data Types
"""

name = "Bob"         # Storing a String value
age = 35             # Storing an Integer value
cash = 100.25        # Storing a Float value
retired = False      # Storing a Boolean value

# How to know the Data Type of a variable
# Invoking the function 'type(<VARIABLE NAME>)'

print("Data Type of the variable 'name' is", type(name))
print("Data Type of the variable 'age' is", type(age))
print("Data Type of the variable 'cash' is", type(cash))
print("Data Type of the variable 'retired' is", type(retired))

# Composite data types

nucamp_locations = ["Seattle", "Tacoma", "Bellevue"]    # List
Bob_Info = {"name": "Bob", "age": 35, "cash": 100.25,
            "retired": False}                           # Dictionary
my_tuple = ("apple", "banana", "cherry")                # Tuple
my_set = {"cats", "dogs", "birds"}                      # Set
