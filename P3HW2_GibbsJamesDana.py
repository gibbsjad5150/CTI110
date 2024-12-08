Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
# Dana Gibbs-James
# Date: 12/8/2024
# Assignment Name: P3HW2
# A brief description: This program calculates an employee's pay based on hours worked, 
# including overtime pay, and displays details such as the name, pay rate, hours worked, 
# overtime hours, regular pay, overtime pay, and gross pay.

"""
Pseudocode:
1. Prompt user to enter the employee's name.
2. Prompt user to enter the number of hours worked this week.
3. Prompt user to enter the employee's pay rate.
... 4. Check if the employee worked overtime (more than 40 hours).
...     a. If yes, calculate overtime hours and overtime pay:
...        Overtime pay = overtime hours * pay rate * 1.5
... 5. Calculate pay for regular hours:
...     Regular pay = min(hours worked, 40) * pay rate
... 6. Calculate gross pay:
...     Gross pay = Regular pay + Overtime pay
... 7. Display the following details:
...     - Employee name
...     - Pay rate
...     - Number of hours worked
...     - Overtime hours
...     - Overtime pay
...     - Regular pay
...     - Gross pay
... """
... 
... # Step 1: Get inputs from the user
... employee_name = input("Enter the name of the employee: ")
... hours_worked = float(input("Enter the number of hours the employee worked this week: "))
... pay_rate = float(input("Enter the employee's pay rate: "))
... 
... # Step 2: Determine overtime and calculate pay
... overtime_hours = max(0, hours_worked - 40)
... overtime_pay = overtime_hours * pay_rate * 1.5
... regular_hours = min(hours_worked, 40)
... regular_pay = regular_hours * pay_rate
... gross_pay = regular_pay + overtime_pay
... 
... # Step 3: Display results
... print("\n--- Pay Details ---")
... print(f"Employee Name: {employee_name}")
... print(f"Pay Rate: ${pay_rate:.2f}")
... print(f"Hours Worked: {hours_worked}")
... print(f"Overtime Hours: {overtime_hours}")
... print(f"Overtime Pay: ${overtime_pay:.2f}")
... print(f"Regular Pay: ${regular_pay:.2f}")
... print(f"Gross Pay: ${gross_pay:.2f}")
