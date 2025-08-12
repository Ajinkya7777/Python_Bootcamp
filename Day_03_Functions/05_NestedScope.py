# Day 3 - Nested functions & scope

# Nested function
def outer_function(name):
    def inner_function():
        return f"Hello from inner function, {name}!"
    return inner_function()

print(outer_function("Aj"))

# Scope example
x = 10  # Global

def modify_var():
    global x
    x = 20  # Modify global variable

modify_var()
print("Global x after modification:", x)

# Nonlocal scope
def outer():
    y = 5
    def inner():
        nonlocal y
        y = 15
    inner()
    return y

print("Value of y after inner function:", outer())
