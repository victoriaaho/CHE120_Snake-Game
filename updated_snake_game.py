@ -0,0 +1,117 @@
from random import randrange
from turtle import *
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

def start_game():
    """Initialize the game loop by starting the movement and drawing the border."""
    screen = Screen()
    screen.bgpic('grass.gif')
    clear()
    draw_border()  # Draw the border after clearing the welcome screen
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move(True)  # Pass True to indicate the game has started

def show_welcome_screen():
    """Display the welcome message and wait for player input to start."""
    screen = Screen()
    screen.bgpic('background.gif')
    clear()
    update()
    listen()
    onkey(start_game, 's')  # Press 's' to start
    
def draw_border():
    """Draw a visible border around the play area."""
    penup()
    goto(-200 - 5, 200 + 5)  #ajust
    pendown()
    pencolor("white")  # Color for the border
    width(4)  # Border thickness

    for _ in range(4):#4 iterations - creates the square with 4 sides
        forward(390)  # Move forward to create a side of the square
        right(90)     # Turn right 90 degrees to create the next side

    penup()  # Lift the pen after drawing
    width(1)  # Reset pen width to default
    
def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190


def move(game_started):
    """Move snake forward one segment if game has started."""
    if not game_started:
        return

    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'white')
        update()
        ontimer(game_over,1000)
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()
    draw_border()  # Draw the border only after the game starts

    for body in snake:
        square(body.x, body.y, 9, '#286b0a')

    square(food.x, food.y, 9, '#f10000')
    update()
    ontimer(lambda: move(game_started), 100)

def game_over():
    """display game over screen and wait for player to descid whether to restart or quit"""
    screen = Screen()
    screen.bgpic('game_over.gif')
    clear()
    update()
    
    listen()
    onkey(restart_game, 'r')
    onkey(quit_game, 'q')
    
def restart_game(): 
    """shows the welcome screen again"""
    global food, snake, aim #global refers to variables defines outside of the local function
    food = vector(0, 0) #resetting the positions
    snake = [vector(10, 0)]
    aim = vector(0, -10)
    show_welcome_screen() #calling the function to display screen
    
def quit_game():
    """exits the game"""
    bye()
    
setup(600, 600, 0, 0)
hideturtle()
tracer(False)
show_welcome_screen()
done()