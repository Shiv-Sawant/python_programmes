import random

easy_words = ["apple", "banana", "grape", "orange", "peach"]
medium_words = ["computer", "python", "programming", "algorithm", "function"]
hard_words = [
    "encyclopedia",
    "photosynthesis",
    "metamorphosis",
    "quintessential",
    "hippopotamus",
]

print("====== Guessing Password Game ====")
print("Choose difficulty level:")
print("1. Easy")
print("2. Medium")
print("3. Hard")

level = input("Enter the level (1/2/3): ").strip()
if level == "1":
    word_list = random.choice(easy_words)
elif level == "2":
    word_list = random.choice(medium_words)
elif level == "3":
    word_list = random.choice(hard_words)
else:
    print("Invalid level. Please choose 1, 2, or 3.")
    word_list = random.choice(easy_words)

attempts = 0
print(f"Guess the password! It has {len(word_list)} letters.")

while True:
    guess = input("Enter your guess: ").strip().lower()
    attempts += 1

    if guess == word_list:
        print(
            f"Congratulations! You've guessed the password '{word_list}' in {attempts} attempts."
        )
        break

    hint = ""
    for i in range(len(word_list)):
        if i < len(guess) and guess[i] == word_list[i]:
            hint += guess[i]
        else:
            hint += "_"
    print(f"Hint: {hint}")
