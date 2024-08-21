#modules
import random as r
import sys

#resources
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
ACE = 11
#personalities in game
#intro
print(f"WELCOME TO BLACKJACK: WANNA PLAY!? ")
print()
print("""$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$$$$$$$$$$$XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX$$$$$$$$$$$
$$$$$$XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX$$$$$$
$$$$XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX$$$$
$$$XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX$$$
$$$XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX$$$
$$$XXXXXXXXXXXXXXXXXXXXXXXXXXXXX:.......::;;++xxXXXXXXXXXXXXXXXXXXXxx+xXXXXXXXXXXXXXXXXXXXXXXXXXXX$$
$$$XXXXXXXXXXXXXXXXXXXXXXXXXXXX:.......................:;;::::::::::::::+XXXXXXXXXXXXXXXXXXXXXXXXX$$
$$$XXXXXXXXXXXXXXXXXXXXXXXXXXXx......:$&;...........................::::;xXXXXXXXXXXXXXXXXXXXXXXXX$$
$$$XXXXXXXXXXXXXXXXXXXXxx++;;;:......;&$......................................::;;;++xXXXXXXXXXXX$$$
$$$XXXXXXXx+;::..............:.......+&+.................................................:::::+X$$$$
$$$XXXXX;....................:....:..x&:................................................::::::::X$$$
$$$XXXXX......+;............::...+&;:$X................................................::::::::;x$$$
$$$XXXXX.....:xx;...........::....:+x;.....:;:.......................................::::::::::;X$$$
$$$XXXXX:....+:+x:..........::............+.......:;++x+;:::::...................::::::::::::::;$$$$
$$$XXXXX;...:+:;xx:.........:....:+&$;....+....;$$:...:XX&XX&$$XXXXxx++;;:.....::::::::::::::::+$$$$
$$$XXXXX+...;:..:xx:.......::...X&&&&&X..::.:x&&&&&+...;$$&&&$&&$$$&XX$$X$;:::;++;::::::::::::;x$$$$
$$$XXXXXx..:+:...+xx+......::...X&&&&&&..;.x&&&&&&&&$:..X$$$$$$$$$$X$$$$x:::::::::+:::::::::::;X$$$$
$$$XXXXXx:.:...............:......x&;;:..;;&&&&&&&&&&X.:+x++++++.;++xxx::::::;++++::::::::::::+X$$$$
$$$XXXXXX:....;:.+x;......::............:;.&&&&&&&&&&x;+xx++xx;:.xXX+;:::::::;+;+x::::::::::::+X$$$$
$$$XXXXXX;..:xxxxxxx:.....::............:;..:+;&$$&$+;++Xxxxx+:...:x:;::::::::x+:+:::::::::::;x$X$$$
$$$XXXXXX+...+xxxxx+:.....::............:;...:$&$:.:;xxxxxxx+x+::::+;+;:::::;+xx+;:::::::::::;X$X$$$
$$$XXXXXXx.....;xx:......::.............;:......::;xxx+xxX++X:::;XXx++:::::::+;;;::::::::::::;X$X$$$
$$$XXXXXXX...............::.............X&&x:;x&XXxx+&&Xx$Xx;++:::::+:::::::+++++::::::::::::+XXXX$$
$$$XXXXXXX:..............::.............&&&;$$$&xxxX+&$$x$xxXXXXXxx$x:::::::++x++::::::::::::x$XXX$$
$$$XXXXXXX+.............:::............;&&+X$$+XX+X+x&XXXX$XXXxxX$&+xXx::;+::xX;;:::::::::::;XXXXX$$
$$$XXXXXXXx.............:::............x&&;&$xXXXXxxX&XXx+;XXXXX&X+X+&&$X+:;$xx+;:::::::::::;XXXXX$$
$$$XXXXXXX$.............::.............$&$+$$x$Xxx$&&&&$$XxXXX$$+xx+x$$$&$x;x+x+::::::::::::+$XXXX$$
$$$XXXXXXXX:...........:::............;&&&;&$x$Xxx+$$&$$&&&&$&XxX+xX$XXX$$&&X;:+:::::::::::;xXXXXX$$
$$$XXXXXXXX+...........:::............++$&+$$Xx$XxxX$X&$$&$&&&$x+X$xX+X+xXX$&$X+:::::::::::;XXXXXX$$
$$$XXXXXXXXx...........:::............XXxx$;$$XxXXxx$X$X$$X$$&&xXXXx$$Xxxx$x$$&;:::::::::::+XXXXXX$$
$$$XXXXXXXXX:.........:::...........::x$XxxXx$X$xXXXx$$XXX$$X&&$$xx&&&x$$x$XX$$:::::::::::;+XXXXXX$$
$$$XXXXXXXXX:.........:::.......:::::;$XxxXxxx$X$+XxX&&Xxx$$&&&$&$&X+$XxX$+$XXx:::::::::::;xXXXXXX$$
$$$XXXXXXXXX;.........:::.....:::::::;XXXxxXx$+X$&$Xx&&$++;;+X&XxxX$$XxxXXX+$X;:::::::::::;XXXXXXX$$
$$$XXXXXXXXX+........:::.:..:::::::::+XxXx$$XX&$xx$$$&&$$X$$$&$XXXxx$$$+xX$xxX::::::::::::+XXXXXXX$$
$$$XXXXXXXXXx:.......:::.::::::::::::X$XxXx$$x&&Xx$++&&$$XX$XX$xxXXX+$$&+xXX+X::::::::::::+XXXXXXX$$
$$$XXXXXXXXXx:......::::.:::::::::::;$&&$$+$$x&x$$xxx$&&$&$$X$$XxXXxxX$$XX$xXx::::::::::::xXXXXXXX$$
$$$XXXXXXXXXX:......::::.:::::::::::;+X$&&$$$+x$XX+xX;$&&&$&$&$$XxxXXxX$$x$&$+::::::::::;;XXXXXXXX$$
$$$XXXXXXXXXX;....::::::::::::::::::+;XxX$&&$&XXxxXxx&$XX$&&&&&&&XxxxxX$$x$&$;::::::::::;;XXXXXXXX$$
$$XXXXXXXXXXX+...:::::::::::::::::::x+Xx;;x$&&$XxX+X&XXXx++XXX$&xXXxXxX$Xx$&X;::::::::::;+XXXXXXXX$$
$$XXXXXXXXXXXX.::::::::.:::::::::::;+xxx:;;:x$xX+x&XXX$$XxXXXX$XxxXXXx$$$X&&X:::::::::;;;xXXXXXXXX$$
$$XXXXXXXXXXXX.::::::::.::::::::;;;x+xXXXxXXXXXXXXXXXXXXXXXxxXXxXxX+&$$XXX&$x:;:::;;;;;;;XXXXXXXXX$$
$$$XXXXXXXXXXX;:::;;+xxXXX$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$XXxx++;;;;;;;+XXXXXXXXX$$
$$$XXXXXXXXX$$$$$$$$$$$$$$$$$$$$$$$$$$$X$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$XXXXXXXXXXXXX$$
$$$$X$$$&$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$X$$$X$$$$$$$$XX$$$$
$&&&&&&&$$X$$$$$$XXXX$$$$$$$$XX$$$$$$$$XXX$$$XXXX$XXXX$$$$XXXX$$$$$X$$$$$$$$XXX$$$XXXXX$$X$$$&&&&&&$
&&&&&&&&+::::::+x;.::X$$$$$$x::x$$$$+::::::x+:.:;X::.:X$$x::.:x$$$;.;$&$$X;:::::+x::.:x+:::+$&&&&&&&
&&&&&&&&$+:+$X::xX::x$$$$$$X:::;X$$+:;X$X;:;X+:;X+:;X$$$$$X;:X$&&+:::x$&X;:x$$+::XX;:XX;:x$&&&&&&&&&
&&&&&&&&$+;;;;;+$$;;X$$$$$$+;x+;+$$;;x$$$$X$$x;;;;+$$&$$$$X;;X&&X;+x;;X&x;;$$&$$$&$;;+;;X&&&&&&&&&&&
&&&&&&&&$x;x$$+;x$;+X$$$X$x;;;;;;x$+;+$$$$$$$x;+X+;+$&X++$X+;X$X;;;;;;+$X;;X$&&$$$$+;xX+;X&&&&&&&&&&
&&&&&&&&$x;x$$+;x$;+X$X+xX;x$$$x;+X$;;x$$x;x$x;+$$x;+$X;+$X;+$$+;$&&$+;x$x;+X$$++$$+;$$X+;x$&&&&&&&&
&&&&&&&&XxxxxxX$$xxxxxxxXxxxX$Xxxxx$$XxxxX$$XxxxX$xxxxX$xxxX&$xxxx$$xxxxX$$XxxxX$$xxxx$XxxxX$&&&&&&&
&&&&&&&&$$&&&&&&&$&&&&&&&&&&&&&&$&&&&&$&&&&&$&&&&&&&&&&&&&&&&&&&&&&$&&&&&&&&&&&&&&$&&&&&&&$$&&&&&&&&
&&&&&&&&&&&&&&&&&$&&&&&&&&$$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&""")
def randomCard(cards):
    """
func? to generate two random cards for
personalities     
    """
    random_cards = []
    for i in range(2):
        r.choice(cards)
        random_cards.append(r.choice(cards))
    return random_cards

def is_lst_empty(lst):
    """
func? to check if a list is empty
    """
    len(lst)
    if len(lst) != 0:
        return True
    elif len(lst) == 0:
        return False
print()
deal = input("DEAL?: ")#deal, a word used to start the game
print()

match deal:
# match-case is a feature that gets the variable and compares it to the cases
    case 'yes':
        user = randomCard(cards) #adds cards to user
        custom_user = ", ".join([str(x) for x in user])# customizes user's card output
        print(f"You have: {custom_user}")
        computer = randomCard(cards) #adds cards to computer
        custom_computer = ", ".join([str(x) for x in computer])
        print(f"Dealer : {min(computer)}, ?")
    case 'no':
        sys.exit(f"PLAYER LEFT ")
    case _:
        print(f"incorrect")
        try_again = 0
        while try_again < 2:
            deal = input('DEAL? ')
            if deal == 'yes':
                user = randomCard(cards) #adds cards to user
                custom_user = ", ".join([str(x) for x in user])# customizes user's card output
                print(f"You have: {custom_user}")
                computer = randomCard(cards) #adds cards to computer
                custom_computer = ", ".join([str(x) for x in computer])
                print(f"Dealer : {computer[r.randint(0,1)]}, ❓️")
                try_again = 2
            elif deal == 'no':
                sys.exit("PLAYER LEFT")
            try_again += 1
            if try_again == 2:
                if deal != 'yes':
                    sys.exit('try again')
                elif deal != "no":
                    sys.exit('try again')
            
def add_randomCards(user,computer):
    """
func? to add the add the cards of persons
    """    
    for i in range(2):
        total_user = user[0] + user[1]# uses index value
        total_computer= computer[0] + computer[1]
    return total_user, total_computer #returns the sum of the list elements for both personalities
    
result = add_randomCards(user,computer)
total_user = result[0] #assigns the result value, total_user of the function add_randomCards to var total_user
#straight win, finds if one personality gets a royal and Ace
ace_combo = [11, 10]
"""
compares all personalities to the straight win list
and reverse
"""
print()
if user == ace_combo and computer == ace_combo:
    print('DRAW 🫱🏼‍🫲🏾\nUSER: {custom_user} | DEALER: {custom_computer}')
elif user == ace_combo:#compares
    print(f"YOU WIN 💵💰\n USER: {custom_user} | DEALER: {custom_computer}")
    sys.exit()
elif user == sorted(ace_combo, reverse=True):#code0 reverses the ace combo list and checks it
    print(f"YOU WIN 💵💰\n USER: {custom_user} | DEALER: {custom_computer}")
    sys.exit()
elif computer == ace_combo:
    print(f"DEALER WINS 💀🤖\n USER: {custom_user} | DEALER: {custom_computer}")
    sys.exit()
elif computer == sorted(ace_combo, reverse=True):#same as code0
    print(f"DEALER WINS 💀🤖\n USER: {custom_user} | DEALER: {custom_computer}")
    sys.exit()
#result[0] - total_user //add_randomCard()
#result[1] - total_computer //add_randomCard()


    
if result[0] > 21:#checks if user > 21
    sys.exit("YOU LOSE. BUST ❌️")
elif result[0] < 21:#if not,
    hit_again = True
    while hit_again:
        #creates a loop to continue asking user it they want to hit up a card
        print()
        hit = input("Do you want to HIT?: ")
        print()
        if hit == 'yes':#if yes
                user.append(r.choice(cards))#adds a card
                custom_user = ", ".join([str(x) for x in user])#customizes the list output
                print(f" You have: {custom_user}")
                print()
                total_user = sum(user)#adds all elements in user's list and and assigns to a new var
                if 11 in user:#checks if 11 is in the user's
                    if total_user > 21:
                        ace_or_not = int(input('You got an Ace. Will you pick 11 or 1? '))
                        match ace_or_not: #option to choose whether 1 or 11, user gets and ace, and the sum of the cards is over 21
                            case 1:
                                for i in user:
                                    if i == 11:
                                        index = user.index(11)
                                        user[index] = 1
                            case 11:
                                for i in user:
                                    if i == 11:
                                        i = 11
                        custom_user = ", ".join([str(x) for x in user])                
                        print(f"You have: {custom_user}")
                        total_user = sum(user)
                        if total_user > 21:
                            sys.exit("YOU LOSE. BUST ❌️")
                        elif total_user < 21:
                            pass
                elif total_user > 21:
                    sys.exit("YOU LOSE. BUST ❌️")  
                elif total_user < 21:
                    if 11 in user:
                        ace_or_not = int(input('You got an Ace. Will you pick 11 or 1? '))
                        match ace_or_not:
                            case 1:
                                for i in user:
                                    if i == 11:
                                        index = user.index(11)
                                        user[index] = 1
                            case 11:
                                for i in user:
                                    if i == 11:
                                        i = 11
                        
                        print(f'You have: {user}')
                        total_user = sum(user)
                        if total_user > 21:
                            sys.exit("YOU LOSE. BUST ❌️")
                        elif total_user < 21:
                            pass
                elif total_user == 21:
                    print(f'YOU WIN 💵💰\n USER: {custom_user} | DEALER: {custom_computer}')
                    sys.exit()
        elif hit == 'no':# if users no more wants a card
            if 11 in user:
                ace_or_not = int(input('You got an Ace. Will you pick 11 or 1? '))
                match ace_or_not:
                    case 1:
                        for i in user:
                            if i == 11:
                                index = c.index(11)
                                i = 1
                    case 11:
                        for i in user:
                            if i == 11:
                                i = 11
                custom_user = ", ".join([str(x) for x in user])                
                print(f"You have: {custom_user}")
                total_user = sum(user)  
            hit_again = False #ends the loop
            if result[1] < 17:#when total_computer is below, 17 only before code runs
               total_user = sum(user)#this var was called here, to make the code below run
               if result[1] > total_user:
                     custom_computer = ", ".join([str(x) for x in computer])#customizes list output
                     print(f"DEALER WINS: 💀🤖\n USER: {custom_user} | DEALER: {custom_computer}")
                     sys.exit()
               elif result[1] < total_user:#if result of function < total_user
                   computer.append(r.choice(cards))
                   custom_computer = ", ".join([str(x) for x in computer])
                   total_computer = sum(computer)
                   if 11 in computer:
                       if total_computer > 21:
                           print(f"DEALER LOST. YOU WIN 💵💰\n USER: {custom_user} | DEALER: {custom_computer}")
                           sys.exit()
                   elif total_computer > 21:
                       print(f"DEALER LOST. YOU WIN 💵💰\n USER: {custom_user} | DEALER: {custom_computer}")
                       sys.exit()
                   elif total_computer == 21:
                       print(f"DEALER WINS 💀🤖 \n USER: {custom_user} | DEALER: {custom_computer}")
                       sys.exit() 
            elif result[1] > 17:
                print(f'DEALER LOSES. YOU WIN 💵💰\n USER: {custom_user} | DEALER: {custom_computer}')
                sys.exit()
"""
below are variables that are called if the conditions above are not called
"""
print()
custom_user = ", ".join([str(x) for x in user])
custom_computer = ", ".join([str(x) for x in computer])             
total_user = sum(user)
total_computer = sum(computer)
if total_user > total_computer:
    print(f"YOU WIN 💵💰\n USER: {custom_user} | DEALER: {custom_computer}")
    sys.exit()
elif total_user < total_computer:
    print(f"DEALER WINS 💀🤖\n USER: {custom_user} | DEALER: {custom_computer}")
    sys.exit()
elif total_user == total_computer:
    print(f"DRAW 🫱🏼‍🫲🏾\n USER: {custom_user} | DEALER: {custom_computer}")
    sys.exit()                                              
