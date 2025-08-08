"""
# Tuples

In Python tuples are very similar to lists, however, unlike lists they are *immutable* meaning they cannot be changed. 
You would use tuples to present things that shouldn't be changed, such as days of the week, or dates on a calendar. 

In this section, we will get a brief overview of the following:

    1.) Constructing Tuples
    2.) Basic Tuple Methods
    3.) Immutability
    4.) When to Use Tuples

You'll have an intuition of how to use tuples based on what you've learned about lists. We can treat them very similarly with the major distinction being that tuples are immutable.

## Constructing Tuples

The construction of a tuple uses () with elements separated by commas. For example:
"""

# Create a tuple
t = (1, 2, 3)

# Check length just like a list
print(len(t))  # 3

# Can also mix object types
t = ('one', 2)
print(t)  # ('one', 2)

# Use indexing just like we did in lists
print(t[0])  # 'one'

# Slicing just like a list
print(t[-1])  # 2

"""
## Basic Tuple Methods
Tuples have built-in methods, but not as many as lists do.
"""

# Use .index to enter a value and return the index
print(t.index('one'))  # 0

# Use .count to count the number of times a value appears
print(t.count('one'))  # 1

"""
## Immutability
It can't be stressed enough that tuples are immutable. To drive that point home:
"""

try:
    t[0] = 'change'  # This will raise an error
except TypeError as e:
    print(e)  # 'tuple' object does not support item assignment

"""
Because of this immutability, tuples can't grow. Once a tuple is made we cannot add to it.
"""

try:
    t.append('nope')  # This will raise an error
except AttributeError as e:
    print(e)  # 'tuple' object has no attribute 'append'

"""
## When to use Tuples

Tuples are not used as often as lists in programming, but are used when immutability is necessary. 
If in your program you are passing around an object and need to make sure it does not get changed, then a tuple becomes your solution. It provides a convenient source of data integrity.

"""
