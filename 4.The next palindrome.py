# Problem Statement

no_of_testcases = int(input("Enter number of Testcases:"))


def is_palindrome(a):
    a = int(a) + 1
    while True:
        if str(a) == str(a)[::-1]:
            print(f"Next Palindrome is {a}")
            break
        else:
            a = int(a) + 1


for i in range(no_of_testcases):
    n = input("Enter the number:")
    is_palindrome(n)
