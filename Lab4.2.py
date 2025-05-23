###################################
# Created by Owen Phillips        #
# Coding with Python Lab 4.2      #
# Write to file                   #
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

#Writing to ipFile
ipFile = open('iplist.txt','w')
for item in addList:
    ipFile.write(f'{firstOct}.{item}\n')

ipFile.close()

