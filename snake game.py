import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off screen updates
# some needed variables
colors = "red", "blue", "white", "black", "purple"
# Snake setup
snake = []
for i in range(3):  # Initial snake of length 3
    segment = turtle.Turtle("square")
    segment.color(random.choice(colors))
    segment.penup()
    segment.goto(-20 * i, 0)  # Arrange segments in a line
    snake.append(segment)

# Food setup
food = turtle.Turtle("circle")
food.color(random.choice(colors))
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# Score setup
score = 0

# Movement
direction = "stop"

def go_up():
    global direction
    if direction != "down":  # Prevent reversing direction
        direction = "up"

def go_down():
    global direction
    if direction != "up":
        direction = "down"

def go_left():
    global direction
    if direction != "right":
        direction = "left"

def go_right():
    global direction
    if direction != "left":
        direction = "right"

screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")

# Main game loop
while True:
    screen.update()
    time.sleep(0.1)  # Adjust speed

    pen = turtle.Turtle()
    pen.speed(0)
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 250)
    pen.write("Score : 0  High Score : 0", align="center", font=("Candara", 24, "bold"))


    # Move the snake
    if direction != "stop":
        x, y = snake[0].pos()
        if direction == "up":
            snake[0].sety(y + 20)
        elif direction == "down":
            snake[0].sety(y - 20)
        elif direction == "left":
            snake[0].setx(x - 20)
        elif direction == "right":
            snake[0].setx(x + 20)

        # Move segments
        for i in range(len(snake) - 1, 0, -1):
            snake[i].goto(snake[i - 1].pos())

    # Check for collision with food
    if snake[0].distance(food) < 15:
        food.goto(random.randint(-280, 280), random.randint(-280, 280))
        # Add a new segment
        segment = turtle.Turtle("square")
        segment.color(random.choice(colors))
        segment.penup()
        snake.append(segment)
        score += 10
        print(f"Score: {score}")

    # Check for collision with walls
    x, y = snake[0].pos()
    if x < -300 or x > 300 or y < -300 or y > 300:
        print("Game Over!")
        break

    # Check for collision with itself
    for segment in snake[1:]:
        if snake[0].distance(segment) < 10:
            print("Game Over!")
            break
screen.mainloop()
