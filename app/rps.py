# this is my rock paper scissors game 

print("Welcome to my game")

player_choice = input("Please select an option ('rock', 'paper', 'scissors'): ")
print("USER CHOSE:", player_choice)

#todo: validate choice 

import random

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOSE:", computer_choice)

def determine_winner(u, c): 
    if u == c:
        result = "TIE GAME"
    elif u == "rock" and c == "scissors": 
        result = "USER WINS"
    elif u == "rock" and c == "paper": 
        result = "COMP WINS"
    elif u == "scissors" and c == "rock": 
        result = "COMP WINS"
    elif u == "scissors" and c == "paper": 
        result = "USER WINS"
    elif u == "paper" and c == "scissors": 
        result = "COMP WINS"
    elif u == "paper" and c == "rock": 
        result = "COMP WINS"
    return result 

result_message = determine_winner(player_choice, computer_choice)
print(result_message)