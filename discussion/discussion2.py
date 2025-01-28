# Your name: Leah Kim
# Class : SI 206 003
# Your email: leahgk@umich.edu

import turtle



def draw_emoji(t):
    """
    Draw a smiling face emoji using the passed turtle.
    """
    # Draw the face
    t.penup()
    t.goto(0, -150)
    t.pendown()
    t.begin_fill()
    t.color("yellow")
    t.circle(150)  
    t.end_fill()

    #Left eye
    t.penup()
    t.goto(-60, 30)
    t.pendown()
    t.begin_fill()
    t.color("black")
    t.circle(20)
    t.end_fill()

    #Right eye
    t.penup()
    t.goto(60, 30)
    t.pendown()
    t.begin_fill()
    t.color("black")
    t.circle(20)
    t.end_fill()

    #Mouth
    t.penup()
    t.goto(-70, -20)
    t.setheading(-60)
    t.pendown()
    t.pensize(5)
    t.circle(80, 120) 
    t.penup()
    t.hideturtle()


def main():
    """
    Create a Screen object, a Turtle object, and draw the emoji.

    Also, the program exits when you click on the screen.
    """
    screen = turtle.Screen()
    screen.bgcolor("lightpink")
    screen.title("Leah Kim Emoji")

    t = turtle.Turtle()
    t.speed(5)

    draw_emoji(t)

    screen.exitonclick()


if __name__ == '__main__':
    main()