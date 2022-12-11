"""This program simulates a dress-up game where a user can put clothes on
themselves."""

from argparse import ArgumentParser
import sys
import pandas as pd
from PIL import Image

class Character:
    """ Creates a customizable character for user to dress up
     
     Attributes:  
            name (str): name of person
            budget (int): the budget of the player. Defaults to 100
            closet (list of str): clothes bought/clothes removed
            wearing (list of str): clothes that the player is currently wearing
    """
    
    def __init__(self, name, budget = 100):
        """Initializes the character class attributes additionally prints the
        clothes from the two different users.

        Args:
            name (str): the name of the player
            budget (int, optional): Assigned player budget. Defaults to 100.
        
        Side effects:
            Defines the values of the attributes.
        """
        #initalizes attributes
        #sets player, budget, etc.
        self.name = name
        self.budget = budget
        self.closet = []
        self.wearing = []
    
    def wear_clothes(self, item):
        """Allows the user to wear clothes by moving clothes from closet to self
        
        Args:
            item (str): the name of the clothing item that we're going to wear.
            
        Returns:
            new self.wearing attribute
            
        Side effects:
            alters the state of self.closet and self.wearing
        """
        if len(self.wearing) > 5:
            print(f"Hey, you're wearing too much! You gotta take something off.")
        elif item in self.closet:
            self.wearing.append(item)
            self.closet.remove(item)
        else:
            print(f"Looks like that's not something you can do.")
    #wear clothes and removes it from closet
    
    def remove_clothes(self, item):
        """Removes an article of clothing

        Args:
            item(str): The article of clothing the user wants to remove

        Side effects:
            Redefines the contents worn by character and added it to self.closet
        """
        if item in self.wearing:
            self.closet.append(item)
            self.wearing.remove(item)
        else:
            print(f"Looks like that's not something you can do.")
    #removes clothes, puts it into closet
    
    def print_closet(self):
        """Displays the contents of the closet
       
        Side effects:
            Prints to stdout.
        """
        print(f"Here's what's in your closet. Take a look!")
        for item in self.closet:
            print(item)
    #stores owned clothes

    def print_wearing(self):
        """Displays the clothes the user is wearing.
        
        Side effects:
            Prints to stdout.
        """
        print(f"Here's what you're wearing right now.")
        for item in self.wearing:
            print(item)
    
    def print_budget(self):
        """Prints the current budget of the player.
        
        Side effects:
            Prints to stdout.
        """
        print(f"You currently have ${self.budget}.")
        #implementing the __add__ function here
        print("Add more funds by using budget + (however much you want to increase)")
        
    def buy_clothes(self, item):
        """buys clothes from catalogue if whithin budget and not currently owned. 
        CREDIT for conditional expression. 
        
        Args: 
        item (str): item from catalogue to be bought.
        
        Side Effects: 
        alters attribute budget. 
        
        Returns: 
        budget (float) after subtraction.
        """
        #list comp - usedto present the dataframe 
        #   that excludes fashion score
        #sorted() - used to sort the result from list comp by cost
        #  (default lowest to highest)
        
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
        #Conditional Expression: if item in closet, proceed, else error message
        #removes clothes from closet, refunds 50%, restates budget -> menue
        
        pass
    
    def __add__(self, increase):
        """Adds more money in budget
        
        Side Effects: 
            Redefines the value of self.budget
            Prints text that acknoledges the change in

        Concepts:
        Magic Expression: Mia
        """
        self.budget = float(self.budget) + increase
        print(f"Your new budget is {self.budget}")
        
    
    def visualize(budget, time):
        """ 
        Plots Budget over time using either seaborn or pyplot
        
        Args:
           budget (float): amount of money the player has left after spending
           time (int): the length of the game running
        
        Returns: 
            plot of budget over time
        """
    def judge(self):
        """Judges the user's score based on the clothing that they've worn.
        """
        fashion_sum = self.wearing[self.wearing["Clothing Name"].isin(self.wearing)]
        ["Fashion Score"].sum()
        
        if fashion_sum <= 5:
            print(f"Loser, do better. \n Fashion Score: {fashion_sum}/25")
        elif fashion_sum >= 6 and fashion_sum <= 10:
            print(f"Getting There. \n Fashion Score: {fashion_sum}/25")
        elif fashion_sum >= 11 and fashion_sum <= 15:
            print(f"So Close... \n Fashion Score: {fashion_sum}/25")  
        elif fashion_sum >= 16 and fashion_sum <= 20:
            print(f"Great Job! \n Fashion Score: {fashion_sum}/25")
        else: 
            print(f"Perfect Score!!! \n Fashion Score: {fashion_sum}/25")
        if self.wearing == ["Blue Button Down", "Classic Jeans", "Blue Tie", "Glasses"]:
            im = Image.open(r"/Users/miamonique/Desktop/candi.png")
            im.show()
       
    
def main(catalogue_filepath):
    """Runs the program, reads in necessary information and offers choices for
    the player.
    
    Args:
        catalogue_filepath (str): the filepath of a .csv file containing
        various information on different clothes.
    
    Side effects:
        Prints to standard output. Simulates an interactive application through 
        the usage of the "while" statement. Allows users to call different
        methods using keywords.
    """
    
    """Techniques used for this section:
    - Optional Parameters
    - Opening a file using with statements
    """
    player_name = input(str("Welcome to the dress up game simulator! Please enter your name: "))
    player = Character(player_name)
    catalogue = pd.read_csv(catalogue_filepath)
    response = ("Please select a choice from the following options, or 'QUIT' to exit program:\n"
                    "Enter 'CATALOGUE' to view the options currently avaliable in our catalogue.\n"
                    "Enter 'CLOSET' to view the items within your personal closet.\n"
                    "Enter 'WEARING' to view the items that you are currently wearing.\n"
                    "Enter 'BUDGET' to view your current budget.\n"
                    "Enter 'JUDGE' in order to walk down the runway and judge your fashion!\n"
                    "Enter 'VISUALIZE' in order to see your budget changes over time.\n"
                    "Enter 'WEARCLOTHES' in order to put something on that you have!\n"
                    "Enter 'TAKEOFF' in order to take clothing off.\n"
                    "Enter 'SELL' in order to sell an article of clothing that you have.\n"
                    "Enter 'BUY' in order to buy new clothing you don't have!\n"
                    "Enter 'ADD' in order to see a category of clothes.\n"
                    "Enter 'SAVE' in order to save your current progress to a file.\n"
                    "Enter 'LOAD' in order to load your progress from a file.")
    while response != "QUIT":
        
        if response == "CATALOGUE":
            catalogue = pd.read_csv(catalogue_filepath)
            print(catalogue.to_string())
            
        elif response == "CLOSET":
            player.print_closet()
            
        elif response == "WEARING":
            player.print_wearing()
            
        elif response == "BUDGET":
            player.print_budget()
            
        elif response == "JUDGE":
            player.judge()
            
        elif response == "VISUALIZE":
            pass
        
        elif response == "BUY":
            item = input(str("Which item are you planning on purchasing? "))
            if (catalogue["Clothing Name"].eq(item)).any():
                if player.budget > catalogue[item,'Cost']
                
        elif response == "LOAD":
            filepath = input(str("Please enter the filepath of the save file: "))
            with open(filepath, "r", encoding = "UTF-8") as f:
                lines = f.read().splitlines()
            player.name = lines[0]
            player.budget = int(lines[1])
            player.closet = lines[2].split(",")
            player.wearing = lines[3].split(",")
            
        elif response == "SAVE":
            filename = input(str("What is the name of the file you'd like the save data to be called? "))
            with open (filename, "w", encoding = "UTF-8") as f:
                f.write(f"{player.name}\n")
                f.write(f"{player.budget}]n")
                f.write(f"{','.join(player.closet)}\n")
                f.write(f"{','.join(player.wearing)}")    
        
        else:
            print(f"Sorry, that's not an option. Why don't you try again?")
        
        response = input(str("Please select a choice from the following options, or 'QUIT' to exit program:\n"
                    "Enter 'CATALOGUE' to view the options currently avaliable in our catalogue.\n"
                    "Enter 'CLOSET' to view the items within your personal closet.\n"
                    "Enter 'WEARING' to view the items that you are currently wearing.\n"
                    "Enter 'BUDGET' to view your current budget.\n"
                    "Enter 'JUDGE' in order to walk down the runway and judge your fashion!\n"
                    "Enter 'VISUALIZE' in order to see your budget changes over time.\n"
                    "Enter 'WEARCLOTHES' in order to put something on that you have!\n"
                    "Enter 'TAKEOFF' in order to take clothing off.\n"
                    "Enter 'SELL' in order to sell an article of clothing that you have.\n"
                    "Enter 'BUY' in order to buy new clothing you don't have!\n"
                    "Enter 'ADD' in order to see a category of clothes.\n"
                    "Enter 'SAVE' in order to save your current progress to a file.\n"
                    "Enter 'LOAD' in order to load your progress from a file."))            
        

def parse_args(arglist):
    """ Parse command-line arguments

    Expect one mandatory argument, the path to the file of clothings

    Args:
        arglist (list of str): command-line arguments; path to clothes csv

    Returns:
        namespace: the parsed argument as a namespace 
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help = "filepath of clothes cataloge csv")

    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath)

    
    
"""Here's the list of the techniques we want to showcase

- conditional expressions - Layla
- optional parameters and/or use of keyword arguments - William
- f-strings - Flavyne
- with statements - William
- the ArgumentParser class - Mia
- Custom list sorting with a key funciton - Flavyne
- comprehensions or generator expressions - Layla
- magic methods other than __init__() - Mia
- concatenating, merging, filtering, or performing groupby operations on Pandas DataFrames - Anna
- visualizing data with pyplot or seaborn - Anna
"""
