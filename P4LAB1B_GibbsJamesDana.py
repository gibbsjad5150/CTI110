Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import turtle

# Set up the screen and turtle
... screen = turtle.Screen()
... t = turtle.Turtle()
... 
... # Set pen size and color
... t.pensize(3)
... t.color("red")
... 
... # Draw the first initial (e.g., "A")
... t.penup()
... t.goto(-100, 0)  # Move to start position
... t.pendown()
... 
... t.left(75)
... t.forward(100)
... t.right(150)
... t.forward(100)
... t.backward(50)
... t.right(105)
... t.forward(40)
... 
... # Move to position for second initial
... t.penup()
... t.goto(50, 0)
... t.pendown()
... 
... # Draw the second initial (e.g., "B")
... t.left(75)  # Reset orientation
... t.forward(100)
... t.right(90)
... for _ in range(18):  # Draw the top half-circle
...     t.forward(5)
...     t.right(10)
... t.right(180)
... for _ in range(18):  # Draw the bottom half-circle
...     t.forward(5)
...     t.right(10)
... 
... # Close on click
... screen.mainloop()
