"""
Modify this docstring.

"""

# imports first

import random

from util_datafun_logger import setup_logger

# Set up logging .............................................

logger, logname = setup_logger(__file__)

# reusable functions next
#Create about five lists. 

actor_names = ["Milo", "Johnny", "Christoph", "Nick", "Brad"]

actress_names = ["Zoe", "Amy", "Zendaya", "Florence", "Megan"]

movie_genre = ["Action", "Comedy", "Romance", "Horror", "Drama" ]

movie_rating = ["G", "PG", "R", "NR"]

streaming_services = ["Netflix", "Hulu", "HBO", "Amazon"]

# call functions and execute code
#Use the built-in functions: len(), set(), and zip() to combine 2 or more lists into tuples.

def combine_lists_using_len():
    len_list = len(movie_genre)                        
    logger.info("The length is: {len_list}")


def combine_lists_using_set():
    set_list = tuple(set(movie_genre))
    logger.info(f"New sorted set list is: {set_list}")

def combined_tuples_using_zip():
    zip_list= tuple(zip(actor_names, actress_names))
    logger.info(f"Combined list is: {zip_list}")

#Use random.choice() to pick a random value from one of your lists.
def random_choice():
    ran_list = random.choice(movie_rating)
    logger.info(f"Random rating is: {ran_list}")

#Customize the sentence generator to create random sentences about your domain.    
def random_sentence():
    actor_choice = random.choice(actor_names)
    logger.info(f"{actor_choice} has made movies with {actor_choice}")

#Use open(), read(), split(), and set() to read a text file and get a list of unique words. 
def process_text():  
    with open("text_woodchuck.txt", "r") as fileObject:
        text = fileObject.read()
        list_words = text.split()  
        unique_words = set(list_words)  

        # Get the count and list of words
        word_count = len(list_words)

        logger.info(f"The list of words is: {list_words}")
        logger.info(f"There are {word_count} words in the file.")

        # Print the count and list of unique words
        unique_word_ct = len(unique_words)

        logger.info(f"The set of unique words is: {unique_words}")
        logger.info(f"There are {unique_word_ct} unique words in the file.")

def show_log():
    """Read log file and print it to the terminal"""
    with open(logname, "r") as file_wrapper:
        print(file_wrapper.read())


if __name__ == "__main__":
    logger.info("Calling functions from main block")

    combine_lists_using_len()
    combine_lists_using_set()
    combined_tuples_using_zip()
    random_choice()
    random_sentence()
    process_text()

    show_log()

