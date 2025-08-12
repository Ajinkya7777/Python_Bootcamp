class Animal:
    def speak(self):
        # Abstract method simulation
        # Forces subclasses to implement this method
        # Later, we will use Python's 'abc' module to define proper abstract classes and methods.
        raise NotImplementedError("Subclass must implement the 'speak' method.")

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says woof...!"

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says meow...!"

def petSpeak(pet):
    try:
        print(pet.speak())
    except NotImplementedError as e:
        print(f"Error: {e}")

# Creating objects
myDog = Dog("Tommy")
myCat = Cat("Kitto")

# Looping over the pets directly
for pet in [myDog, myCat]:
    print(type(pet))
    print(pet.speak())

# List of pets including an invalid one (Animal)
pets = [Dog("Tom"), Cat("Jerry"), Animal()]

# Loop over pets and call petSpeak for each (with error handling)
for pet in pets:
    petSpeak(pet)

# NOTES:
# 1. The base class Animal uses NotImplementedError in speak() to simulate abstract methods.
# 2. Dog and Cat classes override speak() to provide specific behavior.
# 3. petSpeak() is a helper function demonstrating polymorphism:
#    it accepts any object that has a speak() method and handles errors if not implemented.
# 4. Looping over a list of pets and calling petSpeak() shows how polymorphism enables
#    the same interface to work with different objects.
# 5. In the future, we will use Python's 'abc' module for formal abstract classes and methods.
