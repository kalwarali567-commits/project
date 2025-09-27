import turtle  # Import the turtle graphics module

turtle.pensize(3)  # Set the thickness of the drawing pen

# Draw a triangle
turtle.penup()  # Lift the pen to move without drawing
turtle.goto(-200, -50)  # Move to starting position
turtle.pendown()  # Put the pen down to start drawing
turtle.circle(40, steps = 3)  # Draw a polygon with 3 sides (triangle)

# Draw a square
turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps=4)  # Polygon with 4 sides (square)

# Draw a pentagon
turtle.penup()
turtle.goto(8, -50)
turtle.pendown()
turtle.circle(40, steps=5)  # Polygon with 5 sides (pentagon)

# Draw a hexagon
turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.circle(40, steps=6)  # Polygon with 6 sides (hexagon)

# Draw a circle
turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.circle(40)  # Draw a perfect circle (default 360 steps)

turtle.done()  # Finish the turtle drawing window
