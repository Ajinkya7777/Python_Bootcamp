"""
Dictionaries

We've been learning about sequences in Python but now we're going to switch gears and learn about mappings in Python.
Mappings can be thought of as hash tables in other languages.

This section covers:
1.) Constructing a Dictionary
2.) Accessing objects from a dictionary
3.) Nesting Dictionaries
4.) Basic Dictionary Methods

Mappings store objects by a key, unlike sequences that store objects by position.
A Python dictionary consists of a key and an associated value. The value can be almost any Python object.
"""

# Constructing a Dictionary
# Make a dictionary with {} and : to signify a key and a value
my_dict = {'key1': 'value1', 'key2': 'value2'}

# Call values by their key
print(my_dict['key2'])  # Output: 'value2'

"""
Dictionaries can hold various data types. For example:
"""

my_dict = {'key1': 123, 'key2': [12, 23, 33], 'key3': ['item0', 'item1', 'item2']}

# Call items from the dictionary
print(my_dict['key3'])  # Output: ['item0', 'item1', 'item2']

# Call an index on that value
print(my_dict['key3'][0])  # Output: 'item0'

# Call methods on that value
print(my_dict['key3'][0].upper())  # Output: 'ITEM0'


# We can modify the values of keys:


print(my_dict['key1'])  # Output: 123

# Subtract 123 from the value
my_dict['key1'] = my_dict['key1'] - 123

# Check
print(my_dict['key1'])  # Output: 0


# Python allows shorthand operators like -= for self subtraction:


my_dict['key1'] -= 123
print(my_dict['key1'])  # Output: -123


# Creating keys by assignment in an empty dictionary:


# Create a new dictionary
d = {}

# Assign new keys and values
d['animal'] = 'Dog'
d['answer'] = 42

print(d)  # Output: {'animal': 'Dog', 'answer': 42}


# Nesting dictionaries:


# Dictionary nested inside dictionaries
d = {'key1': {'nestkey': {'subnestkey': 'value'}}}

# Access nested value
print(d['key1']['nestkey']['subnestkey'])  # Output: 'value'


# Some useful dictionary methods:


# Create a sample dictionary
d = {'key1': 1, 'key2': 2, 'key3': 3}

# Get all keys
print(d.keys())  # dict_keys(['key1', 'key2', 'key3'])

# Get all values
print(d.values())  # dict_values([1, 2, 3])

# Get all items as tuples
print(d.items())  # dict_items([('key1', 1), ('key2', 2), ('key3', 3)])

