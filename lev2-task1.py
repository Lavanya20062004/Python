import random
secret = random.randint(1, 100)
print("I have selected a number between 1 and 100. Can you guess it?")
attempts = 0
while True:
    guess_str = input("Enter your guess (1–100): ").strip()
    try:
        guess = int(guess_str)
    except ValueError:
        print("That's not a valid number. Please enter an integer.")
        continue

    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} {'try' if attempts == 1 else 'tries'}.")
        break
