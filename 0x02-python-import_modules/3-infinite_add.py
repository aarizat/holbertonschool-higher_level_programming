#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print(0)
    else:
        print(sum(list(map(lambda x: int(x), sys.argv[1:]))))
