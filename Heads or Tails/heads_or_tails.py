"""The Heads or Tails Game."""
import random
import turtle


def toss_coin():
    """Tosses a coin and returns the result."""
    return random.choice(["Head", "Tail"])


def play_game():
    """Plays The Heads or Tails Game."""
    user_score = 0

    # create the screen
    screen = turtle.Screen()
    screen.setup(width=600, height=400)
    screen.title("The Heads or Tails Game")
    screen.bgcolor("black")

    # create the coin
    coin = turtle.Turtle()
    coin.shape("circle")
    coin.color("silver")
    coin.speed(0)
    coin.penup()
    coin.hideturtle()

    # create the text
    text = turtle.Turtle()
    text.color("blue")
    text.speed(0)
    text.penup()
    text.hideturtle()
    text.goto(0, 0)

    text.write("Welcome to the Heads or Tails Game!")
    rounds = screen.textinput("Heads or Tails Game",
                              "Enter number of rounds you want to play: ")
    # print("Let's start!\n")

    for toss in range(1, rounds + 1):
        screen.clear()
        coin.goto(0, 0)
        coin.stamp()

        text.write(f"Round {toss}\n Pick 'Head' or 'Tail': ",
                   align="center",
                   font=("Arial", 20, "bold"))
        user_choice = screen.textinput("'Heads' or 'Tails'", "").capitalize()

        while user_choice not in ["Head", "Tail"]:
            user_choice = screen.textinput("Heads or Tails",
                                           "Pick 'Head' or 'Tail': "
                                           ).capitalize()

        if user_choice == toss_coin():
            user_score += 1
            text.write("You guessed right!\n",
                       align="center",
                       font=("Arial", 20, "bold"))
        else:
            text.write("You guessed wrong!\n",
                       align="center",
                       font=("Arial", 20, "bold"))

        turtle.delay(1000)

    screen.clear()
    text.goto(0, 0)
    text.write(f"Game Over!\nYour final score: {user_score}",
               align="center",
               font=("Arial", 20, "bold"))

    screen.exitonclick()


if __name__ == "__main__":
    play_game()
