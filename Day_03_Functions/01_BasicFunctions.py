# Day 3 - Basic Functions & Methods

# Simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("Aj"))

# Function with default parameter
def power(num, exponent=2):
    return num ** exponent

print(power(5))       # 25
print(power(5, 3))    # 125

# Method example (functions inside classes)
class Calculator:
    def multiply(self, a, b):
        return a * b

calc = Calculator()
print(calc.multiply(4, 6))
