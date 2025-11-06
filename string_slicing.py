# Course: CIS245 - Introduction to Programming
# Instructor: Dr. Azizian
# Author: Joe Nowakowski
# Date Created: 10/19/2025
# Date Last Modified: 10/20/2025

# Purpose: Take input from user, asking for full name. The full name is validated. 
#          The program outputs initials of full name in proper format.


def main():
    """
    Main Function

    Gets full name and prints initials. Accepts more than 3 names in full name.
    """
    full_name = get_full_name()
    initials = get_initials(full_name)
    print(initials)


def get_full_name():
    """
    Gets full name.
    
    Validates full name entered by making sure each character is alphabetical and returns full name.
    """
    while True:
        try:
            full_name = input("Please enter your full name: ")
            names = full_name.split()
            for name in names:      # takes each name from full name
                for ch in name:     
                    if ch.isalpha(): # checks each character to ensure each name only contains letters
                        pass
                    else:
                        raise ValueError # if not a letter, raises Value Error
            return full_name # breaks while loop if all characters in all names are letters
                             # and returns full name
                    
            
        except ValueError: # the Value Error raised
            print("Please enter your name only")   # message printed for Value Error

 
def get_initials(full_name):
    """
    Gets initials from full name parameter.

    Ensures that each initial is capitalized and returns all initials.
    """

    initials ="" # initializes variable "initials" as empty string
 
    names = full_name.split() 
    for name in names: # looks at each name in names list
        initials += f"{name[0].title()}. " # adds first letter of each name followed by a 
                                           # # period and a space
    return initials  # returns formatted string of initials                      


if __name__ == "__main__": # Guard
    main()