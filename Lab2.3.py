###################################
# Created by Owen Phillips        #
# Coding with Python Lab 2.3      #
# User Input                      #
# Northwood Tech College          #
###################################

# Initialization of the Calculator.

print('Welcome to the Lump Sum Loan Payment Calculator')
# Asking the user for their name.

firstName = input('What is your first name? ')
# Determining what the loan amount is, including a loop that denies

# anything other than a numerical value.

while True:
 
try:
 
loanAmt = float(input('What is the loan amount? $'))
 
break
 
except ValueError:
 
print('Please enter a valid number without commas.')
 
print()
 
# Determining the interest rate and ensuring the user

# uses a decimal value through an if/else statement that

# does not allow any value greater than 1.

while True:
 
try:
 
rate = float(input('What is the interest rate? (In decimal form: 10% = .10) '))
 
if rate < 1:
 
break
 
else:
 
print('Please enter a valid decimal value.')
 
print()
 
except ValueError:
 
print('Please enter a valid decimal value.')
 
print()
# Defining Variables.

calcRate = rate + 1
intRate = rate * 100
payment = loanAmt * calcRate
# The final output.

print(firstName + ', your lump sum payment of your $' + str(loanAmt) + \
 
' loan with ' + str(intRate) + '% interest is $' + str(payment))
