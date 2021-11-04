# Problem Statement
import random


def Jumbled_name(lst):
    fname_lname = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
    for fname, lname in fname_lname.items():
        rand_key = random.choice(list(fname_lname.keys()))
        temp_name = lname
        # swapping the names and surnames
        fname_lname[fname] = fname_lname[rand_key]
        fname_lname[rand_key] = temp_name
    print("Possible combination")
    for k, v in fname_lname.items():
        print(f"{k} {v}")


if __name__ == '__main__':
    num = int(input("Enter the no.of the friend:"))
    print("Enter the names of your Friends:")
    names = [input() for i in range(num)]

    lst = [y for x in names for y in x.split(' ', 1)]
    Jumbled_name(lst)
