Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Dana Gibbs-James
... # 12/3/2024
... # Dictionary
... # This program creates a dictionary of vehicles and their MPG values. It allows the user to select a vehicle, input miles driven, and calculates the gallons of gas needed.
... 
... # Step 1: Create the dictionary
... vehicles = {
...     "Camaro": 18.21,
...     "Prius": 52.36,
...     "Model S": 110,
...     "Silverado": 26,
... }
... 
... # Step 2: Get the keys from the dictionary
... keys = vehicles.keys()
... print("Available vehicles:", keys)
... 
... # Step 3: Prompt the user to enter a vehicle
... vehicle = input("Enter a vehicle to see its MPG: ")
... 
... # Step 4: Check if the vehicle exists in the dictionary
... if vehicle in vehicles:
...     mpg = vehicles[vehicle]
...     print(f"The {vehicle} gets {mpg} mpg.")
... 
...     # Step 5: Prompt the user for miles to be driven
...     miles = float(input(f"How many miles will you drive the {vehicle}? "))
... 
...     # Step 6: Calculate gallons of gas needed
...     gallons = miles / mpg
...     print(f"{gallons:.2f} gallon(s) of gas are needed to drive the {vehicle} {miles:.1f} miles.")
... else:
...     print("Vehicle not found. Please make sure to enter the name exactly as listed.")
