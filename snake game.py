import turtle
import time
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off screen updates

# Some needed variables
colors = ["red", "blue", "green", "black", "purple"]
GAME_OVER = False

# Snake setup
snake = []
head = turtle.Turtle("square")
head.color(random.choice(colors))
head.penup()
snake.append(head)

# Food setup
food = turtle.Turtle("circle")
food.color(random.choice(colors))
food.penup()
food.goto(random.randint(-280, 280), random.randint(-280, 280))

# Barrier setup
barrier = turtle.Turtle("triangle")
barrier.color("black")
barrier.penup()
barrier.goto(random.randint(-280, 280), random.randint(-280, 280))

# Score setup
scores = 0
high_score = 0  # Initialize high score

# Scoreboard turtle
score = turtle.Turtle()
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0, 250)
score.write(f"Score: {scores}  High Score: {high_score}", align="center", font=("Candara", 24, "bold"))

# Game Over display
def GameOver():
    global GAME_OVER
    GAME_OVER = True
    gameOver = turtle.Turtle()
    gameOver.speed(0)
    gameOver.penup()
    gameOver.hideturtle()
    gameOver.goto(0, 0)
    gameOver.write("Game Over!", align="center", font=("Courier", 36, "bold"))

# Movement direction
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

# Function to clone a turtle
def clone_turtle(original_turtle):
    new_turtle = original_turtle.clone()  # Create a copy of the turtle
    new_turtle.penup()  # Keep the new turtle from drawing
    return new_turtle

# Main game loop
while not GAME_OVER:
    screen.update()
    time.sleep(0.1)  # Adjust speed

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
        food.color(random.choice(colors))
        food.goto(random.randint(-280, 280), random.randint(-280, 280))

        # Add a new segment by cloning the last segment
        new_segment = clone_turtle(snake[-1])
        new_segment.color(random.choice(colors))  # Optionally randomize the color of the new segment
        snake.append(new_segment)

        # Update Score
        scores += 10
        if scores > high_score:
            high_score = scores

        score.clear()
        score.write(f"Score: {scores}  High Score: {high_score}", align="center", font=("Courier", 24, "bold"))

    # Check for collision with walls
    x, y = snake[0].pos()
    if x < -300 or x > 300 or y < -300 or y > 300:
        GameOver()

    # Check for collision with barrier
    if snake[0].distance(barrier) < 15:
        scores -= 5 
        barrier.goto(random.randint(-280, 280), random.randint(-280, 280))  # Move the barrier
        score.clear()
        score.write(f"Score: {scores}  High Score: {high_score}", align="center", font=("Courier", 24, "bold"))

    # Randomly move the barrier to a new position every 5 seconds
    if random.randint(1, 50) == 1:
        barrier.goto(random.randint(-280, 280), random.randint(-280, 280))

screen.mainloop()
