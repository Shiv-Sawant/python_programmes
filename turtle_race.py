import turtle
import time
import random

WIDTH, HEIGHT = 1200, 600
COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "brown", "cyan", "magenta", "lime", "navy", "maroon", "olive", "teal", "silver", "gold", "coral", "indigo", "violet"]

def get_number_of_turtles():
    while True:
        try:
            num_turtles = input("Enter the number of turtles (2-20): ")
            if num_turtles.isdigit():
                num_turtles = int(num_turtles)
            else:
                print("Invalid input. Please enter a valid integer.")
                continue
            
            if 2 <= num_turtles <= 20:
                return num_turtles
            else:
                print("Please enter a number between 2 and 20.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def race(colors):
    turtles = create_turtles(colors)
    
    while True:
        for t in turtles:
            t.forward(random.randint(1, 20))
            x, y = t.position()
            if y >= HEIGHT // 2 - 10:
                print(f"The winner is the {t.color()[0]} turtle!")
                return
    

def create_turtles(colors):
    turtles = []
    spacingx = WIDTH // (len(colors) + 1)
    for i, color in enumerate(colors):
        t = turtle.Turtle()
        t.color(color)
        t.shape("turtle")
        t.left(90)
        t.penup()
        t.setpos(-WIDTH // 2 + (i + 1) * spacingx, -HEIGHT // 2 + 20)
        t.pendown()
        turtles.append(t)   
    return turtles

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Race")

turtles = get_number_of_turtles()
init_turtle()

random.shuffle(COLORS)
colors = COLORS[:turtles]

race(colors)