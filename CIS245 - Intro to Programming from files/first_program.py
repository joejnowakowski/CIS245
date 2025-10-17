# M1: Assignment 2 - Your First Python Program
# Author: Joe Nowakowski
# Date Created: 9/7/2025

# This program calculates the total cost of the number
# of feet of fiber optic cable needed for a project.

COST_PER_FOOT = 0.87  # Cost of fiber optic cable per foot
COST_OVER_100FT = .80  # Cost per foot if over 100ft
COST_OVER_250FT = .70  # Cost per foot if over 250ft
COST_OVER_500FT = .50  # Cost per foot if over 500ft
correct_input = False  # Flag for valid input

print("Welcome to the Fiber Optic Cable Cost Calculator!\n")

# Loop through until valid input is received
while not correct_input:
    try:
        # Get the number of feet of cable needed from the user
        f_optic_cable_ft = float(
            input("Please enter the number of feet of fiber optic cable to be used: "))
        if f_optic_cable_ft < 0:
            print("Error: Please enter a positive number.\n")
        else:
            correct_input = True  # Valid input, break out of while loop
    except ValueError:
        print("Sorry, that is not a valid input. Please enter a a positive number.\n")

# Calculate the total cost
if f_optic_cable_ft <= 100:
    total_cost = f_optic_cable_ft * COST_PER_FOOT
elif f_optic_cable_ft <= 250:
    total_cost = f_optic_cable_ft * COST_OVER_100FT
elif f_optic_cable_ft <= 500:
    total_cost = f_optic_cable_ft * COST_OVER_250FT
else:
    total_cost = f_optic_cable_ft * COST_OVER_500FT

# Display the total cost to the user
print(f"\nThe total cost for {f_optic_cable_ft} feet of fiber optic cable " +
      # total cost formatted to 2 decimal places and also with commas where applicable
      f"is ${total_cost:,.2f}.\n")


# End of program message
print("Thank you for using the Fiber Optic Cable Cost Calculator!")
