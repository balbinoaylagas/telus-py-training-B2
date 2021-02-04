"""
Python Lists
"""

# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data,
#   the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:
thislist = ["apple", "banana", "cherry"]
print()
print(thislist)

# List Items
# List items are ordered, changeable, and allow duplicate values.
# List items are indexed, the first item has index [0], the second item has index [1] etc.

# Ordered
# When we say that lists are ordered, it means that the items have a defined order,
#   and that order will not change.
# If you add new items to a list, the new items will be placed at the end of the list.

# Changeable
# The list is changeable, meaning that we can change, add, and remove items in a list
#   after it has been created.

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print()
print(thislist)

# List Length
# To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print()
print(len(thislist))

# List Items - Data Types
# List items can be of any data type:
# String, int and boolean data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print()
print(list1)
print(list2)
print(list3)

# A list can contain different data types:
# A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]
print()
print(list1)

# type()
# From Python's perspective, lists are defined as objects with the data type 'list':
# <class 'list'>
# What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print()
print(type(mylist))

# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.
# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry"))  # note the double round-brackets
print()
print(thislist)

# Access Items
# List items are indexed and you can access them by referring to the index number:
# Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print()
print(thislist[1])


# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.
# Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print()
print(thislist[-1])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print()
print(thislist[2:5])


# Check if Item Exists
# To determine if a specified item is present in a list use the in keyword:
# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
print()
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")


# Change Item Value
# To change the value of a specific item, refer to the index number:
# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print()
print(thislist)


# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values,
#   and refer to the range of index numbers where you want to insert the new values:
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print()
print(thislist)

# If you insert more items than you replace, the new items will be inserted where you
#   specified, and the remaining items will move accordingly:
# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print()
print(thislist)

# If you insert less items than you replace, the new items will be inserted where you
#   specified, and the remaining items will move accordingly:
# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print()
print(thislist)


# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use
#   the insert() method.
# The insert() method inserts an item at the specified index:
# Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print()
print(thislist)


# Append Items
# To add an item to the end of the list, use the append() method:
# Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print()
print(thislist)

# Insert Items
# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at the specified index:
# Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print()
print(thislist)


# Extend List
# To append elements from another list to the current list, use the extend() method.
# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print()
print(thislist)

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object
#   (tuples, sets, dictionaries etc.).
# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print()
print(thislist)

# Remove Specified Item
# The remove() method removes the specified item.
# Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print()
print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.
# Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print()
print(thislist)

# if you do not specify the index, the pop() method removes the last item.
# Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print()
print(thislist)


# The del keyword also removes the specified index:
# Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print()
print(thislist)


# The del keyword can also delete the list completely.
# Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist
"""
print()
print(thislist)
"""

# Clear the List
# The clear() method empties the list.
# The list still remains, but it has no content.
# Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print()
print(thislist)


# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:
# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print()
print(thislist)


# Example
# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print()
print(thislist)


# Sort Descending
# To sort descending, use the keyword argument reverse = True:
# Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print()
print(thislist)


# Example
# Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print()
print(thislist)
