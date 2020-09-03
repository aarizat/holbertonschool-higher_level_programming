#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("{} arguments".format(argc - 1))
    else:
        print("{} arguments".format(argc - 1))
        for idx, arg in enumerate(sys.argv[1:]):
            print("{}: {}".format(idx+1, arg))
