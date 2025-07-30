import random

# Ask the user for bounds
while True:
    try:
        lower = int(input("Enter the LOWER bound: "))
        upper = int(input("Enter the UPPER bound: "))
        if lower >= upper:
            print("Lower bound must be less than upper bound. Try again.")
        else:
            break
    except ValueError:
        print("Please enter valid integer bounds.")

# Generate a random secret number in the inclusive range
secret = random.randint(lower, upper)

print(f"\nI'm thinking of a number between {lower} and {upper}. Can you guess it?")

attempts = 0
while True:
    try:
        guess = int(input("Your guess: "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        continue

    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret} in {attempts} {'try' if attempts == 1 else 'tries'}.")
        break
