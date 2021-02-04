"""
python Strings
"""

# strings
print()
print("Hello world")

# assign a string to a variable
message = "my new hello world"
print()
print(message)

# multiple line strings
print()
message = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(message)

# strings are arrays
#                        111
#              0123456789012
stringArray = "Hello, World!"
print()
print(stringArray[1])

# looping through a string
print()
for letter in "banana":
    print(letter)

# string length
message = "hello world"
print()
print(len(message))

# Check String
# Check if "free" is present in the following text:
txt = "The best things in life are free!"
print()
print("free" in txt)
print("donkey" in txt)

# Print only if "free" is present:
print()
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


# Check if NOT
txt = "The best things in life are free!"
print()
print("expensive" not in txt)

# print only if "expensive" is NOT present:
txt = "The best things in life are free!"
print()
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")
