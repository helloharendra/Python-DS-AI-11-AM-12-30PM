from turtle import *
bgcolor("black")
speed(0)
pensize(3)

colors=["red","orange","yellow","green","cyan","blue","purple"]

for i in range(60):
    pencolor(colors[i % len(colors)])
    circle(150)
    right(6)


penup()
goto(0,-50)
pendown()

color("red")
begin_fill()
left(50)
forward(133)
circle(50,200)
forward(133)
end_fill()

penup()
goto(2,-200)
pendown()

color("white")
write("Roshan Yadav", align="right", font=("Arial", 24, "bold"))

penup()
goto(0,-240)
pendown()

color("lightgreen")
write("From Kanaila", align="center", font=("Arial", 14, "bold"))

hideturtle()

done()