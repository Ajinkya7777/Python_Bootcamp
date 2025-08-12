# Day 3 - Tuple unpacking from a function

def get_min_max(numbers):
    return min(numbers), max(numbers)

nums = [5, 2, 9, 1, 7]
min_val, max_val = get_min_max(nums)  # Tuple unpacking
print(f"Min: {min_val}, Max: {max_val}")
