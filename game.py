#note on submission: I had everything working and was reviewing / trying to create a .gitignore file because I forgot to make one when i set up the repo
# when I uncomment the from dotenv import load_dotenv line, the from is underlined and says that I can't load it. 
# I'm not sure why this is happening... I tried deleting and redownloading my local repo, restarting the requirements.txt and .env files
#tried making a new anaconda environemnt with everything installed and couldnt figure out why this is the case
# put the commented code that would be needed for the username below along with the necessary files, but functionality is working 100%.

import random
import os 

#from dotenv import load_dotenv
# load_dotenv()

#
# creating a username
#

# PLAYER_NAME = os.getenv("USER_NAME", default="Player 1")

print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
# should be ("Welcome 'PLAYER_NAME' to my )
print("-------------------")



#
# asking user for an input
#
user_input = input("Please choose either 'rock', 'paper', or 'scissors': ")
print("You chose: '", user_input, "'")

#
#simulating a computer input
#

options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
print("The computer chose: '" , computer_choice , "'")
print("-------------------")

#
# Validate the user selection
#
if user_input not in options:
        print("OOPS. Please choose a valid option and try again")
        exit()
#
#determining who won
#

if user_input == computer_choice :
    print("It's a tie !")
elif user_input == "rock" and computer_choice == "scissors":
        print("You win !")
elif user_input == "scissors" and computer_choice == "paper":
        print("You win!")
elif user_input == "paper" and computer_choice == "rock":
        print("You win!")
elif computer_choice == "rock" and user_input == "scissors" :
        print("Oh, the computer won. It's ok.")
elif computer_choice == "scissors" and user_input == "paper" :
        print("Oh, the computer won. It's ok.")
elif computer_choice == "paper" and user_input == "rock" :
        print("Oh, the computer won. It's ok.")

print("-------------------")
print("Thanks for playing. Please play again!")


#
#user_name = input("Please create a username\n")
#
#print("Welcome " + USER_NAME)
#
#user_input = input("Please input rock, paper, or scissors\n")
#
#if(user_input != "rock" and user_input != "paper" and user_input != "scissors")
#{
#    print("Sorry, this is not a valid input")
#}
#
#print("You chose: " + user_input)
 