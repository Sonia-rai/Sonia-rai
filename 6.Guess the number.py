# Problem Statement


import random


def Guess_game(a, b, num):
    trails = 1
    while True:
        guess = int(input(f"Guess the number between {a} and {b} :"))
        if a <= guess <= b:
            if guess == num:
                print(f"CONGRAS!! You guessed it right in {trails} no. of trails!!")
                break

            elif guess < num:
                print("THE GUESSED NUMBER IS LESS!! ENTER BIGGER NUMBER ".capitalize())
                trails += 1

            elif guess > num:
                print("THE GUESSED NUMBER IS HIGH!! GUESS SMALLER NUMBER ".capitalize())
                trails += 1
        else:
            print("ENTER NUMBER WITHIN LIMITS".capitalize())

    return trails


print("\t\t\t\t\t\t\t\t\t\tWELCOME TO GUESS THE NUMBER GAME\n")
print("RULES ARE SIMPLE:\n1.CHOOSE RANGE i.e LOWER AND UPPER LIMIT"
      "\n2.YOU WILL HAVE 5 ATTEMPTS ONLY".capitalize())

try:
    a = int(input("Enter the lower limit:"))
    b = int(input("Enter the upper limit:"))
    print("It's Player 1 Turn :)")
    num1 = random.randint(a, b)
    Player1_count = Guess_game(a, b, num1)
    print("Now,It's Player 2 Turn :)")
    num2 = random.randint(a, b)
    Player2_count = Guess_game(a, b, num2)

    print(f"No.of Trails took by Player 1 are {Player1_count}\n"
          f"No.of Trails took by Player 2 are {Player2_count} ")

    if Player1_count < Player2_count:
        print("PLAYER 1 WINs")
    elif Player2_count < Player1_count:
        print("PLAYER 2 WINs ")
    else:
        print("IT's A TIE !!!")

except ValueError:
    print("PLEASE ENTER VALID INPUT i.e INTEGER")
