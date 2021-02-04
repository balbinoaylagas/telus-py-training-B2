"""
Python Functions
"""

# A function is a block of code which only runs when it is called.

# You can pass data, known as parameters, into a function.

# A function can return data as a result.

# Creating a Function
# In Python a function is defined using the def keyword:

"""
def my_function():
    print("Hello from a function")
"""

# Calling a Function
# To call a function, use the function name followed by parenthesis:


def my_function():
    print("Hello from a function")


my_function()


# Arguments
# Information can be passed into functions as arguments.

# Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

# The following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:


def my_functionName(fname):
    print(fname + " Refsnes")


my_functionName("Emil")
my_functionName("Tobias")
my_functionName("Linus")


# Arguments are often shortened to args in Python documentations.

# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:

# A parameter is the variable listed inside the parentheses in the function definition.

# An argument is the value that is sent to the function when it is called.

# Number of Arguments
# By default, a function must be called with the correct number of arguments. Meaning that
#   if your function expects 2 arguments, you have to call the function with 2 arguments,
#   not more, and not less.

# This function expects 2 arguments, and gets 2 arguments:


def my_functionNames(fname, lname):
    print(fname + " " + lname)


my_functionNames("Emil", "Refsnes")


# If you try to call the function with 1 or 3 arguments, you will get an error:
# Example
# This function expects 2 arguments, but gets only 1:

"""
def my_functionNames(fname, lname):
    print(fname + " " + lname)


my_functionNames("Emil")
"""

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

# If the number of arguments is unknown, add a * before the parameter name:


def my_functionMultiple(*kids):
    print("The youngest child is " + kids[2])


my_functionMultiple("Emil", "Tobias", "Linus")


# Arbitrary Arguments are often shortened to *args in Python documentations.

# Keyword Arguments
# You can also send arguments with the key = value syntax.

# This way the order of the arguments does not matter.


def my_functionOrder(child3, child2, child1):
    print("The youngest child is " + child3)


my_functionOrder(child1="Emil", child2="Tobias", child3="Linus")


# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.

# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:


def my_functionKey(**kid):
    print("His last name is " + kid["lname"])


my_functionKey(fname="Tobias", lname="Refsnes")


# Default Parameter Value
# The following example shows how to use a default parameter value.

# If we call the function without argument, it uses the default value:


def my_functionNoArgs(country="Norway"):
    print("I am from " + country)


my_functionNoArgs("Sweden")
my_functionNoArgs("India")
my_functionNoArgs()
my_functionNoArgs("Brazil")


# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:


def my_functionList(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]

my_functionList(fruits)

# Return Values
# To let a function return a value, use the return statement:


def my_functionReturn(x):
    return 5 * x


print(my_functionReturn(3))
print(my_functionReturn(5))
print(my_functionReturn(9))


# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.


def myfunctionPass():
    pass
