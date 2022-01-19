# Author: SMR (AMDG) 01/18/22
even_list = []
def even_item(lst):
    for i, v in enumerate(lst):
        if int(i) % 2 == 0:
            even_list.append(v)
    return ("The even numbered indexes include: {0}".format(even_list))
test_lst = [3,4,5,7,9,14]
print(even_item(test_lst))