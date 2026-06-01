import turtle

# Setup screen
screen = turtle.Screen()
screen.title("Simple Sketch App")
screen.bgcolor("white")

pen = turtle.Turtle()
pen.speed(0)
pen.width(3)

# -------- DRAWING --------
def draw(x, y):
    pen.goto(x, y)

def pen_up():
    pen.penup()

def pen_down():
    pen.pendown()

# -------- COLORS --------
def set_black():
    pen.color("black")

def set_red():
    pen.color("red")

def set_blue():
    pen.color("blue")

def set_green():
    pen.color("green")

# -------- CLEAR --------
def clear_screen():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

# -------- EVENTS --------
screen.listen()

# Mouse drag to draw
screen.onscreenclick(lambda x, y: pen.goto(x, y))
screen.onkey(pen_up, "u")     # press U to lift pen
screen.onkey(pen_down, "d")   # press D to draw

# Color keys
screen.onkey(set_black, "1")
screen.onkey(set_red, "2")
screen.onkey(set_blue, "3")
screen.onkey(set_green, "4")

# Clear
screen.onkey(clear_screen, "c")

# Hide turtle cursor
pen.hideturtle()

turtle.done()