# Day 3 - Interaction between functions

def square(x):
    return x * x

def sum_of_squares(a, b):
    return square(a) + square(b)  # Calling another function

print(sum_of_squares(3, 4))
