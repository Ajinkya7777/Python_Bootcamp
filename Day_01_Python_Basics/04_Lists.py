# Lists

"""
  Earlier when discussing strings there is the concept of a sequence in Python.
  Lists can be thought of the most general version of a  sequence in Python.
  Unlike strings, they are mutable, meaning the elements inside a list can be changed!

  In this section we will learn about:
  1) Creating lists
  2) Indexing and Slicing Lists
  3) Basic List Methods
  4) Nesting Lists
  5) Introduction to List Comprehensions
 
 Lists are constructed with brackets [] and commas separating every element in the list.
 
 """

# Assign a list to an variable named my_list
my_list = [1, 2, 3]

# We just created a list of integers, but lists can actually hold different object types. For example:
my_list = ['A string', 23, 100.232, 'o']

# Just like strings, the len() function will tell you how many items are in the sequence of the list.
print(len(my_list))  # Output: 4

# Indexing and Slicing
# Indexing and slicing work just like in strings.
my_list = ['one', 'two', 'three', 4, 5]

# Grab element at index 0
print(my_list[0])  # Output: 'one'

# Grab index 1 and everything past it
print(my_list[1:])  # Output: ['two', 'three', 4, 5]

# Grab everything UP TO index 3
print(my_list[:3])  # Output: ['one', 'two', 'three']

# We can also use + to concatenate lists, just like we did for strings.
print(my_list + ['new item'])  # Output: ['one', 'two', 'three', 4, 5, 'new item']

# Note: This doesn't actually change the original list!
print(my_list)  # Output: ['one', 'two', 'three', 4, 5]

# You would have to reassign the list to make the change permanent.
my_list = my_list + ['add new item permanently']
print(my_list)  # Output: ['one', 'two', 'three', 4, 5, 'add new item permanently']

# We can also use the * for a duplication method similar to strings:
print(my_list * 2)  
# Output: ['one', 'two', 'three', 4, 5, 'add new item permanently', 'one', 'two', 'three', 4, 5, 'add new item permanently']

# Again doubling not permanent
print(my_list)  # Output: ['one', 'two', 'three', 4, 5, 'add new item permanently']

# Basic List Methods

# Create a new list
list1 = [1, 2, 3]

# Use the append method to permanently add an item to the end of a list:
list1.append('append me!')
print(list1)  # Output: [1, 2, 3, 'append me!']

# Use pop to "pop off" an item from the list.
# By default pop takes off the last index, but you can also specify which index to pop off.
print(list1.pop(0))  # Pop off the 0 indexed item, Output: 1
print(list1)  # Output: [2, 3, 'append me!']

# Assign the popped element, remember default popped index is -1
popped_item = list1.pop()
print(popped_item)  # Output: 'append me!'
print(list1)  # Output: [2, 3]

# It should also be noted that lists indexing will return an error if there is no element at that index.
# For example:
# print(list1[100])  # This will raise IndexError: list index out of range

# We can use the sort method and the reverse methods to also affect your lists:
new_list = ['a', 'e', 'x', 'b', 'c']
print(new_list)  # Output: ['a', 'e', 'x', 'b', 'c']

# Use reverse to reverse order
new_list.reverse()
print(new_list)  # Output: ['c', 'b', 'x', 'e', 'a']

# Use sort to sort the list (for numbers it will go ascending)
new_list.sort()
print(new_list)  # Output: ['a', 'b', 'c', 'e', 'x']

"""
    Nesting Lists :-
    A great feature of of Python data structures is that they support *nesting*.
    This means we can have data structures within data structures.
    For example: A list inside a list.
"""

# Let's make three lists
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]
lst_3 = [7, 8, 9]

# Make a list of lists to form a matrix
matrix = [lst_1, lst_2, lst_3]
print(matrix)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# We can again use indexing to grab elements,
# but now there are two levels for the index.
# The items in the matrix object, and then the items inside that list!
print(matrix[0])      # Output: [1, 2, 3]
print(matrix[0][0])   # Output: 1

"""
    List Comprehensions :- 
    Python has an advanced feature called list comprehensions.
    They allow for quick construction of lists.
    To fully understand list comprehensions we need to understand for loops.
    Build a list comprehension by deconstructing a for loop within a []
"""
 
# We used a list comprehension here to grab the first element of every row in the matrix object.
first_col = [row[0] for row in matrix]
print(first_col)  # Output: [1, 4, 7]


