"""
Python Sets
"""

# Sets are used to store multiple items in a single variable.

# Set is one of 4 built-in data types in Python used to store collections of data, the other 3 are List,
#   Tuple, and Dictionary, all with different qualities and usage.

# A set is a collection which is both unordered and unindexed.

# Sets are written with curly brackets.
# Create a Set:
thisset = {"apple", "banana", "cherry"}
print()
print(thisset)


# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

# Set Items
# Set items are unordered, unchangeable, and do not allow duplicate values.
# Unordered
# Unordered means that the items in a set do not have a defined order.
# Set items can appear in a different order every time you use them, and cannot be referred to by index or key.
# Unchangeable
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can add new items.
# Duplicates Not Allowed
# Sets cannot have two items with the same value.

# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print()
print(thisset)


# Get the Length of a Set
# To determine how many items a set has, use the len() method.
# Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print()
print(len(thisset))


# Set Items - Data Types
# Set items can be of any data type:
# String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print()
print(set1)
print(set2)
print(set3)


# A set can contain different data types:
# A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}
print()
print(set1)


# type()
# From Python's perspective, sets are defined as objects with the data type 'set':
# <class 'set'>
# What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print()
print(type(myset))


# The set() Constructor
# It is also possible to use the set() constructor to make a set.
# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print()
print(thisset)


# Access Items
# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop, or ask if a specified value is present
#   in a set, by using the in keyword.
# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
print()
for x in thisset:
    print(x)


# Example
# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print()
print("banana" in thisset)


# Change Items
# Onceaset is created, youcannotchangeitsitems, butyoucanaddnewitems.


# Add Items
# Once a set is created, you cannot change its items, but you can add new items.
# To add one item to a set use the add() method.
# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


# Add Sets
# To add items from another set into the current set, use the update() method.
# Add elements from tropical and thisset into newset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


# Add Any Iterable
# The object in the update() method does not have be a set, it can be any iterable object
#   (tuples, lists, dictionaries et,).
# Add elements of a list to at set:

thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)


# Remove Item
# To remove an item in a set, use the remove(), or the discard() method.
# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)


# Note: If the item to remove does not exist, remove() will raise an error.

# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print()
print(thisset)


# Note: If the item to remove does not exist, discard() will NOT raise an error.

# You can also use the pop() method to remove an item, but this method will remove the last item.
#   Remember that sets are unordered, so you will not know what item that gets removed.

# The return value of the pop() method is the removed item.
# Remove the last item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print()
print(x)
print(thisset)


# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print()
print(thisset)


# The del keyword will delete the set completely:
"""
thisset = {"apple", "banana", "cherry"}
del thisset
print()
print(thisset)
"""

# Loop Items
# You can loop through the set items by using a for loop:
# Loop through the set, and print the values:

thisset = {"apple", "banana", "cherry"}
print()
for x in thisset:
    print(x)
