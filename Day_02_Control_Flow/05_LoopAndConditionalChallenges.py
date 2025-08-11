# Challenge 1: Sum of even numbers between 1 and 50
total = 0
for i in range(1, 51):
    if i % 2 == 0:
        total += i
print(f"Sum of even numbers: {total}")

# Challenge 2: Guess the number
secret = 7
guess = None
while guess != secret:
    guess = int(input("Guess the number (1-10): "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
print("You guessed it!")
