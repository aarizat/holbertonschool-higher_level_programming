#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        elements = 0
        for idx in range(x):
            print("{}".format(my_list[idx]), end="")
            elements += 1
        print("")
        return elements
    except:
        print("")
        return elements
