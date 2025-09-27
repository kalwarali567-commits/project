import turtle
from random import randint

turtle.speed(2)

turtle.color('red') # color for lattice

# ✅ Draw horizontal lines
x = -88
for y in range(88, -88 - 1, -10):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(168)


# ✅ Draw vertical lines
y = 88
turtle.right(90) # straight grid

for x in range(-88, 88 + 1, 10):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(168)

# ✅ Set pen size & color for random walk
turtle.pensize(3)
turtle.color('green')


turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

x = y = 0
# ✅ Now make continuous random walk until it hits border
while abs(x) < 88 and abs(y) < 88:
    r = randint(0, 3)# random direction 0–3

    if r == 0:# move right
        x += 10
        turtle.setheading(0)
        turtle.forward(10)

    elif r == 1: # move down
        y -= 10
        turtle.setheading(270)
        turtle.forward(10)

    elif r == 2:# move left
        x -= 10
        turtle.setheading(180)
        turtle.forward(10)


    elif r == 3:# move up
        y += 10
        turtle.setheading(90)
        turtle.forward(10)


turtle.done()