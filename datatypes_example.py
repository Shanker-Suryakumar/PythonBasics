# Print the data type of the variable x.
x = "Hello World"	# str
print(type(x))

x = 20	# int
print(type(x))

x = 20.5	# float
print(type(x))

x = 1j	# complex - Complex numbers are written with a "j" as the imaginary part.
print(type(x))

x = ["apple", "banana", "cherry"]	# list
print(type(x))

x = ("apple", "banana", "cherry")	# tuple
print(type(x))

x = range(6)	# range
print(type(x))

x = {"name" : "John", "age" : 36}	# dict
print(type(x))

x = {"apple", "banana", "cherry"}	# set
print(type(x))

x = frozenset({"apple", "banana", "cherry"})	# frozenset
print(type(x))

x = True	# bool
print(type(x))

x = b"Hello"	# bytes
print(type(x))

x = bytearray(5)	# bytearray
print(type(x))

x = memoryview(bytes(5))	# memoryview
print(type(x))

# Setting the Specific Data Type
x = str("Hello World")	# str
print(type(x))

x = int(20)	# int
print(type(x))

x = float(20.5)	# float
print(type(x))

x = complex(1j)	# complex - Complex numbers are written with a "j" as the imaginary part.
print(type(x))

x = list(("apple", "banana", "cherry"))	# list
print(type(x))

x = tuple(("apple", "banana", "cherry"))	# tuple
print(type(x))

x = range(6)	# range
print(type(x))

x = dict(name="John", age=36)	# dict
print(type(x))

x = set(("apple", "banana", "cherry"))	# set
print(type(x))

x = frozenset(("apple", "banana", "cherry"))	# frozenset
print(type(x))

x = bool(5)	# bool
print(type(x))

x = bytes(5)	# bytes
print(type(x))

x = bytearray(5)	# bytearray
print(type(x))

x = memoryview(bytes(5))	# memoryview
print(type(x))