Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Dana Gibbs-James
... # Date: 12/3/2024
... # P2HW1
... # A brief description of the project: This program calculates and displays travel expenses
... # in a nicely formatted table with user-specified amounts and destination.
... 
... # Prompt the user for input
... initial_budget = float(input("Enter Budget: "))
... destination = input("Enter your travel destination: ")
... gas_cost = float(input("How much do you think you will spend on gas? "))
... hotel_cost = float(input("Approximately, how much will you need for accommodation/hotel? "))
... food_cost = float(input("Last, how much do you need for food? "))
... 
... # Calculate the remaining balance
... remaining_balance = initial_budget - (gas_cost + hotel_cost + food_cost)
... 
... # Display the travel expenses
... print("\n------------Travel Expenses------------")
... print(f"{'Location:':<20}{destination}")
... print(f"{'Initial Budget:':<20}${initial_budget:,.2f}")
... print(f"{'Fuel:':<20}${gas_cost:,.2f}")
... print(f"{'Accommodation:':<20}${hotel_cost:,.2f}")
... print(f"{'Food:':<20}${food_cost:,.2f}")
... print("---------------------------------------")
... print(f"{'Remaining Balance:':<20}${remaining_balance:,.2f}")
