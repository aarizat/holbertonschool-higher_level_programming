#!/usr/bin/python3
for num in range(100):
    print("{}".format('0' + str(num) if num < 10 else num),
          end=', ' if num != 99 else '\n')
