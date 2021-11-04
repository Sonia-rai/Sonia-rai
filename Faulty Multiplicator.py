# Problem Statement

import random


def rohan_multiplication(number):
    wrong = random.randint(1, 9)  # Generates an random number stored in var wrong
    # List comprehension
    table = [i * number for i in range(1, 11)]
    # table[wrong] actually locate index at which value will be changed
    table[wrong] = table[wrong] + random.randrange(1, 10)
    return table


def isCorrect(table, number):
    for i in range(1, 11):
        if table[i - 1] != i * number:
            return i - 1
    return None


if __name__ == '__main__':
    number = int(input("Enter a number whose table you wanna see:"))
    myTable = rohan_multiplication(number)
    print(myTable)
    isWrong = isCorrect(myTable, number)
    print("Be Aware!!")
    print(f"The wrong number is present at {isWrong} index")
