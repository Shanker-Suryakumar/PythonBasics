# Rules for Python variables:
# 1. A variable name must start with a letter or the underscore character
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 4. Variable names are case-sensitive (age, Age and AGE are three different variables)

# Variables are containers for storing data values.
# Unlike other programming languages, Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
x = 5
y = "Veena.M"
print(x)
print(y)

# Variables do not need to be declared with any particular type and can even change type after they have been set.
x = 4 # x is of type int
x = "Yashodha.M" # x is now of type str
print(x)

# String variables can be declared either by using single or double quotes.
x = "Marappa"
# is the same as
x = 'Marappa'
print(x)

# Python allows you to assign values to multiple variables in one line.
x, y, z = "Veena", "Shanker", "Aparna"
print(x)
print(y)
print(z)

# You can assign the same value to multiple variables in one line.
x = y = z = "Rajesh Suryakumar"
print(x)
print(y)
print(z)

# You can use the + character to add a variable to another variable.
x = "Veena is "
y = "gorgeous"
z =  x + y
print(z)

# For numbers, the + character works as a mathematical operator.
x = 5
y = 10
print(x + y)

# Variables that are created outside of a function (as in all of the examples above) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
x = "gorgeous"

def myfunc():
  global x
  x = "cute"
  print("Veena is " + x)

myfunc()

print("Veena is " + x)

# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "gorgeous"

myfunc()

print("Veena is " + x)