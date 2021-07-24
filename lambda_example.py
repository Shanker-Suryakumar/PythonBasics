# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.

# A lambda function that adds 10 to the number passed in as an argument, and print the result.
x = lambda a : a + 10
print(x(5))

# A lambda function that multiplies argument a with argument b and print the result.
x = lambda a, b : a * b
print(x(5, 6))

# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number.
def myfunc(n):
    return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))
