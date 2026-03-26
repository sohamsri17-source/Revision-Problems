# SIMPLE ROCK PAPER SCISSORS GAME

import random
def get_choices():
    player_choice = input("Enter a choice {rock, paper, scissors} : ")
    options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(options) 
    choices = {"player": player_choice, "computer": computer_choice} #Dictionary
    return choices

def check_win(player, computer):
      print(f"You chose : {player}, Computer chose : {computer}")
      if player == computer:
        return"Its a tie."
      elif player == "rock": #Using nested if else 
          if computer == "paper":
              return"Paper captures the rock! You lose!"
          else:
              return"Rock smashes scissors! You win!"
      elif player == "paper":
          if computer == "scissors":
              return"Scissors cuts the paper! You lose!"
          else:
              return"Paper captures the rock! You win!"  
      elif player == "scissors":
          if computer == "rock":
              return"Rock smashes scissors! You lose!"
          else:
              return"Scissors cuts the paper! You win!"
     

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
