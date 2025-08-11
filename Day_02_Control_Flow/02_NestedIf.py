#Nested IF example

number = int(input("Enter a number:"))
if number > 0:
    if number % 2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")

elif number < 0:
    print("Negative Number")
else:
    print("Zero")