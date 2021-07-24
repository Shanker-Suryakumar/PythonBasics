# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
print(bool("VeenaShanker"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(" "))

# In fact, there are not many values that evaluates to False, except empty values, such as (), [], {}, "", the number 0, and the value None. And of course the value False evaluates to False.
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# One more value, or object in this case, evaluates to False, and that is if you have an objects that are made from a class with a __len__ function that returns 0 or False.
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

# Python also has many built-in functions that returns a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type.
x = 200
print(type(x))
print(isinstance(x, int))
print(isinstance(x, str))
