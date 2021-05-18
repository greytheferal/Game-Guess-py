import random
lower = int(input("Enter Lower bound:- "))
upper = int(input("Enter Upper bound:- "))
number = random.randint(lower,upper)

player_name = input("Hello, What's your name?\n")
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between {} and {}' .format(lower,upper))
print('\n')
while number_of_guesses < 5:
    print('Choose a number :')
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
        print('\n')
    if guess > number:
        print('Your guess is too high')
        print('\n')
    if guess > upper:
        print('Out of range')
        print('\n')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))