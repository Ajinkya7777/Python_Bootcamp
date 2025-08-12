class Animal:
    def __init__(self):
        print("Animal constructor called")

class Dog(Animal):
    def __init__(self, name):
        print("Dog constructor started")
        super().__init__()  # Calls Animal's constructor
        self.name = name
        print("Dog constructor finished")

dog = Dog("Buddy")


class Person:
    # Constructor (__init__) to initialize instance variables
    def __init__(self, name, age):
        self.name = name  # instance variable
        self.age = age    # instance variable
    
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

# Creating objects with constructor arguments
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

person1.introduce()  # My name is Alice and I am 30 years old.
person2.introduce()  # My name is Bob and I am 25 years old.


'''
# NOTE:
# The __init__ method (constructor) is not mandatory in Python.
# If not defined, Python provides a default one.
# Use __init__ when you want to initialize instance variables.
# In abstract/base classes, it’s common to omit __init__ if no initialization is needed.
# NOTE:
# It runs automatically when a new object is created.
# It initializes instance variables unique to each object.
# 'self' refers to the current instance of the class.
# If no __init__ method is defined, Python provides a default constructor that does nothing.
# Constructors help set up objects with initial data.
# NOTE:
# The order of method definitions inside a class does not matter.
# But in inheritance, the order of constructor calls matters.
# Use super().__init__() inside subclass __init__ to call the parent constructor.
# This ensures proper initialization of all parts of the object.
# Forgetting to call super().__init__() may lead to incomplete object setup.
# Calling super().__init__() ensures the parent class sets up its part of the object.
# In inheritance, the subclass's __init__ runs first.

'''
