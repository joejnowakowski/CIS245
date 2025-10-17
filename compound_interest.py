# CIS245-T303 Introduction to Programming
# Module 3 Assignment
# Author: Joe Nowakowski
# Date Created: 9/25/2025

# Purpose:
# This program will calculate how many years an initial
# investment will take at a given annual interest rate to 
# double in value. The data will be given by the user. The output will 
# produce the year since initial investment, interested earned for
# that year, and the accumulated investment for that year in a tabular form.

# Initial notes:
# Get initial investment, validate input
# get annual interest rate, validate input
# calculate accumulated amount for each year; 
# have in while loop; terminated when accumulated 
# amount for last year is >=  double of initial investment

ini_invest_flag = False # flag to validate proper format entered for initial investment
while not ini_invest_flag:
    try:
        ini_investment = int(input("Please enter whole number amount of initial investment." 
        "\nIf your initial investment is $10,000, please enter 10000: "))
        ini_invest_flag = True # terminates while loop; input validated
    except:
        print("The initial investment is not a whole number in the correct format. Please enter " 
        "whole dollar amount only.Do not include '$' or commas in your initial investment entry.\n")

ini_interest_flag = False # flag to validate proper format entered for initial investment
while not ini_interest_flag:
    try: # try-except block; if code fails, it doesn't crash the program, instead except block is executed
        ini_interest = float(input("\nPlease enter the annual interest rate. \nIf the interest rate is 3%, please " 
        "enter whole number '3'.\nIf annual interest rate is 2.93%, please enter '2.93': "))
        if ini_interest >= 1:
            ini_interest_flag = True # terminates loop; valid input
        elif ini_interest == 0:
            print("Sorry, you can't have an annual interest rate of 0 for an investment.")
        elif ini_interest < 0:
            print("Sorry, an annual interest rate cannot be a negative number.")
        else:
            print("\nSorry, it seems you may have entered the actual interest rate. Please enter the " 
            "interest rate in terms of percentage.\n")
    except:
        print("\nSorry, you entered something other than a number. Please try again. Do not include " 
        "the '%' sign in the interest rate.\n")
                                
target_accum_investment = ini_investment * 2 # target accumulated investment; double the initial investment
accum_investment = ini_investment # initializes accumulated investment with initial investment
interest_rate = ini_interest / 100 # proper interest rate; not as a percentage
yrly_interest_earned = 0 # initializes yearly interested earned variable
years = 0 # initialized year count
five_rows = 0
# formatted heading for output; < is left-aligned and number is how many
# spaces that column is
print(f"\n{'Years':<8}{'Interest Earned':<17}{'Accumulated Investment'}")
print("-" * 47) # header divider
while accum_investment < target_accum_investment:
    yrly_interest_earned = accum_investment * interest_rate
    accum_investment += yrly_interest_earned # yearly interest earned to accumulated interest
    years += 1 # for each iteration of the while loop, increment year by 1
    five_rows += 1


    # formatted output; rounded to 2 decimals; fractions of pennies still used in actual calculations;
    # 16 space width is used instead of 20 like above header since $ was added
    print(f"{years:<8}${yrly_interest_earned:<16,.2f}${accum_investment:,.2f}")
    
    if five_rows % 5 == 0:
        print("-"*35) # added after every 5 entries for legibility
    
print(f"\nIt will take {years} years to double your investment.\n")