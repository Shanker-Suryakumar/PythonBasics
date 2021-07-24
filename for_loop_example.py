# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# Print each fruit in a fruit list.
fruits = ["apple", "banana", "cherry"]
for x in fruits: print(x)

# Loop through the letters in the word "banana".
for x in "banana": print(x)

# With the break statement we can stop the loop before it has looped through all the items.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

# Exit the loop when x is "banana", but this time the break comes before the print.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# With the continue statement we can stop the current iteration of the loop, and continue with the next.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.
for x in range(6):
    print(x)

# The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6).
for x in range(2, 6):
    print(x)

# Increment the sequence with 3 (default is 1).
for x in range(2, 30, 3):
    print(x)

# The else keyword in a for loop specifies a block of code to be executed when the loop is finished.
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# The "inner loop" will be executed one time for each iteration of the "outer loop".
# Print each adjective for every fruit.
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
    for y in fruits:
        print(x, y)

# for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
    pass