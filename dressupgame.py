"""This program simulates a dress-up game where a user can put clothes on
themselves. It contains a multidude of various features that makes the gameplay
feel realistic, such as budget tracking, selecting clothes from catalogues,
logic checks, savestates, and much more."""

from argparse import ArgumentParser
import sys
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

class Character:
    """A representation of the player character that tracks information on name,
    current budget, what's in their closet, and what they are wearing.
     
     Attributes:  
        name (str): name of person
        budget (float): the budget of the player. Defaults to 100
        closet (list of str): clothes purchased and not currently worn
        wearing (list of str): clothes that the player is currently wearing
    """
    
    def __init__(self, name, budget = 100):
        """Initializes the Character class object.
        
        Args:
            name (str): the name of the player
            budget (int, optional): Assigned player budget. Defaults to 100.
        
        Side effects:
            Defines the values of the attributes `name`, `budget`, `closet`, and
            `wearing`.
            
        Techniques: 
            Optional Parameter (William)
        """
        self.name = name
        self.budget = budget
        self.closet = []
        self.wearing = []
        self.bot = [] #budget over time
    
    def wear_clothes(self):
        """Allows the user to wear clothes by moving clothes from `self.closet`
        to `self.wearing`, if the number of clothes doesn't exceed its max.
        
        Args:
            item (str): the name of the clothing item that we're going to wear.
            
        Side effects:
            Alters the state of `self.closet` and `self.wearing`.
            Prints to stdout.
        
        Techniques: 
            Conditional Expressions (Layla)
        """
        item = input("What item would you like to put on?\n Enter (Case Sensitve): ")


        
        if len(self.wearing) > 5:
            print(f"Hey, you're wearing too much! You gotta take something off.")
        elif item in self.closet:
            self.wearing.append(item)
            self.closet.remove(item)
        else:
            print(f"Looks like that's not something you can do.")
    
    def remove_clothes(self, item):
        """Removes an article of clothing currently worn.

        Args:
            item(str): The article of clothing the user wants to remove

        Side effects:
            Alters the state of `self.closet` and `self.wearing`.
            Prints to stdout.
        
        Techniques: 
            f-strings (appears everywhere) (Flavyne)
        """
        if item in self.wearing:
            self.closet.append(item)
            self.wearing.remove(item)
        else:
            print(f"Looks like that's not something you can do.")
    
    def print_closet(self):
        """Displays the contents of the closet.
       
        Side effects:
            Prints to stdout.
        """
        print(f"Here's what's in your closet. Take a look!")
        for item in self.closet:
            print(item)

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
        print(f"Add more funds by using budget + (however much you want to "
              f"increase by).")
        
    def buy_clothes(self):
        """Allows the user to buy clothes from catalogue if whithin budget and
        not currently owned.
        
        Args: 
            item (str): item from catalogue to be bought.
        
        Side Effects: 
            Alters attribute `self.budget`. 

        Techniques:
            List Comprehension (Layla)
            Sequence Unpacking (Mia)
            Conditional Expressions (Layla)
        """
        catalogue = pd.read_csv("clothes.csv")
        
        display = catalogue.sort_values(by = "Cost")
        display = ([(f"{Index}: {Name} ({Category}) ${Cost}") 
                    for Index, Name, Category, Cost
                    in zip(catalogue.index, catalogue["Clothing Name"],
                                catalogue["Category"], catalogue["Cost"])])

        for line in display: 
            print (line + "\n")
        
        itemindex = int(input("Which item are you interested in purchasing? \n Type Num: "))

        itemcost = int(catalogue["Cost"].loc[catalogue.index[itemindex]])
        itemname = catalogue["Clothing Name"].iloc[int(itemindex)]
        if self.budget >= itemcost:
            self.budget -= itemcost
            self.bot.append(self.budget)
            self.closet.append((itemname)) #change if only want to put clothe title
            print(f"You purchased {itemname}!\n ")
            print("Your new purchase is available in your closet")
        else: 
            print("Sorry your card got declined lol, returning to main menu")
        
        #Take the index and add to closet, subtract cost from self.budget,
        #return to main menu
      
    def sell_clothes(self):
        """Allows the user to sell clothes from closet if currently owned and
        not wearing. 
        
        Args: 
            item (str): item from closet to be sold.
        
        Side effects: 
            alters attribute budget.

        Techniques:
            F-string (Flavyne)
            Sorted with lambda (Flavyne)
        """
        self.closet = sorted(self.closet, key = lambda x:x)

        catalogue = pd.read_csv("clothes.csv")
        counter = 0
        for clothe in self.closet:
            clothename = clothe
            clotheindex = catalogue.index[catalogue['Clothing Name'] == clothe].tolist()[0]
            clothecost = (catalogue["Cost"].loc[catalogue.index[clotheindex]]) * 0.5
            counter += 1
            print(f"{counter}: {clothename} ${clothecost}")
        
        itemindex = (int(input("What item would you like to sell? \n Enter Number:"))) -1
        if itemindex < 0 :
            print("Invalid Number")
        elif itemindex > (len(self.closet)-1) :
            print("Invalid Number")
        else:
            pass

        itemcost = (catalogue["Cost"].loc[catalogue.index[itemindex]]) * 0.5

        print(f"You sold your {self.closet[itemindex]}")
        self.budget += itemcost
        self.bot.append(self.budget)
        del self.closet [itemindex]

        print(f"Your current budget is now {self.budget}")
        print("Your closet has been updated: ")
        for item in self.closet:
            print(item)
    
        
    def visualize(self):
        """ 
        Plots Budget over time using either seaborn or pyplot
        
        Side Effects: 
            plot of budget over time
        
        Techniques:
            pyplot (Anna)
        """

        clothes = pd.read_csv("clothes.csv") 
        plt.plot(self.bot, color ='pink')
        plt.xlabel("Time")
        plt.ylabel("Budget")
        plt.title("Budget Over Time")
        plt.show()
            
        
        
    def judge(self):
        """Judges the user's score based on the clothing that they've worn and what items have the max fashion score
        
        Side effects:
            Prints to stdout.

        Techniques:
        f-string (Flavyne)
        pandas boolean filtering (Anna)
        """
        catalogue = pd.read_csv("clothes.csv")

        fashion_sum = catalogue[catalogue["Clothing Name"].isin(self.wearing)]["Fashion Score"].sum()
        fashion_max = catalogue[catalogue["Clothing Name"].isin(self.wearing)]["Fashion Score"].max()
        catalogue["Wearing"] = pd.Series(self.wearing)
        c = catalogue.iloc[len(self.wearing)::, :].fillna
        b = catalogue[catalogue["Fashion Score"] == fashion_max][["Wearing"]]
        
        if (("Blue Button Down" in self.wearing) and 
        ("Classic Jeans" in self.wearing) and
        ("Blue Tie" in self.wearing) and
        ("Glasses" in self.wearing)):
            im = Image.open(r"/Users/miamonique/Desktop/candi.png")
            im.show()

        elif fashion_sum <= 5:
            print(f"Loser, do better. \n Fashion Score: {fashion_sum}/25 \n \n Clothes with Max Fashion Score: \n{b}")
        elif fashion_sum >= 6 and fashion_sum <= 10:
            print(f"Getting There. \n Fashion Score: {fashion_sum}/25 \n \n Clothes with Max Fashion Score: \n {b}")
        elif fashion_sum >= 11 and fashion_sum <= 15:
            print(f"So Close... \n Fashion Score: {fashion_sum}/25 \n \n Clothes with Max Fashion Score: \n{b}")  
        elif fashion_sum >= 16 and fashion_sum <= 20:
            print(f"Great Job! \n Fashion Score: {fashion_sum}/25 \n \n Clothes with Max Fashion Score: \n{b}")
        else: 
            print(f"Perfect Score!!! \n Fashion Score: {fashion_sum}/25 \n \n Clothes with Max Fashion Score: \n{b}")
    
       
def main(catalogue_filepath):
    """Runs the program, reads in necessary information and offers choices for
    the player using a while loop with key 'QUIT'.
    
    Args:
        catalogue_filepath (str): the filepath of a .csv file containing
        various information on different clothes.
    
    Side effects:
        Prints to standard output. Simulates an interactive application through 
        the usage of the "while" statement. Allows users to call different
        methods using keywords.

    Techniques:
        With Statements (William)
    """
    player_name = input(str("Welcome to the dress up game simulator! Please enter your name: "))
    budget = float(input("Please choose your budget?: "))
    if budget != None:
        player = Character(player_name, budget)
    else:
        player = Character(player_name)
    catalogue = pd.read_csv(catalogue_filepath)
    
    response = input("\n \n \n-----------------------------------------\n"
        "Please select a choice from the following options, or 'QUIT' to exit program:\n"
                    "'CATALOGUE' to view the options currently avaliable in our catalogue.\n"
                    "'CLOSET' to view the items within your personal closet.\n"
                    "'WEARING' to view the items that you are currently wearing.\n"
                    "'BUDGET' to view your current budget.\n"
                    "'JUDGE' in order to walk down the runway and judge your fashion!\n"
                    "'VISUALIZE' in order to see your budget changes over time.\n"
                    "'WEARCLOTHES' in order to put something on that you have!\n"
                    "'TAKEOFF' in order to take clothing off.\n"
                    "'SELL' in order to sell an article of clothing that you have.\n"
                    "'BUY' in order to buy new clothing you don't have!\n"
                    "'ADD' in order to see a category of clothes.\n"
                    "'SAVE' in order to save your current progress to a file.\n"
                    "'LOAD' in order to load your progress from a file.\n"
                    "\n \n-----------------------------------------\n"
                    "Enter KEYWORD: ")
    
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
            player.visualize()
            
        elif response ==  "WEARCLOTHES":
            player.print_closet()
            player.wear_clothes()
            
        elif response ==  "SELL":
            player.sell_clothes()
        
        elif response == "BUY":
            player.buy_clothes()
                
        elif response == "LOAD":
            filepath = input(str("Please enter the filepath of the save file: "))
            with open(filepath, "r", encoding = "UTF-8") as f:
                lines = f.read().splitlines()
            player.name = lines[0]
            player.budget = float(lines[1])
            player.closet = lines[2].split(",")
            player.wearing = lines[3].split(",")
            
        elif response == "SAVE":
            filename = input(str("What is the name of the file you'd like the save data to be called? "))
            with open (filename, "w", encoding = "UTF-8") as f:
                f.write(f"{player.name}\n")
                f.write(f"{player.budget}\n")
                f.write(f"{','.join(player.closet)}\n")
                f.write(f"{','.join(player.wearing)}")    
        
        else:
            print(f"Sorry, that's not an option. Why don't you try again?")
        
        response = input(str("\n \n \n-----------------------------------------\n"
        "Please select a choice from the following options, or 'QUIT' to exit program:\n"
                    "'CATALOGUE' to view the options currently avaliable in our catalogue.\n"
                    "'CLOSET' to view the items within your personal closet.\n"
                    "'WEARING' to view the items that you are currently wearing.\n"
                    "'BUDGET' to view your current budget.\n"
                    "'JUDGE' in order to walk down the runway and judge your fashion!\n"
                    "'VISUALIZE' in order to see your budget changes over time.\n"
                    "'WEARCLOTHES' in order to put something on that you have!\n"
                    "'TAKEOFF' in order to take clothing off.\n"
                    "'SELL' in order to sell an article of clothing that you have.\n"
                    "'BUY' in order to buy new clothing you don't have!\n"
                    "'ADD' in order to see a category of clothes.\n"
                    "'SAVE' in order to save your current progress to a file.\n"
                    "'LOAD' in order to load your progress from a file.\n"
                    "Enter KEYWORD in quotations: "
                    "\n \n-----------------------------------------\n"))            
        
def parse_args(arglist):
    """Parse command-line arguments
    Expecting one mandatory argument, the path to the catalogue file

    Args:
        arglist (list of str): command-line arguments; path to clothes csv

    Returns:
        namespace: the parsed argument as a namespace 
    
    Techniques:
        Parse args (Mia)
    """
    parser = ArgumentParser()
    parser.add_argument("filepath", help = "filepath of clothes cataloge csv")

    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.filepath)

"""
List of the techniques showcased

- conditional expressions - Layla
- optional parameters and/or use of keyword arguments - William
- f-strings - Flavyne
- with statements - William
- the ArgumentParser class - Mia
- Sequence unpacking - Mia
- Custom list sorting with a key funciton - Flavyne
- comprehensions or generator expressions - Layla
- concatenating, merging, filtering, or performing groupby operations on Pandas DataFrames - Anna
- visualizing data with pyplot or seaborn - Anna
"""
