# Author: Joe Nowakowski
# Date Created: 9/29/25
# Purpose: Program created to convert gallons from user input
#          to liters with modularization in mind. 



def main():
    """
    Run the gallons-to-liters program.

    Includes introduction, input validation, and displays the output to the user.
    """ 
    # Above is a docstring that explains what and why function is created
    display_intro()
    gal_amt =  get_gallons_from_user()
    convert_gallons_to_liters(gal_amt)

def display_intro():
    """Display the introduction of program that converts gallons to liters.
       
      Prints a message that includes the conversion factor:
      1 gallon = 3.78541 liters. 
    """
    intro_display = "This program converts measurements in gallons to liters. " \
                    "For your reference the formula is: 1 gallon = 3.78541 liters."
    print(intro_display)

def get_gallons_from_user():
    """Get number of gallons from user.

       Accepts user input as a float(2.5 for example). If invalid input entered,
       prints out error message and reiterates while loop.
    """
    # loop for input validation
    while True:
        try:
            gallons_to_convert = float(input("Enter the number of gallons: "))
            if gallons_to_convert < 0:
                print("Invalid input. Please enter a positive number.\n")
            else:
                return gallons_to_convert # only returned if valid input
        except ValueError:
            print("Invalid input. Please enter a number.\n")

def convert_gallons_to_liters(gal):
    """Convert gallons to liters.
    
       Uses formula 1 gallon = 3.78541 liters.
       Prints out liters to four decimal places.
    """
    liters = gal * 3.78541
    print(f"{gal} gallons is equivalent to {liters:.4f} liters round to 4 decimal places.\n")




# Run main() only if this file is executed directly, not when imported.
if __name__ == "__main__":
    main()