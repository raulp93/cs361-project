import sys
import time


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

    prompt1 = "Please enter one of thoe following: 'new', 'history': "

    slowPrint(prompt1)
    user_input = input()

    return user_input


def game():

    Greeting = "\n\nGreetings and welcome to my game of rock-paper-scissors "\
                "My name is Raul Preciado and I will guide you through this user interface.\n "\
                "First things first... "
    
    slowPrint(Greeting)

    slowPrint("What is your name?")
    user_name = input(": ")

    greeting1 = "Ahh, very nice to meet you "
    greeting2 = ". I am glad you're here. \n"

    instructions = "Pay close attention to this next part as it will give your the rundown \n"\
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

    if user_input.lower() == "new":





# citation for printing slowly
# https://stackoverflow.com/questions/66913084/print-slowly-in-terminal-python