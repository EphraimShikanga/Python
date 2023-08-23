"""Creates the screen and the coins for the Heads or Tails game"""
import turtle
import random


def create_screen():
    """Create the screen"""
    turtle.Screen().listen()
    screen = turtle.Screen()
    screen.setup(width=720, height=400)
    screen.title("The Heads or Tails Game")
    screen.bgcolor("black")
    return screen


def create_text(txt, colours, x_coordinate=0, y_coordinate=0, font_size=20):
    """Create the text"""
    text = turtle.Turtle()
    text.hideturtle()
    text.color(colours)
    text.speed(1)
    text.penup()
    text.goto(x_coordinate, y_coordinate)
    text.write(txt, align="center", font=("Arial", font_size, "bold"))


def draw_circle(color, x_coordinate, y_coordinate, radius):
    """Draw a circle"""
    circle = turtle.Turtle()
    circle.penup()
    circle.fillcolor(color)
    circle.goto(x_coordinate, y_coordinate - radius)
    circle.pendown()
    circle.begin_fill()
    circle.circle(radius)
    circle.end_fill()


def draw_heads_coin():
    """Draw the heads coin"""
    heads_coin = turtle.Turtle()
    heads_coin.speed(100)

    # Draw the coin
    draw_circle("gold", 0, 0, 100)
    draw_circle("saddle brown", 0, 0, 80)
    heads_coin.penup()
    heads_coin.goto(-30, 0)
    heads_coin.pendown()
    heads_coin.write("Heads", font=("Arial", 20, "bold"))
    heads_coin.hideturtle()


def _draw_tails_coin():
    """Draw the tails coin"""
    tails_coin = turtle.Turtle()
    tails_coin.speed(100)

    # Draw the coin
    draw_circle("gold", 0, 0, 100)
    draw_circle("saddle brown", 0, 0, 80)
    tails_coin.penup()
    tails_coin.goto(-30, 0)
    tails_coin.pendown()
    tails_coin.write("Tails", font=("Arial", 20, "bold"))
    tails_coin.hideturtle()
    # turtle.done()


def toss_coin():
    """Tosses a coin and returns the result."""
    return random.choice(["Head", "Tail"])


def get_rounds():
    """Gets the number of rounds the user wants to play."""
    rounds = turtle.numinput("Number of Rounds",
                              "Enter number of rounds you want to play: ")
    if rounds is None:
        turtle.bye()
    else:
        rounds = int(rounds)
    
    return rounds


def play_game():
    """Plays The Heads or Tails Game."""
    create_screen()
    create_text("Welcome to the Heads or Tails Game!", 'green')
    create_text("Click anywhere to start the game.", 'green', 0, -50, 15)
    turtle.onscreenclick(get_rounds())




if __name__ == "__main__":
    play_game()
    turtle.exitonclick()
