# Now we can use the module we just created, by using the import statement.

# There are several built-in modules in Python, which you can import whenever you like.
import platform

# You can choose to import only parts from a module, by using the from keyword.
# from mymodule import person1
# print (person1["age"])
# Note: When importing using the from keyword, do not use the module name when referring to elements in the module. Example: person1["age"], not mymodule.person1["age"].

# Import the module named mymodule, and call the greeting function.
# Create an alias for mymodule called my_module.
import module_example as my_module

x = platform.system()
print("You OS is:", x)

# List all the defined names belonging to the platform module.
y = dir(platform)
print(y)

# Note: When using a function from a module, use the syntax: module_name.function_name.
my_module.greeting("Veena Marappa")

# Import the module named mymodule, and access the person1 dictionary.
objperson = my_module.person1
print("Name {0}, Age {1}, Country {2}.".format(objperson["name"], objperson["age"], objperson["country"]))

