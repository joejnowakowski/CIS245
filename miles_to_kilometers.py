# CIS 245 Introduction to Programming Fall '25
# Author: Joe Nowakowski
# Date Created: 9/30/2025
#
# Purpose: This program will convert the user's input of total miles driven
# and convert that to kilometers, then displays miles and kilometers to user.


def main():
    """Main function.
    
        Gets miles from user. Converts to Km and displays conversion to user.
        """
    intro()
    miles = get_miles()
    kilometers = convert_mi_to_km(miles)
    print(f"You have driven {miles:,} miles which converts to {kilometers:,} kilometers.")    

def get_miles():
    """Gets The miles from user.

       Validates input to be in proper format 
    """
    valid_input = False # flag for while loop

    while not valid_input:
        try:
            miles = float(input("Please enter the number of miles you have driven: "))
            valid_input = True # valid input received
        except ValueError:
            print("You have entered invalid input. Please enter a number; digits only. " 
            "Negative numbers are accepted as well decimal points.")
    return miles

def convert_mi_to_km(miles):
    """Converts miles to kilometers.
    
        Uses conversion factor of 1.60934."""
    MI_TO_KM = 1.60934
    kilometers = miles * MI_TO_KM
    return kilometers

def intro():
    """Introduction to mi to km conversion program.
    
        Displays conversion factor and informs user negative numbers and decimal places
        are allowed, commas are not for input.
    """
    print("Welcome to the distance conversion program for miles to kilometers."
    "This program uses the conversion factor: 1 mi = 1.60934 km. Negative numbers"
    "are accepted as well as decimal places (e.g. 2.75 mi). Please exclude commas"
    "as separators.")


if __name__ == "__main__":
    main()