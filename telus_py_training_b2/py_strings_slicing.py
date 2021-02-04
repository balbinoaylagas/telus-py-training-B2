"""
slicing strings
"""

# slicing
# Get the characters from position 2 to position 5 (not included):
#          0123456789012
message = "Hello, World!"
print()
print(message[2:5])

# slice from the start
# Get the characters from the start to position 5 (not included):
b = "Hello, World!"
print()
print(b[:5])

# slice to the end
# Get the characters from position 2, and all the way to the end:
b = "Hello, World!"
print()
print(b[2:])

# negative indexing
# Get the characters:
# From: "o" in "World!" (position -5)
# To, but not included: "d" in "World!" (position -2):
#    3210987654321
b = "Hello, World!"
print()
print(b[-5:-2])
