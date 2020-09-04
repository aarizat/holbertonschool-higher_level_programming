#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    print(*list(filter(lambda n: n[:2] != "__", dir(hidden_4))), sep="\n")
