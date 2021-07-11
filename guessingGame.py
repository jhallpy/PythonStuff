from random import randrange
import math
check = True
cont = ""
score = 0
while check:
    rand = randrange(1,10)
    print(rand)
    guess = input("Guess the number between 1 and 10! ")
    try:
        guess = int(guess)
        if(guess == rand):
            print("Good job, you got it right! ")
            score += 1
        else:
            print("You were off by " + str(abs(guess-rand)))
        cont = input("Would you like to play again?(y/n) ")
        if(str.lower(cont)=="y"):
            check = True
        else:
            print("Thank you for playing! Your score was: " + str(score))
            check = False
            
    except ValueError:
        print('Please type a number!')


