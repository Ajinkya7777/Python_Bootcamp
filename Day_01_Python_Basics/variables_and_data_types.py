# Day 1: Variables and Data Types

# variables of different types
age = 30                 # Integer
price = 99.99            # Float
first_name = "Ajinkya"   # String
is_active = True         # Boolean

# Printing variable values and types
#type is used to check type of the data type we are having
print("Age:", age, "Type:", type(age))
print("Price:", price, "Type:", type(price))
print("First Name:", first_name, "Type:", type(first_name))
print("Is Active:", is_active, "Type:", type(is_active))

# Type casting examples => similar to java
age_str = str(age)
price_int = int(price)   # Note: this truncates decimals - price will become 99

print("Age as string:", age_str, "Type:", type(age_str))
print("Price as integer:", price_int, "Type:", type(price_int))

# How to take user input 
user_input = input("Enter your name: ")
print("Hello,", user_input)

# this is how we comment in python using '#'
# This is a single-line comment

"""
This is a
multi-line comment (docstring)
"""

# Basic arithmetic operations
a = 10
b = 3

print("Add:", a + b)
print("Sub:", a - b)
print("Multiply:", a * b)
print(" Float Division:", a / b)    
print("Integer Division:", a // b)
print("Modulus:", a % b)   
print("Exponent:", a ** b)
