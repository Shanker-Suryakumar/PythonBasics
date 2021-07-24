# A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

# Create and print a dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# You can access the items of a dictionary by referring to its key name, inside square brackets.
# Get the value of the "model" key.
x = thisdict["model"]
print(x)

# There is also a method called get() that will give you the same result.
x = thisdict.get("model")
print(x)

# You can change the value of a specific item by referring to its key name.
thisdict["year"] = 2020
print(thisdict)

# You can loop through a dictionary by using a for loop.
# When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
for x in thisdict:
  print(x)

# Print all values in the dictionary, one by one.
for x in thisdict:
  print(thisdict[x])

# You can also use the values() function to return values of a dictionary.
for x in thisdict.values():
  print(x)

# Loop through both keys and values, by using the items() function.
for x, y in thisdict.items():
    print("Key: ", x, "| Value: ", y)

# To determine if a specified key is present in a dictionary use the in keyword.
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Print the number of items in the dictionary.
print("Length of dict is: ", len(thisdict))

# Adding an item to the dictionary is done by using a new index key and assigning a value to it.
thisdict["color"] = "red"
print(thisdict)

# The pop() method removes the item with the specified key name.
thisdict.pop("model")
print(thisdict)

# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead).
thisdict.popitem()
print(thisdict)

# The del keyword removes the item with the specified key name.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

# The del keyword can also delete the dictionary completely.
del thisdict

# The clear() keyword empties the dictionary.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)

# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# Another way to make a copy is to use the built-in method dict().
mydict = dict(thisdict)
print(mydict)

# A dictionary can also contain many dictionaries, this is called nested dictionaries.
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

# Create three dictionaries, then create one dictionary that will contain the other three dictionaries.
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

# It is also possible to use the dict() constructor to make a new dictionary.
# note that keywords are not string literals
# note the use of equals rather than colon for the assignment
thisdict = dict(brand="Ford", model="Mustang", year=1964)
print(thisdict)