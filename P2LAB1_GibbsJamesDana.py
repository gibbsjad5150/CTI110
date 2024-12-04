Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Dana Gibbs-James
... # Date: 12/3/2024
... # Variable and Expressions
... # This program calculates the diameter, circumference, and area of a circle
... # based on a user-provided radius and displays the results with specific formatting.
... 
... import math
... 
... # Get the radius from the user
... radius = float(input("Enter the radius of the circle: "))
... 
... # Calculate the diameter, circumference, and area
... diameter = 2 * radius
... circumference = 2 * math.pi * radius
... area = math.pi * radius**2
... 
... # Display the results with the specified formatting
... print(f"The diameter of the circle is {diameter:.1f}")
... print(f"The circumference of the circle is {circumference:.2f}")
