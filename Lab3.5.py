###################################
# Created by Owen Phillips        #
# Coding with Python Lab 3.5      #
# Working with Lists              #
# Northwood Tech College          #
###################################



#Define first octet
while True:
    firstOct = input('Please enter the first three octets of the IP Address range. DO NOT put a dot\
 at the end. ')
    #Check for empty input
    if firstOct:
        break
    else:
        print('Input cannot be empty. Try again.')
        
#All the final octect options
while True:
    try:
        firstLastOct = int(input('First number in address range: '))
        lastOct = int(input('Last number in address range: '))
        addList = list(range(firstLastOct, lastOct+1))
        break
    except ValueError:
        print('Invalid input. Try again.')
#Asks user how they want their list to be outputted
while True:
    order = input('Would you like your list in ascending or descending order? ')

    if order.lower() == 'descending':
        addList.sort(reverse=True)
        for int in addList:
            print(f'{firstOct}.{int}')
        break

    elif order=='ascending' or order=='Ascending':
        for int in addList:
            print(f'{firstOct}.{int}')
        break
    else:
        print('Invalid input. Please enter "ascending" or "descending"')

    
