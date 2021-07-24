# You can convert from one type to another with the int(), float(), and complex() methods.
# Note: You cannot convert complex numbers into another number type.

x = 1 # int
y = 2.8 # float
z = 1j # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers.
import random
print("Random number is:", random.randrange(1,10))