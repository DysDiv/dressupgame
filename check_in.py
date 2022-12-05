"""This program simulates a dress-up game where a user can put clothes on
themselves."""

class Character:
    """ Creates a customizable character for user to dress up
     
     Attributes:  
            name (str): name of person
            clothes (str): clothes
            closet (list of instances): clothes bought/clothes revomed
            catalouge (dict): a dict full of different clothing items
    """
    
    
    def __init__(self, budget, character):
        pass
    #initalizes attributes
    #sets username, budget, etc.
        self.name
        self.budget
        self.eyecolor
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
    
    def remove_clothes(self, item):
        """Removes an article of clothing

        Args:
            item(str): The article of clothing the user wants to remove

        Side effects:
            Redefines the contents worn by character and added it to self.closet
        """
        pass
    #removes clothes, puts it into closet
    
    def closet(self):
        """Stores the purchased and unworn clothes

        Side effects:
            Defines the contents of the closet
        """
        pass
    #stores owned clothes
    
    def catalogue(file):
        """
        Reads in CSV file and finds the max and min of cost and fashion score
        
        Args:
            file (csv): A CSV file in UTF-8 encoding with columns "Clothing Name" (str), "Category" (str), "Cost" (int), and "Fashion Score" (float). 
        The first row of the file contains column headers; each subsequent row describes a single piece of clothes.
        
        Returns: 
            file (csv) after reading it in
        """
        
        """lambda function, add a command to return catalogue from cheap to expensive"""
    #prints catalogue from json file
    
    def buy_clothes(self, item, budget):
        """buys clothes from catalogue if whithin budget and not currently owned. 
        CREDIT for conditional expression. 
        
        Args: 
        item (str): item from catalogue to be bought.
        budget (float): monetary budget
        
        Side Effects: 
        alters attribute budget. 
        
        Returns: 
        budget (float) after subtraction.
        """
        #Conditional Expression: if item not in closet and budget ok, buy.
        pass
    
    def sell_clothes(self, item, budget):
        """sells clothes from closet if currently owned. 
        
        Args: 
        item (str): item from closet to be sold.
        budget (float): monetary budget 
        
        Side Effects: 
        alters attribute budget.
        
        Returns: 
        budget (float) after addition.
        """
        #Conditional Expression: if item in closet, proceed
        #removes clothes from closet, refunds 50%, checks if it's in the closet.
        pass
    
    def __add__():
        """Magic method (we will pick a new name) uses the + symbol in additon 
        to a category of clothes to find all clothes pertaining to that category. 
        CREDIT for list comprehension & generator expressions
        
        Returns: 
        a list of strings: every article of clothes that pertains 
        to a specific category. 
        """
        #list = [EXPR for ITERVAR in ITERABLE if CONDITION]
        pass
    
    def visualize(budget, time):
        """ 
        Plots Budget over time using either seaborn or pyplot
        
        Args:
           budget (float): amount of money the player has left after spending
           time (int): the length of the game running
        
        Returns: 
            plot of budget over time
        """

        
def main(catalogue_filepath, savestate=None):
    """Runs the program, reads in necessary information and offers choices for
    the player.
    
    Args:
        catalogue_filepath (str): the filepath of a .csv file containing
        various information on different clothes.
        savestate (str): the filepath of a .json file that contains information
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
