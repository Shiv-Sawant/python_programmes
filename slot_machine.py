MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

def deposit():
    while True:
        amount = input("Enter the amount you want to deposit: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                return amount
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid number.")

    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                return lines
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")

def get_bet():
    while True:
        bet = input(f"Enter your bet amount (between ${MIN_BET} and ${MAX_BET}): $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                return bet
            else:
                print(f"Bet must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough balance to make that bet. Your current balance is ${balance}.")
        else:
            break
    print("you are betting on", lines, "lines with a bet of $", bet, "each.")

main()