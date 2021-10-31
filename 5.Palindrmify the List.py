# Problem Statement

import Thenextpalindrome

lst = []
size = int(input("Enter the size of List:"))
for element in range(size):
    no = int(input("Enter elements of List one by one:"))
    lst.append(no)
print(f"The List That you Entered is {lst} ")
lst2 = []

'''print(f'Your Required List{[lst[i] if lst[i] < 10 
 else Thenextpalindrome.is_palindrome(lst[i]) for i in range(size)]}  ')'''

for element in lst:
    if element > 10:
        n = Thenextpalindrome.is_palindrome(element)
        lst2.append(n)
    else:
        lst2.append(element)
print(f'Your Required List {lst2} ')
