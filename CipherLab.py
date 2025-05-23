#########################################
# Created by Owen Phillips              #
# Coding with Python Lab Caesar         #                   
# Northwood Tech College                #
#########################################

# Enter encrypted message, change to uppercase and define letters
message = input('Enter your encrypted text: ')
message = message.upper()
letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# Brute force all possibilities, user must determine the read-able one.
for key in range(26):
    messout = ''
    
    for char in message:
        if char in letters:
            num = letters.find(char)
            num = num - key
            
            if num < 0:
                num += 26
            
            messout += letters[num]
        else:
            messout += char
    
    print(f'Key #{key} : {messout}')
