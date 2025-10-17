# Course: CIS245-Introduction to Programming
# Instructor: Dr. Azizian
# Author: Joe Nowakowski
# Date Created: 10/09/2025
# Date Modified: 10/12/2025

# Purpose: Retrieve input from user for file to write to, their name,
# address, and phone number. Write to the file these inputs, respectively,
# as a comma-separated entry, then print out the contents of chosen file.

def main():
    """
    Main function
    
    gets filename to open, user's name, address, and phone number from user.
    Then writes that information to the file and reads back the contents of said
    file.
    """
    file = get_file_name()
    name = get_user_name()
    address = get_user_address()
    phone_number = get_user_phone_number()
    write_to_file(file, name, address, phone_number)
    read_file(file)


def get_file_name():
    """
    gets file name

    Prompts user for the file name and validates response.
    """
    while True:
        file = input("Please enter the file name you would like to use: ").strip()
        if not file:
            print("Filename cannot be blank. Try again.")
            continue

        # If no dot at all, append .txt
        if "." not in file:
            return file + ".txt"

        # Split once from the right: base . ext
        base, ext = file.rsplit(".", 1)

        # Ensures file has a name and extension before returning
        if base and ext:
            return file

        print("Sorry, that's not a correct format (e.g., 'file.txt'). Please try again.")

def get_user_name():
    """
    Gets user's name
    
    Validates input in case all numbers are entered, or nothing was typed and user hit enter.
    """
    while True:
        name = input("Please enter your name: ").strip()
        if not name:
            print("Sorry, please don't leave your name blank.")
        elif name.isdigit():  # if whole name is all digits, reject input
            print("Please enter your name and not a number.")
        else:
            return name.title()


def get_user_address():
    """
    Gets user's address
    
    Validates street address to have at least 2 parts (number and street name), 
    that something was entered, and that the first character is a number.
    
    """
    while True:
        address = input("Please enter your street address: ").strip()
        parts = address.split()

        # Need at least a house number and a street name
        if len(parts) < 2:
            print("Please enter the number of the residence, followed by the street name.")
            continue

        # First token should start with a digit (allows 13A, 221B, etc.)
        if parts[0] and parts[0][0].isdigit():
            return address.title()

        print("Please start with the house/building number (e.g., '123 Main St' or '13A Elm St').")


def get_user_phone_number():
    """
    Prompts user for their phone number.

    Validates proper format
    """
    while True:
        number = input("Please enter your phone number like so, 570-555-1234: ").strip()
        parts = number.split("-")

        if len(parts) == 3 and all(p.isdigit() for p in parts) \
           and len(parts[0]) == 3 and len(parts[1]) == 3 and len(parts[2]) == 4:
            return number

        print("Invalid phone number structure. Please enter it like: 570-555-1234.")


def write_to_file(file, name, address, phone_number):
    """Writes to give filename
    
    Appends comma separated entries in readable format whether if they're the first entry or not
    """
    with open(file,"a+") as f:
        f.seek(0) # brings pointer to beginning of file
        if f.readlines() == []:
            f.write(f"{name}, {address}, {phone_number}") # if first entry
        else:
            f.write(f"\n{name}, {address}, {phone_number}") # if not first entry, adds a newline character to keep the file legible

def read_file(file):
    """
    Reads file

    Prints contents of file.
    """
    with open(file, "r") as f:
        contents = f.read()
        print(contents)

if __name__ == "__main__":
    main()