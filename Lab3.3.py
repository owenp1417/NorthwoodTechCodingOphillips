###################################
# Created by Owen Phillips        #
# Coding with Python Lab 3.3      #
# Age Guesser                     #
# Northwood Tech College          #
###################################

#Defining variables

low = 1
high = 100
attempt = 0
#Initialization of program

print('I\'m going to guess your age! Please respond with either - higher, lower\
or correct')
#Guesses to find age

for val in range(8):
    guess = int((high + low) / 2)
    answer = input(f'Are you {guess} years old?: ')
 
    if answer == 'correct' or answer == 'Correct':
        print(f'Got it in {attempt} attempts!')
        break
    elif answer == 'lower' or answer == 'Lower':
        high = guess
    elif answer == 'higher' or answer == 'Higher':
        low = guess
        attempt = attempt + 1
