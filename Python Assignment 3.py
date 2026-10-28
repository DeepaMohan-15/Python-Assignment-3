
#Number Guessing Game
import random
secret_number=random.randint(1,10)
#print(secret_number)
attempts=3
while attempts>0:
    guess=int(input("Guess the number between 1 and 10)="))
    if guess==secret_number:
        print("Congratulations! You guessed the correct number ")
        break
    else:
        print("Wrong guess! Try again")
        attempts=attempts-1
else:
        print("Better luck next time")
        print("The correct number was=",secret_number)
    
   
    
