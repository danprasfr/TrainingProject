import os
from random import randrange
from math import ceil
Money=1000
Random_Number = randrange(50)
Continue_partie=True
Bet =-1

while Continue_partie:
    Guess_Number = -1
    print ( "you are comming to casino with money", Money,"$")
    while Guess_Number <0 or Guess_Number>49:
        Guess_Number=input("Enter your guess number which should be between 1 to 49 ")
        try:
            Guess_Number=int(Guess_Number)
        except ValueError:
            print("Value should be Numeric")
            Guess_Number=-1
            continue
        if Guess_Number<0:
            print("you have enter a negatif value, this value should be strictly positif ")
        if Guess_Number >49:
            print("Value should be below 50")

    while  Bet <0 or Bet >Money:
        Bet=input("Enter your bet sum")
        try:
            Bet = int(Bet)
        except ValueError:
            print("Value should be Numeric")
            Bet=-1
            continue
        if Bet<=0:
            print("Bet value should be striclty positif and above 0 ")
        if Bet >Money:
            print("Bet value should be below than ", Money, "$")
    print("Random number is : ",Random_Number)
    if Guess_Number == Random_Number:
        print ( "you have correctly guessed the number ")
        Money +=  Bet*3


    elif Guess_Number % 2 == Random_Number %2:
            print ("you got the same color")
            Money +=ceil(Bet*0.5)
    else:
        print ("sorry friend you are loosing your bet")
        Money-=Bet

    if Money <=0 :
        print ("You loose all your money , Game will be stopped.")
        Continue_partie=False
    else:
        print ("you got for instance", Money,"$")
        Quit=input("Do you want to quit (o/O)?")
        if Quit =="o" or Quit=="O":
            print(" you are qutting the game with money", Money, "$")
            Continue_partie=False
os.system("pause")



