# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Arrays are used to store multiple values in one single variable.

# Create an array containing car names.
cars = ["Mercedes-Benz", "Volvo", "BMW"]

# You refer to an array element by referring to the index number.
# Get the value of the first array item.
x = cars[0]
print(x)

# Note: The length of an array is always one more than the highest array index.
print("Length of array is: ",len(cars))

# Print each item in the cars array.
for x in cars:
    print(x)

# You can use the append() method to add an element to an array.
cars.append("Audi")
print(cars)

# You can use the pop() method to remove an element from the array.
# Delete the second element of the cars array.
cars.pop(1)
print(cars)

# You can also use the remove() method to remove an element from the array.
# Note: The list's remove() method only removes the first occurrence of the specified value.
cars.remove("BMW")
print(cars)