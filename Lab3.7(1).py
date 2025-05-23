###############################
# Created by Owen Phillips    #
# Coding with Python Lab 3.7  #
# Movie Recommendations       #
# Northwood Tech College      #
###############################

#Define the lists to be used throughout the script
movies = ['Inception', 'The Shawshank Redemption', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump',\
'The Matrix', 'The Godfather', 'Fight Club', 'The Lord of the Rings: The Fellowship of the Ring', 'The Avengers']
ratings = [8.8, 9.3, 9.0, 8.9, 8.8, 8.7, 9.2, 8.8, 8.8, 8.0]
genres = ['Sci-Fi', 'Drama', 'Action','Crime', 'Drama', 'Sci-Fi', 'Crime', 'Drama', 'Adventure','Action']

#Defining Functions to make it easier to call upon later on in the script

#Menu to show options
def returnmen():
    print('\n\nMovie Recommendations'\
      '\n\nPress:\n'\
      '1 - To display a movie list with their ratings\n'\
      '2 - To display recommendation based on rating\n'\
      '3 - To display movie recommendation based on genre\n'\
      '9 - Returns this menu.\n'\
      '10 - End the script\n\n')

#Function to display the movies and their ratings
def movrate():
    print('\nMovies and their ratings:\n')
    for item in range(len(movies)):
        print(f'{movies[item]} - Rating: {ratings[item]}')

#Function to print movies with an user-defined minimum rating        
def printminrate():
    while True:
        try:
            minRate = float(input('\nEnter the minimum rating you would like to see. 8.0 is the lowest and 9.3 is the highest.\n'\
                                  'Please enter as a decimal option between these options: '))
            if minRate >= 8.0 and minRate <=9.2:
                print(f'\nMovies with a rating equal to or higher than {minRate}:')
                for item in range(len(movies)):
                    if ratings[item] >= minRate:
                        print(f'{movies[item]} - Rating: {ratings[item]}')
                break
            else:
                print(f'\nYour value did not fall within the set boundaries. Please try again!\n')
        except ValueError:
            print('\nTry that again!')
    

#Function to print movies within a particular genre. Takes index values directly from the list to print
def genrate():
    print(f'\nYou can choose between the following genres:\n'\
          'Sci-Fi(1)\n' 'Drama(2)\n' 'Action(3)\n' 'Crime(4)\n' 'Adventure(5)\n')
    while True:
        try:
            genre = int(input('\nChoose an option (9 to exit the genre selection and return to main menu): '))
            if genre == 1:
                print('\nSci-Fi: \n')
                print(f'{movies[0]} - Rating: {ratings[0]}\n'\
                      f'{movies[5]} - Rating: {ratings[5]}')
            elif genre == 2:
                print('\nDrama: \n')
                print(f'{movies[1]} - Rating: {ratings[1]}\n'\
                      f'{movies[4]} - Rating: {ratings[4]}\n'\
                      f'{movies[7]} - Rating: {ratings[7]}')
            elif genre == 3:
                print('\nAction: \n')
                print(f'{movies[2]} - Rating: {ratings[2]}\n'\
                      f'{movies[9]} - Rating: {ratings[9]}')
            elif genre == 4:
                print('\nCrime: \n')
                print(f'{movies[3]} - Rating: {ratings[3]}\n'\
                      f'{movies[6]} - Rating: {ratings[6]}')
            elif genre == 5:
                print('\nAdventure')
                print(f'{movies[8]} - Rating: {ratings[8]}')
            elif genre == 9:
                print('Returning you to main menu!')
                break
            else:
                print('Try that again!')
                
        except ValueError:
            print('Try that again!')


#Loop that calls on the menu options. Includes options to return the menu and to kill the script.
returnmen()
while True:     
    try:
        menuopt = int(input('\nPlease enter your choice (9 to return the menu): '))
        if menuopt == 1:
            movrate()
        elif menuopt == 2:
            printminrate()
        elif menuopt == 3:
            genrate()
        elif menuopt == 9:
            returnmen()
        elif menuopt == 10:
            break
        else:
            print('\n Try that again!')
    except ValueError:
        print('\nTry that again!')

            
    
