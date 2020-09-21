#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    elements = 0
    for idx in range(x):
        try:
            print("{}".format(my_list[idx]), end="")
            elements += 1
        except:
            pass
    print("")
    return elements
