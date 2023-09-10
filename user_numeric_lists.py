"""
Modify this docstring.

"""

# import some standard modules first - how many can you make use of?
import math
import statistics



# TODO: import from local util_datafun_logger.py 

from util_datafun_logger import setup_logger


# TODO: Call the setup_logger function to create a logger and get the log file name

logger, logname = setup_logger(__file__)


# TODO: Create some shared data lists if you like - or just create them in your functions

list1 = [1,2, 23, 11, 14, 76, 61, 10, 32, 56, 77, 77, 87, 167, 221, 245, 307, 11, 61, 90 ]

listx = list(range(10))
listy = [1, 3, 5, 7, 8, 9, 11, 11, 15, 16]


# TODO: define some custom functions

def illustrate_list_statistics():

    logger.info(f"score_list: {list1}")

    mean = statistics.mean(list1)
    median = statistics.median(list1)
    mode = statistics.mode(list1)

    logger.info(f"mean: {mean}")
    logger.info(f"median: {median}")
    logger.info(f"mode: {mode}")

    stdev = statistics.stdev(list1)
    variance = statistics.variance(list1)

    logger.info(f"stdev: {stdev:.2f}")
    logger.info(f"variance: {variance:.2f}")

def illustrate_list_correlation_and_prediction():

    logger.info(f"listx: {listx}")
    logger.info(f"listy: {listy}")

    correlationxy = statistics.correlation(listx, listy)
    logger.info(f"correlation between x and y: {correlationxy:.2f}")

    slope, intercept = statistics.linear_regression(listx, listy)
    logger.info(f"The equation of the best fit line is: y = {slope:.2f}x + {intercept:.2f}")

    x_max = max(listx)
    new_x = 15  

    new_y = slope * new_x + intercept

    logger.info("We predict that when x = {newx}, y will be about {new_y}")

def illustrate_list_built_in_functions():
# Calcuate the max and min scores
    max_value = max(list1)
    min_value = min(list1)

    logger.info(f"Given score list: {list1}")
    logger.info(f"The max() is {max_value}")
    logger.info(f"The min() is {min_value}")

    # Calculate the length of the list
    len_list = len(list1)
    logger.info(f"The len() is {len_list}")

    # Calculate the sum of the list
    sum_list = sum(list1)
    logger.info(f"The sum() is {sum_list}")

    # Calculate the average of the list
    avg_list = sum_list / len_list
    logger.info(f"The average is {avg_list}")

    logger.info(f"Given score list: {list1}")
    # Return a new list soreted in ascending order
    asc_scores = sorted(list1)
    logger.info(f"Using the built-it function sorted(lst) gives: {asc_scores}")

    # Return a new list soreted in descending order
    desc_scores = sorted(list1, reverse=True)
    logger.info(
        f"Using the built-in function sorted(lst,reverse=True) gives: {desc_scores}"
    )

#Make a new short list called lst

def illustrate_list_methods():

#append() a single value to the list

    lst = [2, 3, 5, 7, 9]
    lst.append(6)

# extend the list with another list

    lst.extend([1, 4, 10])

# insert() at an index, insert a value
    i = 0
    newvalue = 27
    lst.insert(i, newvalue)

 # remove(5) remove the number 5 from the list, if found (change 5 to a value in your list)
    item_to_remove = 5
    lst.remove(item_to_remove)

 # Count(2) count how many times 2 appears in your list (if it doesn't, change  2 to a value in your list)
    ct_of_2 = lst.count(2)

 # Sort the list in ascending order using the sort() method
    asc_lst2 = lst.sort()

# Sort the list in descending order using the sort() method
    desc_lst2 = lst.sort(reverse=True)

# Copy the list to a new list
    new_lst = lst.copy()
    logger.info(f"new_numbers are: {new_lst}")

# Remove the first item from the new list
    first = new_lst.pop(0)
    logger.info(
    f"Popped the first (index=0): {first} and now, new_numbers are: {new_lst}")

# Remove the last item from the new list
    last = new_lst.pop(-1)
    logger.info(
    f"Popped the last (index=-1): {last} and now, new_numbers are: {new_lst}")

def illustrate_list_transformations():

    logger.info(f"Number list: {list1}")

# TRANFORMATIONS: Use the built in filter() function to keep x such that x is  less than 4 (or some other cutoff), or keep the even ones, whatever.
    numbers_under_50 = list(filter(lambda x: x < 50, list1))
    logger.info(f"Numbers under 50: {numbers_under_50}")

# Use the built in map() function to map each x to cuberoot of x (hint: use math module)
    cubed_numbers = list(map(lambda x: x ** (1/3), list1))
    logger.info(f"Cubed numbers: {cubed_numbers}")

# Use the built in map() function to calculate the volume of a cube
    volume = list(map(lambda x: x ** 3, list1))
    logger.info(f"Volume of list1: {volume}")

def illustrate_list_comprehensions():
    logger.info(f"List1: {list1}")

#Use a list comprehension to filter (start within square brackets) to get x

    numbers_over_50 = [x for x in list1 if x > 50]
    logger.info(f"Numbers over 50 (using list comprehensions!): {numbers_over_50}")

 
# Use a list comprehension to triple each value in your list1, that is to get x*3 (for x in list1)

    tripled_numbers = [x*3 for x in list1]
    logger.info(f"Tripled numbers are: {tripled_numbers}")


# Use a list comprehension to transform your numeric list into another numeric list
    sqrt_numbers = [math.sqrt(x) for x in list1]

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())




# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
   if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here (see instructions)
    illustrate_list_statistics()
    illustrate_list_correlation_and_prediction()
    illustrate_list_built_in_functions()
    illustrate_list_methods()
    illustrate_list_transformations()
    illustrate_list_comprehensions()

    logger.info("Add more logging statements to the code to see what happens.")
    logger.info("Explore enough to understand.")
    logger.info("Apply these skills to your own topic domain.")

    show_log()



