import random

#This is aPython Intermediate project.
"""
This projects covers topics like:
control flow = if elif, else
Lists
dictionaries
Functions & return values
Libraries = random
"""

def get_choices():
    player_choice = input("\nEnter a choice (rock, paper, scissors): ").lower()
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options)
    choices = {"player":player_choice, "computer":computer_choice}
   
    return choices

def check_win(player,computer):
    print(f"\nYou chose {player}, computer chose {computer}.")
    
    if player == computer:
        return "It's a tie"
    
    elif player == 'rock':  
        if computer == 'scissors':
            return "\nRock smashes scissors! You win!"   
        else:
            return "\nPaper covers rock! You lose."   
    elif player == 'paper':  
        if computer == 'rock':
            return "\nPaper covers rock! You win."   
        else:
            return "\nScissors cuts paper! You lose."   
    elif player == 'scissors':  
        if computer == 'paper':
            return "\nScissors cuts paper! You win!"   
        else:
            return "\nRock smashes Scissors! You lose."   
    
    

choices = get_choices()
results = check_win(choices["player"],choices["computer"])
print(results)