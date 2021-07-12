from random import choice

score = 0
check = True

while check:
    rps = ["rock","paper","scissors"]
    cpu = choice(rps)
    user = str.lower(input("Rock, Paper, Scissors: "))
    if user == cpu:
        print("Tie!")
    elif user == 'rock' and cpu == 'paper':
        print('You chose rock versus paper. You lose!')
    elif user == 'rock' and cpu == 'scissors':
        print('You chose rock versus scissors. You win!')
        score+=1
    elif user == 'paper' and cpu == 'scissors':
        print('You chose paper versus scissors. You lose!')
    elif user == 'paper' and cpu == 'rock':
        print('You chose paper versus rock. You win!')
        score+=1
    elif user == 'scissors' and cpu == 'rock':
        print('You chose scissors versus rock. You lose!')
    elif user == 'scissors' and cpu == 'paper':
        print('You chose scissors versus paper. You win!')
        score+=1
    else:
        print('Please choose Rock, Paper, or Scissors next time!')
        continue

    cont = str.lower(input('Would you like to play again?(y/n) '))
    if(cont!="y" or cont!='yes'):
            check = False
            print("Thank you for playing! Your score was: " + str(score))
        

