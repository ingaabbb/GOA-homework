from turtle import *

#paint a house

width(5)

# draw a square

color("purple")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#draw a door

forward(70)
color("yellow")
begin_fill()

left(90)
forward(110)

right(90)
forward(60)

right(90)
forward(110)

end_fill()

# draw a roof

penup()
goto(200,200)
pendown()

color("red")
begin_fill()

right(150)
forward(200)

left(120)
forward(200)

end_fill()

# draw windows

penup()
goto(10,130)
pendown()

color("blue")

begin_fill()

right(150)
forward(60)

right(90)
forward(60)

right(90)
forward(60)

right(90)
forward(60)

end_fill()

right(180)    #draw a line on window
forward(30)
left(90)

color("black")
forward(60)


left(90)

penup()
goto(190,130)
pendown()

color("blue")

begin_fill()

forward(60)
right(90)

forward(60)
right(90)

forward(60)
right(90)

forward(60)
right(90)

end_fill()

forward(30) # draw a line

color("black")
right(90)
forward(60)


exitonclick()