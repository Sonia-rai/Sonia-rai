# Problem Statement

import time


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


# def Repeat(z):
#     rp = input("Do You wanna repeat the Directions/Instructions again?(y/n)")
#     if rp == 'n' or rp == 'N':
#         exit()
#     elif rp == 'y' or rp == 'Y':
#         speak(z)
#     else:
#         speak("Invalid Input")


a = "Enter the number of apples"
speak(a)
# time.sleep(5)
# Repeat(a)
no = int(input())
b = "Enter the lower bound"
speak(b)
# time.sleep(5)
# Repeat(b)
mn = int(input())
# minimum number of possible students
c = "Enter the upper bound"
speak(c)
# time.sleep(5)
# Repeat(c)
mx = int(input())
# maximum number of possible students
try:
    if mn == mx:
        d = "Range is not defined"
        speak(d)
        # Repeat(d)
    if mn > mx:
        e = ("This cannot be the range as lower bound "
             "cannot greater than upper bound")
        speak(e)
        # Repeat(e)
        exit()

    for i in range(mn, mx + 1):

        if no % i == 0:
            print(f"{i} is divisor of {no}")
            speak(f"{i} is divisor of {no},\n\n Hence {no} apples can be divided between {i} children" )
        else:
            print(f"{i} is not divisor of {no}")
            speak(f"{i} is not divisor of {no},\n\nTherefore apples cannot be divided among {no} children")

except ValueError:
    f = "PLease Enter Integers only!!"
    speak(f)
    # time.sleep(5)
    # Repeat(f)
