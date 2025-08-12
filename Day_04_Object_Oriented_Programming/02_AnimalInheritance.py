'''
Inheritance allows a class (Child) to use properties and methods of another class (Parent).
We use 'super().__init__()' to call the Parent class constructor from the Child class.
Methods in the Child class can override the Parent's methods with the same name.
Class-level variables (like 'eat') can be accessed using 'self' or the class name.
NOTE:
1) In Python, methods defined inside a class must include 'self' as the first parameter.
2) 'self' refers to the instance (object) that is calling the method.
3) This allows access to instance variables and other methods of the same object.
4) When you call obj.method(), Python automatically passes 'obj' as 'self' to the method.
5) Regular functions (outside classes) don’t need 'self' because they aren’t tied to any object.

'''






class Animal():
    eat = "veg"
    
    def __init__(self):
        print("Animal created....")
    
    def speak(self):
        print("I speak")
    
    def isVeg(self):
        print("I eat", self.eat)

class Dog(Animal):
    
    eat = 'non-veg'
    
    def __init__(self, name):
        super().__init__()  # Better way to call the superclass constructor / We can also use Animal().__init__()
        self.name = name

    # method overriding
    def speak(self):
        print("I bark")

    def isVeg(self):
        print("This dog eats {}".format(self.eat))

# Animal Object -> General
animal = Animal()
animal.speak()
animal.isVeg()

print()

# Dog Object
myDog = Dog("Tommy")
myDog.speak()
myDog.isVeg()
