#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    lenn = len(my_list) - 1
    for number in my_list:
        print("{:d}".format(my_list[lenn]))
        lenn -= 1
