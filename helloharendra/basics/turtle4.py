from turtle import *

# Setup
bgcolor("black")
speed(0)
pensize(3)

# --------- GLOW CIRCLE DESIGN ---------
colors = ["red", "orange", "yellow", "green", "cyan", "blue", "purple"]

for i in range(60):
    pencolor(colors[i % len(colors)])
    circle(150)
    right(6)

# --------- HEART DESIGN ---------
penup()
goto(0, -50)
pendown()

color("red")
begin_fill()
left(50)
forward(133)
circle(50, 200)
right(140)
circle(50, 200)
forward(133)
end_fill()

# --------- BRAND NAME ---------
penup()
goto(0, -200)
pendown()

color("white")
write("Naya Prayog Academy", align="center", font=("Arial", 24, "bold"))

# --------- TAGLINE ---------
penup()
goto(0, -240)
pendown()

color("lightgreen")
write("Innovate • Learn • Grow", align="center", font=("Arial", 14, "normal"))

# Hide turtle
hideturtle()

done()