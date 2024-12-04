Python 3.13.0 (v3.13.0:60403a5409f, Oct  7 2024, 00:37:40) [Clang 15.0.0 (clang-1500.3.9.4)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Dana Gibbs-James
>>> #12/3/2024
>>> #P2HW2
>>> #Lists
>>> 
>>> # Pseudocode:
... # 1. Prompt the user to input grades for six modules.
... # 2. Store each grade in a list called `module_grades`.
... # 3. Calculate and store the following:
... #    - Lowest grade in the list.
... #    - Highest grade in the list.
... #    - Sum of all grades in the list.
... #    - Average of the grades in the list.
... # 4. Display the results in the specified format with proper spacing and precision.
... 
... # Step 1: Prompt user for grades and store in a list
... module_grades = []  # Descriptive name for the list
... 
... for i in range(1, 7):  # Loop for six modules
...     grade = float(input(f"Enter grade for Module {i}: "))
...     module_grades.append(grade)
... 
... # Step 2: Calculate required values
... lowest_grade = min(module_grades)
... highest_grade = max(module_grades)
... sum_of_grades = sum(module_grades)
... average_grade = sum_of_grades / len(module_grades)
... 
... # Step 3: Display the results in the specified format
... print("\n" + "-" * 30 + "Results" + "-" * 30)
... print(f"Lowest Grade: {lowest_grade:.1f}")
... print(f"Highest Grade: {highest_grade:.1f}")
... print(f"Sum of Grades: {sum_of_grades:.1f}")
... print(f"Average: {average_grade:.2f}")
... print("-" * 66)
