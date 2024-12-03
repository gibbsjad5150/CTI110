Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Dana Gibbs-James
# Date : 12/2/2024
# P1HW2
# A brief description of the project: This program calculates and displays the total travel expenses and the remaining budget after deducting the expenses.

# Program starts here
def main():
...     # Asking user for inputs
...     print("Welcome to the Travel Budget Calculator!\n")
...     budget = float(input("Enter your budget: $"))
...     destination = input("Enter your travel destination: ")
...     gas_expense = float(input("Enter amount you will spend on gas: $"))
...     accommodation_expense = float(input("Enter amount you will spend on accommodation: $"))
...     food_expense = float(input("Enter amount you will spend on food: $"))
...     
...     # Calculations
...     total_expenses = gas_expense + accommodation_expense + food_expense
...     remaining_budget = budget - total_expenses
...     
...     # Display results
...     print("\nTravel Expenses:")
...     print(f"Destination: {destination}")
...     print(f"Initial Budget: ${budget:.2f}")
...     print(f"Total Expenses: ${total_expenses:.2f}")
...     print(f"Remaining Budget: ${remaining_budget:.2f}")
... 
... # Call the main function
... if __name__ == "__main__":
...     main()
...     
SyntaxError: invalid syntax
>>> 1. Start
... 2. Display a welcome message
... 3. Prompt user to enter their budget
... 4. Prompt user to enter their travel destination
... 5. Prompt user to enter the amount they will spend on gas
... 6. Prompt user to enter the amount they will spend on accommodation
... 7. Prompt user to enter the amount they will spend on food
... 8. Calculate total expenses as sum of gas, accommodation, and food
... 9. Calculate remaining budget by subtracting total expenses from budget
... 10. Display travel destination
... 11. Display budget
... 12. Display total expenses
... 13. Display remaining budget
... 14. End
