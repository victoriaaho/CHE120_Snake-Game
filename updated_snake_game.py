from random import randrange
from turtle import *
from freegames import square, vector

# Global variables for the game
level = 1
food = vector(0, 0) # Initial position of food
snake = [vector(10, 0)] # Initial position of snake
aim = vector(0, -10) # Snake movement direction
food_eaten = 0 # Tracks the number of food items eaten

# Score and level displays
score_disp = Turtle()
score_disp.hideturtle()
score_disp.color('green')
score_disp.penup()
score_disp.goto(0, 260)

level_disp = Turtle()
level_disp.hideturtle()
level_disp.color('green')
level_disp.penup()
level_disp.goto(0, 230)

def start_game():
    """Initialize the game loop by starting the movement and drawing the border."""
    global level #Make global variable - make sure it's updated globally
    screen = Screen()
    screen.bgpic('grass.gif') 
    clear()
    draw_border()  # Draw the border after clearing the welcome screen
   
    # Score and Level display
    score_disp.clear()
    score_disp.write("Score: 0", align="center", font=("Courier New", 16, "normal"))
    
    level_disp.clear()
    level_disp.write("Level: 1", align="center", font=("Courier New", 16, "normal"))
    
    listen()
    onkey(lambda: change(10, 0), 'Right')
    onkey(lambda: change(-10, 0), 'Left')
    onkey(lambda: change(0, 10), 'Up')
    onkey(lambda: change(0, -10), 'Down')
    move(True)  # Pass True to indicate the game has started (start game loop)

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
    goto(-200 - 5, 200 + 5)  #Ajust
    pendown()
    pencolor("white")  # Color for the border
    width(4)  # Border thickness

    for _ in range(4):#4 iterations - creates the square with 4 sides
        forward(390) # Move forward to create a side of the square
        right(90) # Turn right 90 degrees to create the next side

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

    global level, food_eaten
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'black')
        update()
        ontimer(game_over,1000)
        return

    snake.append(head)

    #Check if the snake eats the food
    if round(head.x, 1) == round(food.x, 1) and round(head.y, 1) == round(food.y, 1):
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        
        food_eaten += 1
        score_disp.clear()
        score_disp.write(f"Score: {food_eaten}", align="center", font=("Courier New", 16, "normal"))

        # Update level after every 5 foods eaten
        new_level = food_eaten//1 + 1 # Starting levels from level 1
        if new_level > level:
            level = new_level
            level_disp.clear()
            level_disp.write(f"Level: {level}", align="center", font=("Courier New", 16, "normal"))
    
    else:
        snake.pop(0)
        
    if level == 10:
        ontimer(win_game, 1000)
        return 
        
    
    clear()
    draw_border()  # Draw the border only after the game starts

    
    for body in snake:
        square(body.x, body.y, 9, '#286b0a')

    square(food.x, food.y, 9, '#f10000')
    update()
    ontimer(lambda: move(game_started), 100)

def win_game():
    # Clear the score and level display for the winner page
    score_disp.clear()
    level_disp.clear()
    
    screen = Screen()
    screen.bgpic('winner.gif')
    clear()
    update()
    
    listen()
    onkey(restart_game, 'p')
    onkey(quit_game, 'q')
    
def game_over():
    """display game over screen and wait for player to descid whether to restart or quit"""
    screen = Screen()
    screen.bgpic('game_over.gif')
    clear()
    update()
    
    # Clear the score and level display so it does not show up for the game over screen
    score_disp.clear() 
    level_disp.clear()
    
    listen()
    onkey(restart_game, 'r')
    onkey(quit_game, 'q')
    
def restart_game(): 
    """shows the welcome screen again"""
    global food, snake, aim, level, food_eaten #global refers to variables defines outside of the local function - reset them
    # Resetting all positions
    food = vector(0, 0) 
    snake = [vector(10, 0)]
    aim = vector(0, -10)
    level = 1
    food_eaten = 0 # Reset the food counter
    score_disp.clear()
    level_disp.clear()
    
    show_welcome_screen() #calling the function to display screen
    
def quit_game():
    """exits the game"""
    bye()
    
setup(600, 600, 0, 0)
hideturtle()
tracer(False)
show_welcome_screen()
done()
