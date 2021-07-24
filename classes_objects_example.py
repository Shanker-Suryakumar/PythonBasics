'''Python is an object oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.'''

# To create a class, use the keyword class.
# Create a class named MyClass, with a property named x.
class MyClass:
    x = 5

print(MyClass)

# Create an object named p1, and print the value of x.
p1 = MyClass()
print(p1.x)

# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created.
# Note: The __init__() function is called automatically every time the class is being used to create a new object.
# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class.

# Create a class named Person, use the __init__() function to assign values for name and age.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Insert a function that prints a greeting, and execute it on the p1 object.
    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("Veena.M", 25)
p1.myfunc()

# You can modify properties on objects like this.
p1.age = 26

print("Name is %s and age is %s" %(p1.name, p1.age))

# You can delete properties on objects by using the del keyword.
# del p1.age # AttributeError: 'Person' object has no attribute 'age'.

# You can delete objects by using the del keyword.
del p1

# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class PersonTest:
    pass
