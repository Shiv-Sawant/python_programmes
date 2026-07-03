import random

print("Welcome to the Number Guesser Game!")

name = input("What's your name? ")
num = input(f"Hello, {name}! enter a number.")

if num.isdigit():
    num = int(num)
    if num <= 0:
        print("Please enter a positive number greater than zero.")
else:
    print("That's not a valid number. Please enter a positive integer.")
    quit()
    
random_number = random.randint(0, num)
chance = 0

while True:
    chance += 1
    user_input = input(f"Make a guess: ")
    if user_input.isdigit():
        user_guess = int(user_input)
    else:
        print("That's not a valid number. Please enter a positive integer.")
        continue
    
    
    if user_guess == random_number:
        print(f"Congratulations, {name}! You've guessed the number {random_number} in {chance} tries.")
        break
    elif user_guess < random_number:
        print("Too low! Try again.")
    elif user_guess > random_number:
        print("Too high! Try again.")
