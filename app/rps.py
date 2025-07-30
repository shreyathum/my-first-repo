# this is my rock paper scissors game 

import random

valid_options = ["rock", "paper", "scissors"]

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
        #result = "COMP WINS" #oops bug , that was a bug 
        result = "USER WINS"
    return result 

#only run the code indented inside if we are running the script from the command line 
#but NOT if we are importing 
if __name__ == "__main__": 

    print("Welcome to my game")

    player_choice = input("Please select an option ('rock', 'paper', 'scissors'): ")
    print("USER CHOSE:", player_choice)


    computer_choice = random.choice(valid_options)
    print("COMPUTER CHOSE:", computer_choice)

    result_message = determine_winner(player_choice, computer_choice)
    print(result_message)