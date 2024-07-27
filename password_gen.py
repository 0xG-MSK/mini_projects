print("PASSGeN 0.1".center(50,'-'))
import string as s
import math as m
import random as rd
import sys
#basic characters
letters_lower = list(s.ascii_letters[0:26])
letters_upper = list(s.ascii_letters[26:52])
digits = list(s.digits)
symbols = ['$','(',')','#','!','?','_','&','%','@','.']
#password lenght
print()
pass_lenght= int(input('How long is the password: '))
equal_pass_ratio= round((pass_lenght/4),1)

#
par_password = []
for ll in range(0,m.floor(equal_pass_ratio)):
    random_l_lower = rd.choice(letters_lower)
    par_password += random_l_lower

dynamic_condition1= 0
while dynamic_condition1 < m.floor(equal_pass_ratio):
    random_l_upper = rd.choice(letters_upper)
    par_password += random_l_upper
    dynamic_condition1 += 1

for lu in range(m.ceil(equal_pass_ratio)):
    random_digits = rd.choice(digits)
    par_password += random_digits

#remaining
remainder = pass_lenght-len(par_password)
#
dynamic_condition2 = 0
while dynamic_condition2 < remainder:
    random_symbols = rd.choice(symbols)
    par_password += random_symbols
    dynamic_condition2 += 1

#shuffle
final_password = ""
rd.shuffle(par_password)
print()
print()
#replacing variables
for i in par_password:
    final_password += i
print(f"Your password : {final_password}")


#saved
