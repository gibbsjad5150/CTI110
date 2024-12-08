Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
#Dana GibbsJames
#12/8/2024
#P4HW2
#Edit and enhance programs

# Pseudocode:
# 1. Initialize variables:
#    - total_overtime_pay = 0
#    - total_regular_pay = 0
#    - total_gross_pay = 0
#    - num_employees = 0
#
# 2. Print a header for the program.
#
# 3. Start a loop to process employee data:
#    a. Ask the user to input the employee's name or "Done" to terminate:
#       - If the input is "Done" (case-insensitive), break the loop.
#    b. Ask the user to input the employee's hourly pay rate and hours worked:
#       - Validate inputs (ensure they are numeric); if not, show an error and ask again.
#
# 4. Calculate the employee's pay:
#    a. If hours worked > 40:
#       - Calculate overtime hours as hours_worked - 40
#       - Calculate overtime pay as overtime_hours * (pay_rate * 1.5)
#       - Calculate regular pay as 40 * pay_rate
#    b. Otherwise:
#       - Overtime hours = 0
#       - Overtime pay = 0
#       - Calculate regular pay as hours_worked * pay_rate
#    c. Calculate gross pay as regular_pay + overtime_pay
#
# 5. Display the individual employee's summary:
#    - Include hours worked, pay rate, overtime pay, regular pay, and gross pay.
#
# 6. Update totals:
#    - Add overtime_pay to total_overtime_pay
#    - Add regular_pay to total_regular_pay
#    - Add gross_pay to total_gross_pay
#    - Increment num_employees by 1
#
# 7. After exiting the loop, display the final summary:
#    - Total number of employees entered
#    - Total overtime pay
#    - Total regular pay
#    - Total gross pay

# Initialize variables
total_overtime_pay = 0
total_regular_pay = 0
total_gross_pay = 0
num_employees = 0

print("Employee Pay Calculator\n")

while True:
    # Ask for employee name or termination
    employee_name = input("Enter employee's name or 'Done' to terminate: ")
    if employee_name.lower() == 'done':
        break
    
    # Get pay rate and hours worked
    try:
        pay_rate = float(input(f"Enter {employee_name}'s hourly pay rate: $"))
...         hours_worked = float(input(f"Enter number of hours worked by {employee_name}: "))
...     except ValueError:
...         print("Invalid input. Please enter numeric values for pay rate and hours worked.")
...         continue
... 
...     # Calculate pay
...     if hours_worked > 40:
...         overtime_hours = hours_worked - 40
...         overtime_pay = overtime_hours * (pay_rate * 1.5)
...         regular_pay = 40 * pay_rate
...     else:
...         overtime_hours = 0
...         overtime_pay = 0
...         regular_pay = hours_worked * pay_rate
... 
...     gross_pay = regular_pay + overtime_pay
... 
...     # Display individual employee details
...     print(f"\nSummary for {employee_name}:")
...     print(f"  Hours Worked: {hours_worked:.2f}")
...     print(f"  Pay Rate: ${pay_rate:.2f}")
...     print(f"  Overtime Pay: ${overtime_pay:.2f}")
...     print(f"  Regular Pay: ${regular_pay:.2f}")
...     print(f"  Gross Pay: ${gross_pay:.2f}\n")
... 
...     # Update totals
...     total_overtime_pay += overtime_pay
...     total_regular_pay += regular_pay
...     total_gross_pay += gross_pay
...     num_employees += 1
... 
... # Display final totals
... print("\nTotal Summary:")
... print(f"  Number of employees entered: {num_employees}")
... print(f"  Total Overtime Pay: ${total_overtime_pay:.2f}")
... print(f"  Total Regular Pay: ${total_regular_pay:.2f}")
... print(f"  Total Gross Pay: ${total_gross_pay:.2f}")
