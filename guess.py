#guess the number game.

import random
name = input('Hi there, what is your name? ').strip()

secretNum = random.randint(1,20)
print('Well ' + name + ', I am thinking of a number between 1 and 20... Can you guess it?')

#ask player for input only 6 times

for numGuesses in range(1,7):
    print('Take a guess!')
    guess = int(input())
    if guess < secretNum:
        print('Your number is too low')
    elif guess > secretNum:
        print('Your number is too high')
    else:
        break

if guess == secretNum:
    print('Congrats! you have guessed the right number in ' + str(numGuesses) + ' tries!')
else:
    print('Out of guesses! :(')
    print('The number I was thinking of was ' + str(secretNum))
