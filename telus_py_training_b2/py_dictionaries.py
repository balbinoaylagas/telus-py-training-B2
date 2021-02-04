"""
Python Dictionaries
"""

# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# A dictionary is a collection which is unordered, changeable and does not allow duplicates.

# Dictionaries are written with curly brackets, and have keys and values:

# Create and print a dictionary:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print()
print(thisdict)


# Dictionary Items
# Dictionary items are unordered, changeable, and does not allow duplicates.

# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

# Print the "brand" value of the dictionary:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print()
print(thisdict["brand"])


# Unordered
# When we say that dictionaries are unordered, it means that the items does not have a defined order, you cannot refer to an item by using an index.

# Changeable
# Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

# Duplicates Not Allowed
# Dictionaries cannot have two items with the same key:

# Duplicate values will overwrite existing values:
# this code gives an error
"""
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964, "year": 2020}
print()
print(thisdict)
"""


# Dictionary Length
# To determine how many items a dictionary has, use the len() function:
# Print the number of items in the dictionary:
print()
print(len(thisdict))


# Dictionary Items - Data Types
# The values in dictionary items can be of any data type:
# String, int, boolean, and list data types:
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"],
}
print()
print(thisdict)


# type()
# From Python's perspective, dictionaries are defined as objects with the data type 'dict':

# <class 'dict'>
# Print the data type of a dictionary:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print()
print(type(thisdict))


# Accessing Items
# You can access the items of a dictionary by referring to its key name, inside square brackets:
# Get the value of the "model" key:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = thisdict["model"]
print()
print(x)


# There is also a method called get() that will give you the same result:
# Get the value of the "model" key:
x = thisdict.get("model")
print()
print(x)


# Get Keys
# The keys() method will return a list of all the keys in the dictionary.
# Get a list of the keys:
x = thisdict.keys()
print()
print(x)


# The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary
#   will be reflected in the keys list.
# Add a new item to the original dictionary, and see that the value list gets updated as well:
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.keys()
print()
print(x)  # before the change
car["color"] = "white"
print(x)  # after the change


# Get Values
# The values() method will return a list of all the values in the dictionary.
# Get a list of the values:
x = thisdict.values()
print()
print(x)


# The list of the values is a view of the dictionary, meaning that any changes done to the dictionary
#   will be reflected in the values list.
# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.values()
print()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change


# Get Items
# The items() method will return each item in a dictionary, as tuples in a list.
# Get a list of the key:value pairs
x = thisdict.items()
print()
print(x)


# The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary
#   will be reflected in the items list.
# Add a new item to the original dictionary, and see that the items list gets updated as well:
car = {"brand": "Ford", "model": "Mustang", "year": 1964}
x = car.items()
print()
print(x)  # before the change
car["year"] = 2020
print(x)  # after the change


# Check if Key Exists
# To determine if a specified key is present in a dictionary use the in keyword:
# Check if "model" is present in the dictionary:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print()
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")


# Change Values
# You can change the value of a specific item by referring to its key name:
# Change the "year" to 2018:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["year"] = 2018
print()
print(thisdict)

# Update Dictionary
# The update() method will update the dictionary with the items from the given argument.

# The argument must be a dictionary, or an iterable object with key:value pairs.
# Update the "year" of the car by using the update() method:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"year": 2020})
print()
print(thisdict)

# Adding Items
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict["color"] = "red"
print()
print(thisdict)

# Update Dictionary
# The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.

# The argument must be a dictionary, or an iterable object with key:value pairs.
# Add a color item to the dictionary by using the update() method:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.update({"color": "red"})
print()
print(thisdict)


# Removing Items
# There are several methods to remove items from a dictionary:
# The pop() method removes the item with the specified key name:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.pop("model")
print()
print(thisdict)


# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.popitem()
print()
print(thisdict)


# The del keyword removes the item with the specified key name:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict["model"]
print()
print(thisdict)


# The del keyword can also delete the dictionary completely:
"""
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
del thisdict
print()
print(thisdict)  # this will cause an error because "thisdict" no longer exists.
"""

# The clear() method empties the dictionary:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
thisdict.clear()
print()
print(thisdict)


# Loop Through a Dictionary
# You can loop through a dictionary by using a for loop.

# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.

# Print all key names in the dictionary, one by one:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print()
for x in thisdict:
    print(x)


# Print all values in the dictionary, one by one:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print()
for x in thisdict:
    print(thisdict[x])


# You can also use the values() method to return values of a dictionary:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print()
for x in thisdict.values():
    print(x)


# You can use the keys() method to return the keys of a dictionary:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print()
for x in thisdict.keys():
    print(x)


# Loop through both keys and values, by using the items() method:
thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print()
for x, y in thisdict.items():
    print(x, y)
