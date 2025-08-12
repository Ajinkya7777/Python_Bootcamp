# Day 3 - filter() and map() with normal functions and lambdas

numbers = [1, 2, 3, 4, 5, 6]

# Normal function with filter
def is_even(num):
    return num % 2 == 0

even_numbers = list(filter(is_even, numbers))
print("Even numbers:", even_numbers)

# Lambda with filter
even_numbers_lambda = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers (lambda):", even_numbers_lambda)

# Normal function with map
def square(num):
    return num * num

squared_numbers = list(map(square, numbers))
print("Squares:", squared_numbers)

# Lambda with map
squared_lambda = list(map(lambda x: x * x, numbers))
print("Squares (lambda):", squared_lambda)
