# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.

# Create a Tuple.
fruitstuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruitstuple)

# You can access tuple items by referring to the index number, inside square brackets.
print(fruitstuple[1])

# Negative indexing means beginning from the end, -1 refers to the last item, -2 refers to the second last item etc.
print(fruitstuple[-1])

# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new tuple with the specified items.

# Note: The search will start at index 2 (included) and end at index 5 (not included).
print(fruitstuple[2:5])

# This example returns the items from index -4 (included) to index -1 (excluded).
print(fruitstuple[-4:-1])

# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
fruitslist = list(fruitstuple)
fruitslist[1] = "litchi"
fruitstuple = tuple(fruitslist)

print("Created a tuple from list:", fruitstuple)

# You can loop through the tuple items by using a for loop.
for items in fruitstuple:
    print(items)

# Check if "apple" is present in the tuple.
if "apple" in fruitstuple:
    print("Yes, 'apple' is in the fruits tuple")

# Print the number of items in the tuple.
print("Length of fruits tuple is:", len(fruitstuple))

# One item tuple, remember the commma.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Note: You cannot remove items in a tuple.
# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely.
# The del keyword can delete the tuple completely.
del thistuple

# To join two or more tuples you can use the + operator.
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print("After joining two tuples:", tuple3)

# It is also possible to use the tuple() constructor to make a tuple.
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
