"""
python modify strings
"""

# upper case
a = "Hello, World!"
print()
print(a.upper())

# lower case
a = "Hello, World!"
print()
print(a.lower())

# remove white space
a = " Hello, World! "
print()
print(a.strip())  # returns "Hello, World!"

# replace string
a = "Hello, World!"
print()
print(a.replace("H", "J"))

# split string
a = "Hello, World!"
print()
print(a.split(","))  # returns ['Hello', ' World!']
splitArray = a.split(",")
for section in splitArray:
    print(section)
