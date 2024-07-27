import sys

print(''' ____  _____ _   _ ____   ____ ______   ______ _____ 
/ ___|| ____| \ | |  _ \ / ___|  _ \ \ / /  _ \_   _|
\___ \|  _| |  \| | | | | |   | |_) \ V /| |_) || |  
 ___) | |___| |\  | |_| | |___|  _ < | | |  __/ | |  
|____/|_____|_| \_|____/ \____|_| \_\|_| |_|    |_|  ''')

print("WELCOME TO SENCRYPT")
print()
import string
#increase number of elements in list
alphabets = list(string.ascii_letters)
for i in range(38):
    alphabets += list(string.ascii_letters)
repeat = True
while repeat:
    mode = input("● Encode or ● Decode:\n").lower()
    #mode 
    #encode,
    #decode
    modes = ['encode','decode']
    if mode == 'encode':
        print()
        message = input('Type message: ')
    elif mode == 'decode':
        print()
        message = input('Enter encrypted text: ')
    #mode validation
    else:
        print()
        try:
            """
            checks user input for validation and prompt 
            re-input
            """
            mode= input('Please try again: Encode or Decode: ')
            print('')
            if mode not in modes: #if wrong input persist, a while is created for re-inputs
                try_again = True
                while try_again:
                    mode = input('Please try again: Encode or Decode: ')
                    print()
                    if mode in modes:
                        try_again = False #condition for terminating loop
            if mode == 'encode': #message inputs
                message = input('Type message: ')
            elif mode == 'decode':
                message = input('Enter encrypted text: ')
        except:
            sys.exit('error')
    #shift validation
    #checks if shift input is correct       
    print()
    try:
        shift = int(input('Enter shift number: '))
    except:
        if isinstance(shift, int): #checks whether shift is int
            pass
        elif not isinstance(shift,int):
                raise ValueError('Please enter a valid shift')


    #sys of encrytion
    #function encrypt()
    #for encrypting message input, #CIPHER
    def encrypt(cipher_text, shift_num):
        """
        for encryption of message using
        a shift key
        """
        cipher_text = ""
        for e in message:
            if e in alphabets: #if indexed char is element of str
                pos = alphabets.index(e)
                new_pos = pos + shift_num
                try: #to eradicate indexERROR 
                    new_e = alphabets[new_pos]
                except: #ask a re-input
                    try_again = True
                    while try_again:
                        shift = int(input('Out of Range: Enter a valid shift'))
                cipher_text += new_e
            elif e not in alphabets: #adds strange element to cipher_text
                cipher_text += e
            else: #after adding strange element, bypass code with 'pass' keyword
                new_pos = pos + shift_num
                new_e = alphabets[new_pos]  
                cipher_text += new_e
                pass
                print()
        print(f'Encryted text: {cipher_text}')
        
    #sys of decryption
    #function decrypt()
    def decrypt(text, shift_num):
        text = ""
        for d in message:
            if d in alphabets:
                pos = alphabets.index(d)
                new_pos = pos - shift_num
                try:
                    new_d = alphabets[new_pos]
                except:
                    try_again= True
                    while try_again:
                        shift= int(input('Out of Range: Enter a valid shift: '))
                text += new_d
            elif d not in alphabets:
                text += d
            else:
                new_pos = pos - shift_num
                new_d = alphabets[new_pos]  
                text += new_d
                pass
                print()
        print(f"Decoded text: {text}")

    #if @nd else stats
    if mode == 'encode':
        encrypt(message, shift)
    elif mode == 'decode':
        decrypt(message, shift)
    else:
        sys.exit()
    print()
    ask_to_repeat = input('Do you want to repeat?: ').lower() #repeat the operation again
    if ask_to_repeat == 'yes':
        pass
    elif ask_to_repeat == 'no':
        repeat = False
