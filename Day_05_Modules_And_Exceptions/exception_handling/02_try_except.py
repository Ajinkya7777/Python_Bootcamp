# try_except.py

def handle_exception_example():
    """
    Demonstrates the basic structure of try-except block for error handling.
    """
    try:
        # Simulate an exception (ZeroDivisionError)
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Error: {e}")  # Handle specific exception (ZeroDivisionError)
    finally:
        print("This block always executes.")  # This block will always run

# Notes:
# 1. The `try` block contains code that might raise an exception.
# 2. The `except` block catches specific exceptions and handles them.
# 3. The `finally` block runs no matter what, even if an exception is raised.
