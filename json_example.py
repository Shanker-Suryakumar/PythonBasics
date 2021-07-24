# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.

# Python has a built-in package called json, which can be used to work with JSON data.
# Import the json module.
import json

# If you have a JSON string, you can parse it by using the json.loads() method.
# Convert from JSON to Python.
# some JSON:
x =  '{ "name":"Veena.M", "age":26, "city":"Mysore"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print("Name {0}, Age {1}, City {2}".format(y["name"], y["age"], y["city"]))

# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
# a Python object (dict).
x = {
  "name": "Veena.M",
  "age": 26,
  "city": "Mysore"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# use four indents to make it easier to read the result.
print(json.dumps(x, indent=4))

# Use the separators parameter to change the default separator.
print(json.dumps(x, indent=4, separators=(". ", " = ")))

# The json.dumps() method has parameters to order the keys in the result.
# sort the result alphabetically by keys.
print(json.dumps(x, indent=4, sort_keys=True))

# Convert Python objects into JSON strings, and print the values.
print(json.dumps({"name": "Veena.M", "age": 26}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
