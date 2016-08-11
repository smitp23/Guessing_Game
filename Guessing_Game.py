import random

def checking(i):
    try:
        float(i)
        return True
    except ValueError:
        return False


play = True
proceed = False


while True:
    rand = random.randint(1,9)
    guessCount = 0
    userGuess = raw_input("Guess a number:   ")
    if userGuess == "exit":
        quit()
    else:
        #print (type(userGuess))
        
        if checking(userGuess) == False:
            while proceed == False:
                print('Enter a valid input')
                userGuess = raw_input("Guess a number:   ")
                if userGuess == "exit":
                    quit()
                if checking(userGuess) == True:
                    proceed = True                                           
        
        while True:
            userGuess = int(userGuess)
            if userGuess == rand:
                guessCount = guessCount + 1
                print('You guessed right! Your guess count: %d' % (guessCount))
                print('Starting new game')
                break
            else:
                print('You guessed wrong!')
                if userGuess < rand:
                    print('Your guess was less than the random')
                    guessCount = guessCount + 1
                    #print(rand-userGuess)
                else:
                    print('Your guess was higher than the random')
                    guessCount = guessCount + 1
                    #print(userGuess-rand)

                print('Try again')

            proceed = False
            userGuess = raw_input("Guess a number:   ")
            if userGuess == "exit":
                quit()
            else:
                if checking(userGuess) == False:
                    while proceed == False:
                        print('Enter a valid input')
                        userGuess = raw_input("Guess a number:   ")
                        if userGuess == "exit":
                            quit()
                        if checking(userGuess) == True:
                            proceed = True               
