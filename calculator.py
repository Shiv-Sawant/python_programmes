print("====Welcome to digital calculator====")

def show_history():
    file = open("history.txt","r")
    lines = file.readlines()
    
    if(len(lines) == 0):
        print("History Not Found.!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()
    
def clear():
    file = open("history.txt","w")
    file.close()
    
def save_history(val,res):
    file = open("history.txt","a")
    file.write(val + " = " + str(res) + "\n")
    file.close()
    
def calculator(user_input):
    parts = user_input.split()
    
    if(len(parts) != 3):
        print("provide valid equation")
        return
    
    num1 = float(parts[0])
    op = parts[1]
    num2 = float(parts[2])    
    result = 0
    
    if(op == "+"):
        result = num1 + num2
    elif(op == "-"):
        result = num1 - num2
    elif(op == "*"):
        result = num1 * num2
    elif(op == "/"):
        if(num2 == 0):
            print("cannot divided by zero")
        result = num1 / num2
    save_history(user_input, result)
    print("result => ", result)
    
def main():
    
    while True:
        user_input = input("Enter calculation (+ -  /) or command (history, clear or exit)")
        
        if(user_input == "exit"):
            break
        elif(user_input == "clear"):
            clear()
        elif(user_input == "history"):
            show_history()
        else:
            calculator(user_input)
            
    
main()