#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return
    for idx in range(len(my_list)-1):
        if my_list[idx] > my_list[idx+1]:
            my_list[idx], my_list[idx+1] = my_list[idx+1], my_list[idx]
    return my_list[-1]
