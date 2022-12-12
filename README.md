# dressupgame
```
Our project revolves around a dress-up game where the primary feature of the program is taking a custom character and “dressing them up” with accessories.

In this program, we store all of the information in regards to the character in attributes, such as the name of the character, the total budget, and lists that emulate pseudo-closets and contents that you are wearing.

The user would be able to add or modify components as they see fit, with budget constraints.

Here are some highlight features of the program:
    1. The ability to purchase and sell items based off of a pre-existing catalogue, provided by the user
    2. Real-time tracking of your budget by taking information from each item and updating them as you sell and buy
    3. Emergency funds using "+" magic method
    4. The ability to load and save the state of the game
    5. Ability to judge the user's fashion score
    6. Ability to visualize budget change over time

How to run the program:
    Parse args allows the user to run the program from the command line. Simply input the following format on the command line:
    python3 dressupgame.py `catalogue_name.csv`

    The main function should initialize the player object and run the while loop to simulate UI.
```
