# You can assign a multiline string to a variable by using three quotes.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Or three single quotes.
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Strings in Python are arrays of bytes representing unicode characters.
a = "Hello, World!"
print(a[0])

# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])

# Use negative indexes to start the slice from the end of the string.
b = "Hello, World!"
print(b[-5:-2])

# To get the length of a string, use the len() function.
a = "Hello, World!"
print("Length of string is:", len(a))

# The strip() method removes any whitespace from the beginning or the end.
a = " Hello, Veena.M! "
print(a.strip()) # returns "Hello, Veena.M!"

# The lower() method returns the string in lower case.
a = "Hello, Veena.M!"
print(a.lower())

# The upper() method returns the string in upper case.
a = "Hello, Veena.M!"
print(a.upper())

# The replace() method replaces a string with another string.
a = "Hello, Veena M!"
print(a.replace("M", "Shanker"))

# The split() method splits the string into substrings if it finds instances of the separator.
a = "Hello, Veena.M!"
print(a.split(",")) # returns ['Hello', ' Veena.M!']

# To check if a certain phrase or character is present in a string, we can use the keywords in or not in.
txt = "Veena's home town is Mysore"
x = "Mys" in txt
y = "Mys" not in txt
print("Search string exists:", x)
print("Search string exists:", y)

# Merge variable a with variable b into variable c.
a = "Hello"
b = "Veena.M"
c = a + b
print(c)

# To add a space between them, add a " ".
a = "Hello"
b = "Veena.M"
c = a + " " + b
print(c)

# We can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are.
age = 31
txt = "My name is Shanker, and I am {} years old"
print(txt.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders.
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item no {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders.
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# To insert characters that are illegal in a string, use an escape character.
# An escape character is a backslash \ followed by the character you want to insert.
# An example of an illegal character is a double quote inside a string that is surrounded by double quotes.
txt = "We are the so-called \"Mysorians\" from the Karnataka."
print(txt)