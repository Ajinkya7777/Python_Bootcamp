# Basic arithmetic operations in Python
# -------------------------------------

# Addition
# Example: adding two numbers
sum_result = 2 + 1

# Subtraction
# Example: subtracting one number from another
difference = 2 - 1

# Multiplication
# Standard multiplication between two numbers
product = 2 * 2

# Division
# Regular division always returns a float in Python 3
division_result = 3 / 2

# Floor Division
# This returns the integer part only, no decimals (like math.floor)
floor_div = 7 // 4  # Output will be 1

# Modulo
# Returns the remainder of a division
mod_result = 7 % 4  # Should give 3

# Power (Exponentiation)
# This raises 2 to the power of 3 (2^3)
power = 2 ** 3

# Square root using exponent
# Raising to the power of 0.5 is same as square root
sqrt_result = 4 ** 0.5

# Order of operations (PEMDAS)
# Python follows standard operator precedence
order_ops = 2 + 10 * 10 + 3  # Evaluates as 2 + 100 + 3 = 105

# Using parentheses to change the order
# This groups operations to control execution
custom_order = (2 + 10) * (10 + 3)  # (12) * (13) = 156

# -------------------------------------
# Variable Assignments and Reassignments
# -------------------------------------

# Assigning a number to a variable
a = 5

# Variables can be used in arithmetic operations
double_a = a + a  # 5 + 5 = 10

# Reassigning the variable to a new value
a = 10

# Checking current value of a
current_value = a

# Reusing variable to redefine itself
a = a + a  # Now a becomes 20

# -----------------
# Assignment 1
# -----------------

# Defining income and tax rate
my_income = 100
tax_rate = 0.1  # 10% tax rate

# Calculating tax by multiplying income with rate
my_taxes = my_income * tax_rate  # Should be 10.0

# Output the final tax amount
print("Tax amount:", my_taxes)
