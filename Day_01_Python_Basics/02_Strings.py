# Strings in Python
# -----------------
# Strings are used to record text information such as names.
# They are sequences, which means Python keeps track of every element in the string.

# Creating Strings
# ----------------

# Single quotes
'hello'

# Double quotes
"hello"

# Full sentence
'This is also a string'

# Be careful with quotes inside strings!
# 'I'm going to get an error'  # This will raise a SyntaxError

# Using double quotes to avoid escape characters or else we can use '/' also
"Now I'm ready to use single quotes inside a string!"

# Printing Strings
# ----------------

# This just returns a string in an interactive environment
'Hello World'

# Multiple strings like this won’t display together
'Hello World 1'
'Hello World 2'

# Use print() to properly display strings
print('Hello World 1')
print('Hello World 2')

# Printing new lines
print('Use \\n to print a new line')
print('\n')
print('See what I mean?')

# String Basics
# -------------

# len() function returns the length of a string
len('Hello World')  # Should return 11

# String Indexing and Slicing
# ---------------------------

# Assigning a string
s = 'Hello World'

# Indexing
s[0]    # 'H'
s[1]    # 'e'
s[2]    # 'l'

# Slicing from index 1 onwards
s[1:]   # 'ello World'

# Slicing from beginning to index 3 (not inclusive)
s[:3]   # 'Hel'

# Full slice returns original string
s[:]    # 'Hello World'

# Negative indexing
s[-1]   # 'd'
s[:-1]  # 'Hello Worl'

# Step size in slicing
s[::1]    # 'Hello World'
s[::2]    # 'HloWrd'
s[::-1]   # 'dlroW olleH' — reversed string

# String Properties (Immutability)
# --------------------------------

# Strings are immutable. This will raise an error:
# s[0] = 'x'  # TypeError

# Concatenation
s + ' concatenate me!'  # New string
s = s + ' concatenate me!'  # Reassign to same variable
print(s)

# Repetition
letter = 'z'
letter * 10  # 'zzzzzzzzzz'

# Basic String Methods
# --------------------

s.upper()      # Converts to uppercase
s.lower()      # Converts to lowercase
s.split()      # Splits string into list using space as default separator
s.split('W')   # Splits using 'W' as separator

# Print Formatting
# ----------------

# Insert values into a string with format()
"Insert another string with curly brackets: {}".format("The inserted string")

#f-strings 
full_name = "Ajinkya Shinde"
firstName,lastName = full_name.split(" ")
print(f"The First Name is {firstName} & Last Name is {lastNamep}")