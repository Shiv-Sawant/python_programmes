import random
import time

operations = ['+', '-', '*', '/']
min_num = 3
max_num = 12
total_questions = 10

def generate_expression():
    num1 = random.randint(min_num, max_num)
    num2 = random.randint(min_num, max_num)
    op = random.choice(operations)
    exp = f"{num1} {op} {num2}"
    ans = eval(exp)
    return exp, ans

expression, answer = generate_expression()

for i in range(total_questions):
    expression, answer = generate_expression()
    print(f"Question {i + 1}: {expression} = ?")
    start_time = time.time()
    user_answer = input("Your answer: ")
    end_time = time.time()
    
    try:
        user_answer = float(user_answer)
        if user_answer == answer:
            print("Correct!")
        else:
            print(f"Incorrect! The correct answer is {answer}.")
    except ValueError:
        print(f"Invalid input! The correct answer is {answer}.")
    
    elapsed_time = end_time - start_time
    print(f"Time taken: {elapsed_time:.2f} seconds\n")
