import string

# Prompt the user to enter the filename
file_path = input("Enter the text file path: ").strip()

try:
    # Open and read the file
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    # Normalize case
    text = text.lower()
    # Remove punctuation
    translator = str.maketrans('', '', string.punctuation)
    text = text.translate(translator)

    # Split into words
    words = text.split()

    # Count word occurrences using dictionary
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    # Sort words alphabetically
    for word in sorted(counts):
        print(f"{word}: {counts[word]}")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
except Exception as e:
    print("An error occurred:", e)
