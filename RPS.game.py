
#modules
import sys
import random
import difflib as dfb

#intro
#age checking
try:
    age = int(input(" Enter your age\n"))
except:
    try_again = True
    while try_again:
        age = int(input(" Enter your age again: "))
        if isinstance(age, int):
            try_again = False
            
if age < 3 or age > 200:# sorry you can't live to this age :○
    sys.exit('ACCESS DENIED')
elif age >= 9 or age <= 80:
        print('ACCESS GRANTED')
else:
    sys.exit('WRONG INPUT')
        
game_continue = True
rounds = 1
while game_continue:

    def getCloseInput(string, data_structure):
        """
    gets a str with a data_sturucture and returns and close opposite to str
        """
        close_matches = dfb.get_close_matches(string, data_structure, cutoff=0.2)
        return close_matches[0]
        
    computer_score_lst = []
    player_score_lst = []
    
    def resultsCounter(results):
        """
        func() to get results for each round
        """
        match results:
            case '😎 YOU WIN 🎉':
                player_score_lst.append(1)
                computer_score_lst.append(0)
            case "🐍 PYTHON WINS":
                computer_score_lst.append(1)
                player_score_lst.append(0)
            case 'DRAW 🤔':
                player_score_lst.append(0)
                computer_score_lst.append(0)
        tableResults(player_score_lst, computer_score_lst)
   
    def tableResults(list1, list2):
        """
        create a table with the results
        """
        print(f"'ROUNDS': {rounds}")#displays № of rounds played
        print(f"{'Player': <10}|{'Computer': ^10}| {'Rounds': >5}")#title of table
        for i in range(rounds):
            print(f"{list1[i-1]: <10}|{list2[i-1]: ^10}")#table content
       
    def gameChecker(player, computer):
        """
        to check with personality won a specific loop/round
        """
        if player == 'ROCK' and computer == 'SCISSORS':
            announcement = '😎 YOU WIN 🎉'
            print(announcement)
        elif player == 'PAPER' and computer == 'ROCK':
            announcement = '😎 YOU WIN 🎉'
            print(announcement)
        elif player == 'SCISSORS' and computer == 'PAPER':
            announcement = '😎 YOU WIN 🎉'
            print(announcement)
        elif player == computer:
            announcement = 'DRAW 🤔'
            print(announcement)
        else:
            announcement = "🐍 PYTHON WINS"
            print(announcement)
        return announcement
 
    answers = ['yes', 'y', 'no', 'y']#a list with common answer to loops
            

    """
to repeat the game
    """    
    print(" ")
    print("ROCK".ljust(14, ".") + " 🪨")
    print("PAPER".ljust(14, ".") + " 📃")
    print("SCISSORS".ljust(14, ".") + " ✂️") 

    playables = ['ROCK','PAPER','SCISSORS']#list of possibles choices

    player = input(f"   \nEnter... PLAY OF CHOICE \n 🪨 ROCK\n 📃 PAPER\n ✂ ️SCISSORS\n\n").upper()
    
    if player not in playables:
        #runs if user input is invalid
     
        keep_asking = True
        while keep_asking:
            #repeats asking
            close_playable = getCloseInput(player, playables)
            ask_player = input(f"error input. Did you mean {close_playable}? ").lower()
            #to check type of answer in answers_lst and stop or continue loop
            if ask_player in ['yes', 'y']:
                player = close_playable
                keep_asking = False
                    
            elif ask_player in ['no', 'n']:
                player = input(f"   \nEnter... PLAY OF CHOICE \n 🪨 ROCK\n 📃 PAPER\n ✂ ️SCISSORS\n\n").upper()
                if player in playables:
                    keep_asking = False
                        
    computer = random.choice(playables)#computers choice
    print()
    print(f"YOU CHOOSE: {player}")
    print(f"PYTHON CHOOSE: {computer}")
    print(" ")
    #main game results checking
    results = gameChecker(player, computer)#assigns results
    #ask to play again
    play_again = input('Do you want to play again? ').lower()
    print()
    match play_again:
        case 'yes':
            rounds+= 1
        case 'no':
            resultsCounter(results)
            game_continue = False #stops loop
        case _:
            play_again = getCloseInput(play_again, answers)
            play_again_error = input(f'Did you mean {play_again[0]}')
            if play_again.lower() in ['yes', 'y']:
                pass
            elif play_again.lower() in ['no', 'n']:
                game_continue = False
"""
signed by 0xG-MSK
goto to https://github.com/0xG-MSK :)
"""