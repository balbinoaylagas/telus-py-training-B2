"""
python format strings
"""

# string format
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# this gives an error!!!
"""
age = 36
txt = "My name is John, I am " + age
print()
print(txt)
"""

# But we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them
#   in the string where the placeholders {} are:
age = 36
txt = "My name is John, and I am {}"
print()
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into
#   the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print()
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct
#   placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay ${2} dollars for {0} pieces of item {1}."
print()
print(myorder.format(quantity, itemno, price))

# f strings o format strings
quantity = 3
itemno = 567
price = 49.95
myorder = f"I want to pay ${price} dollars for {quantity} pieces of item {itemno}."
print()
print(myorder)
