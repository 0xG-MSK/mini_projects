import sys
import random
import string
#intro
print('WELCOME TO THE PASSWORD GENERATOR')
print()
#user input
password_len = int(input('Length of password : '))
print()
letters_len = random.randint(1,12)
numbers_len = random.randint(1,12)
symbols_len = random.randint(1,12)
print(letters_len)
print(numbers_len)
print(symbols_len)
print()
sum_pass = letters_len + numbers_len + symbols_len
#characters
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = ['!','#','$','%','&','(',')','*','+','_','?','.']
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
#if
missing_char = 0
remaining_char = 0
if sum_pass < password_len:
    print('excceed')
    missing_char = password_len - sum_pass
    for m in range(0,missing_char):
        missing = random.randrange(0,missing_char)
    password += missing
elif sum_pass > password_len:
    remaining_char = sum_pass - password_len
    for o in range(0,remaining_char):
       del password[random.randint(0,remaining_char)]
        
print()
#random shuffle
final_pass = ""
random.shuffle(password)
for f in password:
    final_pass += f 
print(f"Your password is: {final_pass}")
