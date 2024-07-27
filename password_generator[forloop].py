import sys
import random
import string
#intro
print('WELCOME TO THE PASSWORD GENERATOR')
print()
#user input
password_len = int(input('Length of password : '))
print()
letters_len = int(input('Length of letters: '))
numbers_len = int(input('Length of numbers: '))
symbols_len = int(input('Lenght of symbols: '))
print()
sum_pass = letters_len + numbers_len + symbols_len
#characters
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!','#','$','%','&','(',')','*','+','_','?','.']
#if 
if sum_pass > password_len:
    sys.exit('Password lenght exceeded')
#password
password = []
#random, forloop
#random letters
for l in range(0, letters_len):
    ran_letters = random.choice(letters)
    password += ran_letters
#random numbers
for n in range(0, numbers_len):
    ran_numbers = random.choice(numbers)
    password += ran_numbers
#random symbols
for s in range(0, symbols_len):
    ran_symbols = random.choice(symbols)
    password += ran_symbols
print(password)
print()
#random shuffle
final_pass = ""
random.shuffle(password)
for f in password:
    final_pass += f 
print(f"Your password is: {final_pass}")

    
    
