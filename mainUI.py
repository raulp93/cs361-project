import time


def get_comp_choice():

    """
    gets a random number from a text file and uses it to select a random choice between 
    rock, paper, or scissors. Returns the choice.
    """
    choices = ["rock", "paper", "scissors"]

    with open("number-service.txt", 'w') as outfile:
        outfile.write("request")

    time.sleep(1)     # gives the number service time to fulfill  the request

    with open("number-service.txt", "r") as infile:
        num_str = infile.read()
    
    num_int = int(num_str)
    choice = choices[num_int % 3]

    return choice





class game:

    def __init__(self, cp_name, player_name):
        """ Creates the game object that holds all the different parameters"""

        self.cp_name = 'computer'
        self.player_name = player_name
        self.num_of_rounds = 1
        self.current_round = 0
        self.game_status = True    # True = rounds left in game        # False = no more rounds left in game
        self.round_status = None
        self.winner = None
        self.rounds_won = 0

    def set_rounds(self, num):
        """sets the number of rounds to be played"""
        self.num_of_rounds = num

    # The method below will be completed when integration with teammates microservices occurs

    # def set_cp_name(name):
    #     """gets a random name from a text file"""
        
    #     with open("request.txt", 'w') as outfile:
    #         outfile.write("request")

    #     with open("response.txt", 'r') as infile:


    def rock(self):
        """method that is called when a player chooses rock"""
        cp_choice = get_comp_choice()

        choice = "rock"

        if choice == cp_choice:
            self.round_status = 'draw'
        
        elif choice == 'paper':
            self.round_status = 'lost'

        else:
            self.round_status = 'won'
            self.rounds_won += 1
        
        self.current_round += 1


        


    def paper(self):
        """method that is called when a player chooses paper"""
        cp_choice = get_comp_choice()

        choice = "paper"

        if choice == cp_choice:
            self.round_status = 'draw'
        
        elif choice == 'scissors':
            self.round_status = 'lost'

        else:
            self.round_status = 'won'
            self.rounds_won += 1
        
        self.current_round += 1


    def scissors(self):
        """method used when a player chooses scissors"""
        cp_choice = get_comp_choice()

        choice = "scissors"

        if choice == cp_choice:
            self.round_status = 'draw'
        
        elif choice == 'rock':
            self.round_status = 'lost'

        else:
            self.round_status = 'won'
            self.rounds_won += 1
        
        self.current_round += 1
    


    


    


