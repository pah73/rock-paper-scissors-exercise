import random


#
# creating a username
#


print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
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
 