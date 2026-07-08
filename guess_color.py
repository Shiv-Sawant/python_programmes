COLORS = ["R", "G", "B", "Y", "O", "P"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    import random

    return [random.choice(COLORS) for _ in range(CODE_LENGTH)]


def guess_code():
    while True:
        guess = input(
            f"Enter your guess ({CODE_LENGTH} colors from {', '.join(COLORS)}): "
        ).upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"Please enter exactly {CODE_LENGTH} colors.")
            continue
        
        if any(color not in COLORS for color in guess):
            print(f"Invalid colors. Please choose from {', '.join(COLORS)}.")
            continue
            
        
        return guess
    
def check_code(guess, real_code):
    color_count = {}
    correct_position = 0
    incorrect_position = 0
    
    for color in real_code:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1
        
    for guess_color, real_color in zip(guess, real_code):
        if guess_color==real_color:
            correct_position += 1
            color_count[guess_color] -= 1
            
    for guess_color,real_color in zip(guess, real_code):
        if guess_color in color_count and color_count[guess_color] > 0:
            incorrect_position += 1
            color_count[guess_color] -= 1
            
    return correct_position, incorrect_position

def game():
    real_code = generate_code()
    # print(real_code)  # For testing purposes, you can remove this line in production
    for attempt in range(1,TRIES+1):
        guess = guess_code()
        correct_position, incorrect_position = check_code(guess, real_code)
        
        if correct_position == CODE_LENGTH:
            print(f"Congratulations! You've guessed the code {real_code} in {attempt} tries.")
            break
        
        print(f"Attempt {attempt}: {correct_position} correct position(s), {incorrect_position} incorrect position(s).")

    else:
        print(f"Sorry, you've used all your tries. The correct code was {real_code}.")
        
game()