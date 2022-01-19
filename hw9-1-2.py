# Author: SMR (AMDG) 01/18/22
def odd_number(lst):
    for i, v in enumerate(lst):
        if i%2 != 0:
            print(v)
odd_number([4, 5, 24, 40])