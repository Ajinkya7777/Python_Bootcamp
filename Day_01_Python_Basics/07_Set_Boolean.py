"""
# Set and Booleans

There are two other object types in Python that we should quickly cover: Sets and Booleans.

## Sets

Sets are an unordered collection of unique elements. We can construct them by using the set() function.
"""

# empty set
x = set()

# We add to sets with the add() method
x.add(1)

# Show set contents
print(x)  # Output: {1}

"""
Note the curly brackets. This does not indicate a dictionary! 
Although you can think of a set as a dictionary with only keys.

Sets only store unique elements. What happens if we add a duplicate element is ,it overrides it?
"""

# Add a different element
x.add(2)
print(x)  # Output: {1, 2}

# Try to add the same element again
x.add(1)
print(x)  # Output: {1, 2}  (no duplicates)

"""
We can cast a list with repeated elements to a set to get unique elements:
"""

# Create a list with repeats
list1 = [1,1,2,2,3,4,5,6,1,1]

# Cast as set to get unique values
print(set(list1))  # Output: {1, 2, 3, 4, 5, 6}

"""
## Booleans

Python comes with Booleans (True and False) that are basically integers 1 and 0.
It also has a placeholder object called None.
"""

# boolean variable
a = True
print(a)  # Output: True

"""
We can also use comparison operators to create booleans:
"""

print(1 > 2)  # Output: False

"""
We can use None as a placeholder for an object we don’t want to assign yet:
"""

b = None
print(b)  # Output: None
