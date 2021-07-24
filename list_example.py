# List is a collection which is ordered and changeable. Allows duplicate members.
# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.

# Create a List.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist)

# Print the second item of the list.
print(thislist[1])

# Print the last item of the list.
print(thislist[-1])

# Note: The search will start at index 2 (included) and end at index 5 (not included).
# Remember that the first item has index 0.
# Return the third, fourth, and fifth item.
print(thislist[2:5])

# This example returns the items from the beginning to "orange".
print(thislist[:4])

# This example returns the items from "cherry" and to the end.
print(thislist[2:])

# This example returns the items from index -4 (included) to index -1 (excluded).
print(thislist[-4:-1])

# To change the value of a specific item, refer to the index number.
thislist[1] = "blackcurrant"
print(thislist)

# You can loop through the list items by using a for loop.
print("for loop example to loop the items in a list and print:")
for x in thislist:
    print(x)

# To determine if a specified item is present in a list use the in keyword.
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

# To determine how many items a list has, use the len() function.
print(len(thislist))

# To add an item to the end of the list, use the append() method.
thislist.append("pineapple")
print(thislist)

# Insert an item as the second position.
thislist.insert(1, "litchi")
print(thislist)

# The remove() method removes the specified item.
thislist.remove("litchi")
print(thislist)

# The pop() method removes the specified index, (or the last item if index is not specified).
thislist.pop()
print(thislist)

# The del keyword removes the specified index.
del thislist[0]
print(thislist)

# The del keyword can also delete the list completely.
del thislist

# The clear() method empties the list.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# Make a copy of a list with the copy() method.
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Make a copy of a list with the list() method.
mylist = list(thislist)
print(mylist)

# One of the easiest ways to join lists are by using the + operator.
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two lists are by appending all the items from list2 into list1, one by one.
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

# Use the extend() method to add list2 at the end of list1.
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# It is also possible to use the list() constructor to make a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered and unindexed. No duplicate members.
# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.