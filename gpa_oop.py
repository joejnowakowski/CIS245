# Course: CIS 245: Introduction to Programming
# Instructor: Dr. Azizian
# Author: Joe Nowakowski
# Date Created: 11/3/2025
# Date Last Modified: 11/6/2025

"""
Purpose: This program gets input from the user for getting the user's first and last names, creates
         a Student object from values, asks for course name, then gets course credits, and then letter grade
         to convert to a Course GPA. The courses are looped until user is done. The cumulative grade
         for the courses is then calculated, and all information gathered is displayed in tabular form.
"""

import re # regular expressions module; used to find or validate a pattern in a string.

def main():
    f_name = get_first_name()
    l_name = get_last_name()
    
    student = Student(f_name, l_name) # Initializes a Student object with first and last names

    while True:
        name = student.get_course_name()
        credits = student.get_course_credits(name)
        
        gpa = student.get_course_gpa()
        student.add_course(name,credits,gpa)

        ans = input("Would you like to add another course? [Y/N]: ")
        if ans.lower() not in ("y", "yes"):
            break

    cum_gpa = student.get_cum_gpa()

    print(f"\n{f_name} {l_name}'s Grade Summary:\n")
    print(f"{"Course":<30}{"Credits":^10}{"Course GPA":^15}") # tabular form, <30 means left-aligned in a 30-character section.
    print("-" * 60)                                           # >15 means right-aligned in a 15-character section.
    
    for k,v in student.courses_info.items():
        print(f"{k:<30}{v["credits"]:^10}{v["gpa"]:^15}")

    print(f"\nCumulative GPA: {cum_gpa:.2f}")

def get_first_name():
    """Gets first name. Validates first name's pattern using a regular expression."""

    # For this pattern, one or more letters, captial or undercase, followed by a 
    # space one or more times. This then checks for an optional letter 0 or more times.
    # Accepts: "Anne-Marie", Anne Marie, "Anne".
    pattern = r"^[A-Za-z]+[-\s]*[A-Za-z]*$"
    while True:
        f_name = input("Please enter your first name: ")
        if re.fullmatch(pattern, f_name): # checks if first name fits the accepted pattern.
            return f_name.title()
        else:
            print("Sorry, numbers and non-letter characters besides a hyphenated name are not accepted.")
    
def get_last_name():
    """Gets last name. Validates last name's pattern using a regular expression."""

    # For this pattern, one or more letters, captial or undercase, followed by a 
    # space or hyphen 0 or more times. This then checks for an optional letter 0 or more times.
    # Accepts: "Jones", "Van Dyke", "Jones-Smith"
    pattern = r"^[A-Za-z]+[-\s]*[A-Za-z]*$"
    while True:
        l_name = input("Please enter your last name: ")
        if re.fullmatch(pattern, l_name): # checks if last name fits the accepted pattern.
            return l_name.title()
        else:
            print("Sorry, numbers and non-letter characters besides a hyphenated name are not accepted.")   

class Student():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        
        self.CREDIT_MAX = 5 # few courses will be above 5, if any; used for credit validation
        self.courses_info = {} # empty dictionary where values are added to by one of the class's methods

         
        
    def get_course_name(self):
        """Gets course name and validates it against an accepted regular expression."""

        # pattern accepts one or more capital or lowercase letters followed by an optional[0 or more spaces 
        # followed by 1 or more digits] occurring 0 or more times, followed an optional [space 0 or more times
        # followed by an optional ", : or -", this is followed by a space that occurs 0 or more times, 
        # then a letter, lowercase or capital, one or more times.] all this will occur 0 or more times. This is
        # followed by an optional [space one or more times followed by a digit one ore more times].
        # Accepts: "History", "History: American Government", "History - American Government", "History 101", 
        # "HIS 101: American Government", "History-American Government", "American History 101, 
        # and "HIS101: American Government"
        pattern = r"^[A-Za-z]+[\s*\d+]*(?:\s*[,:-]?\s*[A-Za-z]+)*(?:\s+\d+)?$"

        while True:
            name = input("What is the name of the course? ").strip()

            if re.fullmatch(pattern, name): # checks if name entered follows the accepted pattern.
                return name.title()
                        
            else:
                print("Please enter the course name in one of the following formats: " 
                "History, History: American Government, HIS 101, History 101 - Politics, American History 101,"
                "or History - American Government.")
                

    def get_course_credits(self,course_name):
        """Gets course credits from user. Validates value given against the minimum and maximum accepted values
        for course credits.
        """
        credits = 0
        while True:
            try:
                credits = int(input(f"How many credits is {course_name}? ").strip())
                if 1 <= credits <= self.CREDIT_MAX:
                    return credits
            except ValueError: # executes when a non integer is given for credits input
                print(f"Sorry, {credits} credits does not fall between 1 and the maximum {self.CREDIT_MAX} credits")
            
    def get_course_gpa(self):
        """Gets GPA based on letter grade for course. Validates value given based on given dictionary list based
           on letter grade, and converts that to the dictionary's value for GPA.
        """

        display= """
        Letter Grade    Percentage Grade        Letter Grade    Percentage Grade
        A                          >= 92.5      C               < 76.5 and >= 72.5
        A-              < 92.5 and >= 89.5      C-              < 72.5  and >= 69.5
        B+              < 89.5 and >= 86.5      D+              < 69.5 and >= 66.5
        B               < 86.5 and >= 82.5      D               < 66.5 and >= 62.5
        B-              < 82.5 and >= 79.5      D-              < 62.5 and >= 59.5
        C+              < 79.5 and >= 76.5      F               < 59.5                        
        """
        grade_list = {"A": 4.0, "A-": 3.67, "B+": 3.33, "B": 3.0, "B-": 2.67, "C+": 2.33, 
                      "C":2.0, "C-": 1.67,"D+":1.33, "D": 1.0, "D-": 0.67, "F": 0}

        while True:
            print(display)
            grade = input("Please enter your letter grade here: ").strip()
            if grade.title() in grade_list.keys():
                return grade_list[grade.title()]
            print(f"{grade} is not a valid letter grade")
                
    def add_course(self, course_name, credits, gpa):
        """Adds course name with values of credits and class GPA to courses_info dictionary. Validation
           for the values was performed when getting the values of the dictionary in previous methods.
        """

        self.courses_info[course_name] = {"credits": credits, "gpa": gpa}
    
    def get_cum_gpa(self):
        """Calculates cumulative gpa based on dictionary which is part of the Student object used."""

        gpa_total = 0
        credits_total = 0
        for v in self.courses_info.values(): # Uses values of the object's dictionary for calculations
            credits_total += v["credits"] 
            gpa_total += v["gpa"] * v["credits"]
        cum_gpa = gpa_total / credits_total 
        return cum_gpa

  

if __name__ == "__main__":
    main()