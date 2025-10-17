# Course: CIS245-T303 Introduction to Programming
# Instructor: Dr. Azizian
# Author: Joe Nowakowski
# Date Created: 10/13/2025
# Date Last Modified: 10/16/2025

# Purpose: The purpose of this program is to get a list of 20 numbers from user,
# and display the list, minimum number, highest number, the sum total, and the average
# of the 20 numbers provided. 
 
TOTAL_NUMS = 20

def main():
    """
    Main function

    Gets the list of numbers from the user, then displays the list, calculates
    and displays mininum number, maximum number, sum total, and average of the list
    of numbers provided.
    """
    nums_list = get_lst_nums(TOTAL_NUMS)
    min_num = min(nums_list)
    max_num = max(nums_list)
    total = sum(nums_list)
    average = get_avg_from_list(nums_list)

    # Prints results in tabular form 
    print("Summary of Results".center(45, "-"))
    print(f"The list of numbers entered: {nums_list}")
    print(f"{'The lowest number:':30} {min_num:>10,}")
    print(f"{'The highest number:':30} {max_num:>10,}")
    print(f"{'The summation of the list:':30} {total:>10,}")
    print(f"{'The average:':30} {average:>10,.3f}")
    print("-" * 45)


def get_lst_nums(lst_len_nums):
    """
    Gets list of numbers


    Creates a list of user-entered numbers, length specified by parameter.
    """
    nums_list = []
    num_iters = 0

    print(f"Please enter {lst_len_nums} numbers and I'll compute some basic stats " 
          "from the list.")
    for num in range(lst_len_nums):
        try:
            num = int(input(f"Please enter {num_iters + 1} of {lst_len_nums} numbers: "))
            nums_list.append(num)
            num_iters += 1
        except ValueError: # raised if a number is a float, or if a non-numeric 
                           # character(s) is entered
            print("Invalid input. Please enter whole numbers.")
        
    return nums_list

def get_avg_from_list(nums_list):
    """
    Gets average from list of numbers.

    Used to determine average by sum of list divided by
    the length of the list
    """

    sum_nums = sum(nums_list) # calculated in main, left in for modularization re-usage
    avg = sum_nums/len(nums_list)
    return avg

if __name__ == "__main__":
    main()