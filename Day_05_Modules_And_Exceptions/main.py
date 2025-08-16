# main.py

from oop.dog import Dog
from oop.cat import Cat
from exception_handling.try_except import handle_exception_example
from exception_handling.custom_exception import validate_pet, InvalidPetError
from modules.animal_module import show_pet_sound
from modules.exception_module import check_pet
from modules.external_package import fetch_data_from_url

def main():
    """
    Main function to run all the examples and demonstrate the concepts.
    """
    # Creating Dog and Cat instances
    myDog = Dog("Tommy")
    myCat = Cat("Kitto")

    # Show pet sounds using the animal module
    show_pet_sound(myDog)  # Outputs: Tommy says woof...!
    show_pet_sound(myCat)  # Outputs: Kitto says meow...!

    # Handling exceptions using try-except
    handle_exception_example()

    # Validating pet type
    try:
        validate_pet(myDog)  # Valid pet
        validate_pet("Not a Pet")  # Invalid pet
    except InvalidPetError as e:
        print(f"Custom Error: {e}")

    # Checking pet validation using exception module
    check_pet("Dog")  # Valid pet
    check_pet(123)    # Invalid pet (this will raise an error)

    # Using external package: requests
    print("\nFetching data from an external URL:")
    fetch_data_from_url("https://jsonplaceholder.typicode.com/todos/1")  # Example API URL

# Entry point for execution
if __name__ == "__main__":
    main()

# Notes:
# 1. The `main()` function ties everything together and demonstrates the various concepts: classes, exception handling, modules, and packages.
# 2. The `if __name__ == "__main__":` construct ensures that this script runs only when executed directly (not when imported).
# 3. The `requests` package is used to fetch data from an external URL in the `fetch_data_from_url()` function.
