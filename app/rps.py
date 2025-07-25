# this is my rock paper scissors game 

print("Welcome to my game")

player_choice = input("Please select an option ('rock', 'paper', 'scissors'): ")
print("USER CHOSE:", player_choice)

#todo: validate choice 

import random

valid_options = ["rock", "paper", "scissors"]
computer_choice = random.choice(valid_options)
print("COMPUTER CHOSE:", computer_choice)

print("WINNER TODO")