'''Inheritance allows us to define a class that inherits all the methods and properties from another class.
Parent class is the class being inherited from, also called base class.
Child class is the class that inherits from another class, also called derived class.'''

# Create a class named Person, with firstname and lastname properties, and a printname method.
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def printname(self):
        print("First name is {0} & lastname is {1}".format(self.firstname, self.lastname))

# Use the Person class to create an object, and then execute the printname method.
objperson = Person("Veena", "Marappa")
objperson.printname()

# To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class.
# Create a class named Student, which will inherit the properties and methods from the Person class.
# Note: Use the pass keyword when you do not want to add any other properties or methods to the class.
class Student(Person):
    # pass
    # When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.
    def __init__(self, fname, lname, year):
        # To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function.
        # Person.__init__(self, fname, lname)

        # Python also has a super() function that will make the child class inherit all the methods and properties from its parent.
        super().__init__(fname, lname)

        self.fname = fname
        self.lname = lname
        # Add a property called graduationyear to the Student class.
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

# Now the Student class has the same properties and methods as the Person class.
# Use the Student class to create an object, and then execute the printname method.
objstudent = Student("Shanker", "Suryakumar", "2010")
objstudent.printname()
print("Graduation year of {0} is {1}".format(objstudent.fname, objstudent.graduationyear))
objstudent.welcome()