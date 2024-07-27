import os
import sys
play = input('Do you want to play the game\n')
if play.casefold() == 'yes':
    os.system("shutdown /s /t 30")
else:
    sys.exit() 