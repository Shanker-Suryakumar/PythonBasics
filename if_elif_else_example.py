a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# If you have only one statement to execute, you can put it on the same line as the if statement.
if a > b: print("a is greater than b")

# If you have only one statement to execute, one for if, and one for else, you can put it all on the same line.
a = 2
b = 330
print("A") if a > b else print("B")

# One line if else statement, with 3 conditions.
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Test if a is greater than b, AND if c is greater than a.
a = 200
b = 33
c = 500
if a > b and c > a: print("Both conditions are True")

# The or keyword is a logical operator, and is used to combine conditional statements.
a = 200
b = 33
c = 500
if a > b or a > c: print("At least one of the conditions is True")

# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
a = 33
b = 200

if b > a: pass
