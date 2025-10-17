# Author: Joe Nowakowski
# Date Created: 9/15/2025
# Last Modified: 9/17/2025

# The example program below is for accessing a commercial
# building for a new employee. Depending on the clearance level of their
# scanned badge, the new employee gets directions from terminal on where
# to start their day with the company based on their input from scanning
# their badge. The code simulates the badge scanner’s input.

print("""
        Welcome to the New Employee Terminal.
        You need some level of security clearance to 
        enter this building. Scan Your badge below and
        hit Enter on Keypad. 
      """)
clearance = 3  # simulating a scanner that read 3 for clearance

# Instructions
if clearance is None:
    print("Error. Please try again.")
elif clearance > 0:   # if clearance is 1 or higher
    print("Enter Bulding. Report to the Help Desk to sign in.")

    if clearance > 1:  # if clearance is 2 or higher
        print("Type in Employee Code For access to "
              "the employee section.")

        if clearance > 2:  # if clearance is 3 or higher
            print("Take Elevator to Level 2. Continue "
                  "in Accounting, straight down the hall. "
                  "Make a left, then a right.")
            if clearance == 3:  # if clearance is 3
                print("Look for a desk with your name "
                      "on a folder. It's a welcome packet. "
                      "Enjoy your new role in Accounting!")
            elif clearance == 4:  # if clearance is 4
                print("Report to the IT department. "
                      "Straight down the hall on other side "
                      "of Accounting, then two lefts.")
            elif clearance == 5:  # if clearance is 5
                print("Report to the Administrative Office."
                      "Straight down the hall. Make a right.")
            else:  # if clearance is 6 or higher
                print("Report to the executive suite. Enter "
                      "the elevator to the left of accounting as "
                      "soon as you enter Accounting. \nAt the end of "
                      "the hall, take elevator to Level 3. "
                      "Make a right. \nExecutive suite is through "
                      "the double doors at the end of the hall.")

        else:  # if clearance is 2
            print("Ask a supervisor for instructions. Get ready for work.")
    else:  # if clearance is 1
        print("Stay in the Lobby. Someone will be with you shortly.")
else:  # if clearance is 0
    print("Please vacate the premises. Call your supervisor if this is an error.")
