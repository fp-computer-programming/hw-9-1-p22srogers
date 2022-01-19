# Author: SMR (AMDG) 1/18/22
def find_where(lst,x):
    for index, value in enumerate(lst):
        if value == x:
            index = index
        else:
            index = -1
            break
    return index
print(find_where([1,5,6,53,6,14,5,34,4],5))