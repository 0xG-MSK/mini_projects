print('WELCOME TO THE GUESS GAME')
import sys
import random
import words

lives = 6
lives_img = ['❤️','❤️','❤️','❤️','❤️','❤️']
print('.'.join(lives_img))# prints out the hearts
random_word = random.choice(words.gwords)
print()
#how to play
def how_to_play():
    print('''0. THE GAME starts with 6 ❤️'s and,
  you are you to maintain till finsh and WIN!,
  You are to guess a letter that fits the blank
  spaces accuratly to form word, if not you lose ️
  ❤️   ''')
#display
display = []
for _ in random_word:
    display += '_'# prints out the spaces of hidden letters
print(" ".join(display))
#description
print()
info = input('How to play? y/n: ').lower()
if info == 'y':
    how_to_play()
else:
    pass

end = False
while not end:
    print()
    user_input = input(' Guess a letter: ')       
    for r in range(len(random_word)):
        letter = random_word[r]# assigns the the current index of r to var letter
        if letter == user_input: #checks if the letter is same as var user_input 
            display[r] = letter# replaces empty '_' with the guessed letter
    if user_input not in random_word:
        print()
        lives -= 1
        lives_img.remove('❤️')
        lives_img.append('💔')#removes the heart and replaces with broken heart 
        print(f'You lost a heart 💔')
        print(".".join(lives_img))
        if lives == 0:
            end = True # ends game loop
            print()
            print("PLAYER DIED 💀")
            print(f"The word was: {random_word}")

    print(" ".join(display))

    if '_' not in display:
        end = True
        print()
        print('YOU WIN ')
