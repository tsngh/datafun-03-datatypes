"""
Modify this docstring.

"""

# import from local util_datafun_logger.py
from util_datafun_logger import setup_logger

# Call the setup_logger function to create a logger and get the log file name
logger, logname = setup_logger(__file__)


# Create some tuples

def illustrate_tuples():
    """This function illustrates tuples in Python."""

    tuple_rating = ("R", "PG", "M", "NR")
    tuple_genre = ("Comedy", "Horror","Action", "Romance")

    logger.info(f"tupleA = {tuple_rating}")
    logger.info(f"tupleB = {tuple_genre}")

# tuple concatenation
    tupleCat = tuple_rating + tuple_genre

# tuple repetition
    tuple1double = tuple_rating * 2

# TODO: Start using this f-string "syntactic sugar" for quick ouptut
# just add space = space inside the curly braces
# it will print the name of the variable and the value
    logger.info(f"{tuple_rating = }")
    logger.info(f"{tuple_genre = }")
    logger.info(f"{tupleCat = }")
    logger.info(f"{tuple1double = }")


#Sets: create two sets. Get the intersection and the union.

def illustrate_sets():
    """This function illustrates sets in Python."""

    rating_A = {1, 2, 3, 4, 5}
    rating_B = {5, 6, 7, 8, 9}

    logger.info(f"setA = {rating_A}")
    logger.info(f"setB = {rating_B}")

    # set union
    set_union = rating_A | rating_B
    logger.info(f'union of sets: {set_union}')

    # set intersection
    set_intersection = rating_A & rating_B
    logger.info(f'intersection of sets: {set_intersection}')


#Use a dictionary to create key-value pairs of each word and its count from a file.

def illustrate_dictionaries():
    """This function illustrates dictionaries in Python."""
    Person_A = {"name": "Zendaya", "age": 27, "movies": 26}
    Person_B = {"name": "Milo", "age": 46, "movies": 24}

    logger.info(f"Person_A = {Person_A}")
    logger.info(f"Person_B = {Person_B}")

with open("text_simple.txt") as file_object:
    word_list = file_object.read().split()

    word_counts_dict = {}
for word in word_list:
    if word in word_counts_dict:
        word_counts_dict[word] += 1
    else:
        word_counts_dict[word] = 1

    logger.info("Word count is a good way to begin processing text.")
    logger.info(f"Given text_simple.txt, the word_counts_dict = {word_counts_dict}")

    # IMPORTANT: Dictionary comprehesions - the preferred approach

    # Create a dictionary of word counts from a list of words
    # A dictionary is always key:value pairs
    # Say "I want word:count for each word in word_list"
    # Cast the result to a dictionary by using curly braces {}
    word_counts_dict2 = {word: word_list.count(word) for word in word_list}

    # Spend most of your practice on comprehensions - they are
    # key to transforming data in Python.

    logger.info("Given text_zen_of_python.txt and comprehensions,")
    logger.info(f"the the word_counts_dict2 = {word_counts_dict2}")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())

# Call some functions and execute code!
# Remember, code blocks must be indented consistently after a colon.

if __name__ == "__main__":
    logger.info("Calling functions from main block")

    # call your functions here
    illustrate_tuples()
    illustrate_sets()
    illustrate_dictionaries()

    logger.info("Add more logging statements to the code to see what happens.")
    logger.info("Explore enough to understand.")
    logger.info("Apply these skills to your own topic domain.")
   
    show_log()
