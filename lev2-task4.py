def generate_fibonacci(n):
    sequence = []
    if n <= 0:
        return sequence
    # First two Fibonacci terms
    sequence.append(0)
    if n == 1:
        return sequence
    sequence.append(1)
    # Generate the rest iteratively
    for _ in range(2, n):
        next_val = sequence[-1] + sequence[-2]
        sequence.append(next_val)
    return sequence

# Prompt user
try:
    n_terms = int(input("Enter the number of Fibonacci terms to generate: "))
    fib_series = generate_fibonacci(n_terms)
    if not fib_series:
        print("Please enter a positive integer.")
    else:
        print("Fibonacci sequence:")
        for num in fib_series:
            print(num, end=" ")
        print()
except ValueError:
    print("Invalid input. Please enter an integer.")
