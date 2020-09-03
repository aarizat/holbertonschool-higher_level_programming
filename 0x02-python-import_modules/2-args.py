#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    if argc == 1:
        print("{} arguments".format(argc - 1))
    else:
        msg = "argument" if argc == 2 else "arguments"
        print("{} {}".format(argc - 1, msg))
        for idx, arg in enumerate(sys.argv[1:]):
            print("{}: {}".format(idx+1, arg))
