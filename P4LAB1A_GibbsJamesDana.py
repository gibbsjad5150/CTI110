Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
... 
... # Set up the screen and turtle
... screen = turtle.Screen()
... t = turtle.Turtle()
... 
... # Draw a square using a for loop
... t.color("blue")
... for _ in range(4):
...     t.forward(100)  # Move forward 100 units
...     t.right(90)     # Turn right 90 degrees
... 
... # Move the turtle to a different position
... t.penup()
... t.goto(-50, -50)
... t.pendown()
... 
... # Draw a triangle using a while loop
... t.color("green")
... count = 0
... while count < 3:
...     t.forward(100)  # Move forward 100 units
...     t.left(120)     # Turn left 120 degrees
...     count += 1
... 
... # Close on click
... screen.mainloop()
