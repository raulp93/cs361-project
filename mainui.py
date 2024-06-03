import sys, time, threading

from game import *
from jsontotablefunc import tablepipeline



# citation for slowPrint function
# Author: https://stackoverflow.com/users/14531062/matiiss
# Date Accessed: 5/8/24
# Source: https://stackoverflow.com/questions/66913084/print-slowly-in-terminal-python

def slowPrint(string, speed=0.01):
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)





Greeting = "\n\nGreetings and welcome to my game of rock-paper-scissors. "\
            "My name is Raul Preciado and I will guide you through this user interface.\n "\
            "First things first... "

slowPrint(Greeting)

slowPrint("What is your name?")
user_name = input(": ")

greeting1 = "Ahh, very nice to meet you "
greeting2 = ". I am glad you're here. \n"

instructions = "Pay close attention to this next part as it will give you the rundown \n"\
               "on all the different controls for this program.\n \n "

slowPrint(greeting1 + user_name + greeting2)

slowPrint(instructions)
quickrules = "QuickStart: \n"
quickrules1 = "Type in 'new' to start a game. Enter how many rounds you want to play. Type in your choice of rock, paper, or scissors when prompted"
quickrules2 = "\nType in 'rules' to review the rules. Type in 'commands' to review the commands. Type in 'new' to start a new game.\n"
slowPrint(quickrules)
slowPrint(quickrules1)
slowPrint(quickrules2)



def check_input(user_input):
    """takes a string as a parameter and validates it"""

    if user_input.lower() == 'rules':
        with open("rules.txt", "r") as infile:
            rules = infile.read()
        slowPrint(rules, 0.007)


    elif user_input.lower() == 'commands':
        with open("commands.txt", "r") as infile:
            cmnds = infile.read()
        slowPrint(cmnds, 0.007)

    elif user_input.lower() =='new':
        slowPrint("Are you sure you want to start over? \nenter 'yes' or 'no': ")
        usure = input()
        if usure == 'yes':
            return False
        
    elif (user_input.lower() == 'rock') or (user_input.lower() == 'paper') or (user_input.lower() == 'scissors'):
        return True
    
    
        
    
def round_info(game, cp_choice):
    """displays information about a round"""

    slowPrint('\nYou chose: ' + game.player_choice)
    slowPrint('\nOpponent Chose: ' + cp_choice)

    if game.round_status == "won":
        slowPrint("\n" + game.player_name + ' ' + "won")
        slowPrint("\n** queue hip-hop horns **\n")

    elif game.round_status == "lost":
        slowPrint("\nOpponent" + " " + "won" )
        slowPrint("\nBetter luck next time...\n")
    
    else:
        slowPrint("\n It was a Draw!\n")
    
    B = threading.Thread(target=game.log_info, args=("round info",))
    B.start()
    if game.winner is not None:
        A = threading.Thread(target=game.log_info, args=("winner",))
        A.start()
        slowPrint("\nAnd the winner is: " + game.winner + "!!\n")
        slowPrint("The Score: \n" + game.player_name + ": " + str(game.rounds_won))
        slowPrint("\n" + "Opponent: " + str(game.num_of_rounds - game.rounds_won - game.rounds_draw))
        slowPrint("\nTotal Draws: " + str(game.rounds_draw))
        A.join()
        tablepipeline()
    B.join()
    
  
    


    

def playgame(user_name):
    """handles the actual playing of the game"""
    #starts a new instance of the game class
    new_game = game(user_name)
    
    slowPrint("Alright " + user_name + ", How many rounds would you like to play? ")
    rounds = int(input())
    # must add data validation
    new_game.set_rounds(rounds)
    rounds_played = 0
    new_game.log_info("name")
    new_game.log_info("rounds")
    #this while loop is meant to prompt the user to enter a choice for each round that is played
    while new_game.num_of_rounds > rounds_played:

        rnd1 = f"\nRound {new_game.current_round + 1}: \n"
        slowPrint(rnd1)
        prompt1 = "Please enter rock, paper, or scissors: "
        slowPrint(prompt1)
        choice = input()
        status = check_input(choice)
        if status == False:
            return
        
        elif choice == 'rock':
            cp_choice = new_game.rock()

        elif choice == 'paper':
            cp_choice = new_game.paper()
    
        elif choice == 'scissors':
            cp_choice = new_game.scissors()
        
        round_info(new_game, cp_choice)

        rounds_played += 1


        
        
        




while True:

    slowPrint("\nWould you like to start a new game? \nenter 'yes' or 'no': ")
    user_input = input()

    if user_input == 'yes':
        playgame(user_name)
        continue

    if user_input == 'no':
       slowPrint("\nAre you sure you want to exit the program?\n ")
       usure = input("enter 'yes' to exit, 'no' to stay: ")
       if usure == "no":
           continue
           
       slowPrint("ok" + " " + user_name + ". Have a good one! ") 
       exit()




