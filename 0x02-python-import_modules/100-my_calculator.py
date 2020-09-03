#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a, b = int(sys.argv[1]), int(sys.argv[3])
    ops = {"+": add(a, b), "-": sub(a, b), "*": mul(a, b), "/": div(a, b)}
    print("{} {} {} = {}".
          format(sys.argv[1], sys.argv[2], sys.argv[3], ops[sys.argv[2]]))
