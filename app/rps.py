# this is my rock paper scissors game 

print("Welcome to my game")

player_choice = input("Please select an option ('rock', 'paper', 'scissors'): ")
print("USER CHOSE:", player_choice)

#todo: validate choice 

import random

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOSE:", computer_choice)

if player_choice == computer_choice:
    result = "TIE GAME"
elif player_choice == "rock" and computer_choice == "scissors": 
    result = "USER WINS"
elif player_choice == "rock" and computer_choice == "paper": 
    result = "COMP WINS"
elif player_choice == "scissors" and computer_choice == "rock": 
    result = "COMP WINS"
elif player_choice == "scissors" and computer_choice == "paper": 
    result = "USER WINS"
elif player_choice == "paper" and computer_choice == "scissors": 
    result = "COMP WINS"
elif player_choice == "paper" and computer_choice == "rock": 
    result = "COMP WINS"


print(result)