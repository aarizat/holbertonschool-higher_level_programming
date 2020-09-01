#!/usr/bin/python3
def uppercase(str):
    for ch in str:
        print("{}".format(chr(ord(ch) - 32) if ord(ch) in range(97, 123)
                          else ch), end='')
    print("")
