# animal_module.py

from oop.dog import Dog
from oop.cat import Cat

def show_pet_sound(pet):
    """
    Prints the sound that a pet makes by calling the `speak` method.
    """
    print(f"{pet.speak()}")

# Notes:
# 1. This file demonstrates how to import specific classes (Dog and Cat) from other modules.
# 2. By calling the `speak()` method on a pet, we showcase polymorphism.
# 3. The `show_pet_sound()` function works with any object that implements a `speak()` method.
