import turtle

# Take input for the circle center (x1, y1)
x1, y1 = eval(input("Enter the center of circle (x1, y1): "))

# Take input for the radius of the circle
radius = int(input("Enter the radius of circle: "))

# Take input for the point (x2, y2) to check if it's inside or outside the circle
x2, y2 = eval(input("Enter the point coordinates (x2, y2): "))

# Draw the circle
turtle.penup()
turtle.goto(x1, y1 - radius)   # Move to bottom of circle to start drawing
turtle.pendown()
turtle.circle(radius)

# Draw the point as a small red filled circle
turtle.penup()
turtle.goto(x2, y2)
turtle.pendown()
turtle.begin_fill()
turtle.color('red')
turtle.circle(3)   # Small circle to represent the point
turtle.end_fill()

# Move turtle to a position for text (optional, not printing text here)
turtle.penup()
turtle.goto(x1 - 70, y2 - radius - 20)
turtle.pendown()

# Calculate distance between circle center and the point
d = ((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1)) ** 0.5

# Check if the point lies inside or outside the circle
if d <= radius:
    print("The point is inside the circle")
else:
    print("The point is outside the circle")

# Hide the turtle cursor
turtle.hideturtle()

# Keep the window open until closed manually
turtle.done()
