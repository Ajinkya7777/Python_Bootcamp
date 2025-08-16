# base_exception.py

class InvalidPetError(Exception):
    """Custom exception for invalid pets."""
    pass

# Notes:
# 1. Custom exceptions are created by subclassing the base `Exception` class.
# 2. `InvalidPetError` will be raised when an invalid pet is detected.
