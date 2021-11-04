# Problem Statement

lst = []
size = int(input("Enter the no. of item :"))
print("Enter calories of food item one by one :")
for i in range(size):
    element = int(input())
    lst.append(element)
print(f"The List that you entered is {lst}")
# First Method
lst2 = []
for i in range(len(lst) - 1, -1, -1):
    lst2.append((lst[i]))
# Alternate First method
# reverse1 = lst[:]
# reverse1.reverse()

# Second Method
reverse2 = lst[::-1]
# Third Method
reverse3 = lst[:]
for i in range(len(reverse3) // 2):
    reverse3[i], reverse3[len(reverse3) - i - 1] = reverse3[len(reverse3) - i - 1], reverse3[i]

if lst2 == reverse2 and reverse2 == reverse3:
    print(f"All the methods give same result i.e. {reverse3}\n")
