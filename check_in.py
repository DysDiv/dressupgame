"""This program simulates a dress-up game where a user can put clothes on
themselves."""
from argparse import ArgumentParser

class Character:
    """Allows user to set custom details for their character."""
    def __init__():
        """ Initializes the Character Class

        Side Effects:
            Defines attributes of the Character class
        """
        self.name
        self.eye_color
        
class Dressup:
    def __init__(self, budget, character):
        """ Initializes the Dressup class

        Args:
            budget (int): Spending token limit
            character: Instance of character class

        Side effects:
            Defines the attributes of Dressup class
        """
        pass
    #initalizes attributes
    #sets username, budget, etc.
        self.budget
        self.character
        self.closet
        self.wearing
        """compare closets between different characters, prints clothes in
        common using set operations"""
    
    def wear_clothes(self, item):
        """Allows the user to wear clothes by moving clothes from closet to self
        
        Args:
            item (str): the name of the clothing item that we're going to wear.
            
        Returns:
            new self.wearing attribute
            
        Side-effects:
            alters the state of self.closet and self.wearing
        """
        pass
    #wear clothes and removes it from closet
    
    def remove_clothes():
        pass
    #removes clothes, puts it into closet
    
    def closet():
        pass
    #stores owned clothes
    
    def catalogue(file):
        """
        file (csv): A CSV file in UTF-8 encoding with columns "Clothes" (str), "Cost" (int), and "Cool Factor" (float). 
        The first row of the file contains column headers; each subsequent row describes a single piece of clothes.
        """
        
        """lambda function, add a command to return catalogue from cheap to expensive"""
    #prints catalogue from json file
    
    def buy_clothes():
        """Layla's docs
        """
        """Conditional Expression: if item not in closet and budget ok, buy"""
        pass
    #adds clothes to closet, subtracts from budget, checks if you already have
    
    def sell_clothes():
        """Layla'a docstrings 
        """
        """Conditional Expression: if item in closet, proceed"""
        pass
    #removes clothes from closet, refunds 50%, checks if it's in the closet
    
    def __add__():
        """layla's docstrings
        """
        """magic method, returns a list of clothes of that type when prompted"""
        """pick another name"""
        """use list comprehension to get the items"""
        """list = [EXPR for ITERVAR in ITERABLE if CONDITION]"""
        pass
    
    def visualize():
        """use data vis tools to print out what the character has on"""

        
def main(catalogue_filepath, savestate=None):
    """Runs the program, reads in necessary information and offers choices for
    the player.
    
    Args:
        catalogue_filepath (str): the filepath of a .csv file containing
        various information on different clothes.
        savestate (str): the filepath of a .txt file that contains information
        on a player's previous settings. If given, loads in information based on
        those settings. Defaults to None.
    
    Side effects:
        Prints to standard output. Simulates an interactive application through 
        the usage of the "while" statement. Allows users to call different
        methods using keywords.
    """
    
    """Techniques used for this section:
    - Optional Parameters
    - Opening a file using with statements
    """
    
    pass

def parse_args(arglist):
    """ Parse command-line arguments

    Expect one mandatory argument, the path to the file of clothings

    Args:
        arglist (list of str): command-line arguments

    Returns:
        namespace: the parsed argument as a namespace 
    """
    pass

if __name__ == "__main__":
    pass
    """f-strings"""
    
    
"""Here's the list of the techniques we want to showcase

- conditional expressions - Layla
- optional parameters and/or use of keyword arguments - William
- f-strings - Flavyne
- with statements - William
- the ArgumentParser class - Mia
- set operations on sets or frozensets - Mia
- comprehensions or generator expressions - Layla
- magic methods other than __init__() - Flavyne
- concatenating, merging, filtering, or performing groupby operations on Pandas DataFrames - Anna
- visualizing data with pyplot or seaborn - Anna
"""
