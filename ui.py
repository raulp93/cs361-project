import sys
import time
from game import *


# citation for slowPrint function
# Author: https://stackoverflow.com/users/14531062/matiiss
# Date Accessed: 5/8/24
# Source: https://stackoverflow.com/questions/66913084/print-slowly-in-terminal-python

def slowPrint(string, speed=0.02):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)



def get_input():
    """prompts the user to enter something"""

    prompt1 = "Please enter one of the following: 'new', 'history': "

    slowPrint(prompt1)
    user_input = input()

    return user_input


def start_new_game(username):
    """handles the starting new game logic"""

    new_game = game(username)
    slowPrint("Alright " + username + ", How many rounds would you like to play? ")
    rounds = int(input())
    # must add data validation
    new_game.set_rounds(rounds)

    while new_game.game_status is True:

        choice = input(" Enter rock/paper/scissors: ")

        if choice == 'rock':
            cp_choice = new_game.rock()

        elif choice == 'paper':
            cp_choice = new_game.paper()
        
        else:
             cp_choice = new_game.scissors()

        slowPrint('\nYou chose: ' + new_game.player_choice)
        slowPrint('\nOpponent Chose: ' + cp_choice)

        if new_game.round_status == "won":
            slowPrint("\n" + new_game.player_name + ' ' + "won")
            slowPrint("\n** queue hip-hop horns **\n")

        elif new_game.round_status == "lost":
            slowPrint("\nOpponent" + " " + "won" )
            slowPrint("\nBetter luck next time...\n")
        
        else:
            slowPrint("\n It was a Draw!\n")
    
    
    slowPrint("\n And the winner is: " + new_game.winner + "!!\n")
    slowPrint("The Score: \n" + new_game.player_name + ": " + str(new_game.rounds_won))
    slowPrint("\n" + "Opponent: " + str(new_game.num_of_rounds - new_game.rounds_won - new_game.rounds_draw))
    slowPrint("\nTotal Draws: " + str(new_game.rounds_draw))

    slowPrint("\nWould you like to play again? Enter yes or no: ")
    again = input()

    if again == 'yes':
        return 'yes'
    
    return 'no'

    
    


def UI_func():

    Greeting = "\n\nGreetings and welcome to my game of rock-paper-scissors. "\
                "My name is Raul Preciado and I will guide you through this user interface.\n "\
                "First things first... "
    
    slowPrint(Greeting)

    slowPrint("What is your name?")
    user_name = input(": ")

    greeting1 = "Ahh, very nice to meet you "
    greeting2 = ". I am glad you're here. \n"

    instructions = "Pay close attention to this next part as it will give you the rundown \n"\
                   "on all the different controls for this program."
    
    command1 = "To start a new game type in 'new'. It will then prompt you to enter how many rounds you'd like to play.\n"
    command2 = "Once the game starts, you will need to type in your choice of rock, paper, or scissors. Make sure you \ntype it in all lower caps"
    command3 = " After each round, the winner of the round will be displayed and then saved.\nYou can type in 'history' to view the results of the previous rounds.\n"
    command4 = ""

    rules = [command1, command2, command3, command4]
 

    slowPrint(greeting1 + user_name + greeting2)
    slowPrint(instructions)
    print('\n')
    slowPrint('---------------------------------------------------------------------------------------------------------\n', 0.005)
    slowPrint('------------------------------------------RULES----------------------------------------------------------\n', 0.005)
    slowPrint('---------------------------------------------------------------------------------------------------------\n', 0.005)

    for i in rules:
        slowPrint(i)

   

    user_input = get_input()

    while user_input == "new" or user_input == 'yes':

        user_input = start_new_game(user_name)

        

    
        




test = UI_func()



