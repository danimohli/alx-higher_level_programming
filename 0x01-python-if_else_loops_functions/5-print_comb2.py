#!/usr/bin/python3

for x in range(0, 100):
    if x < 99:
        print("{}{},".format(x // 10, x % 10), end=' ')

print("{}{}".format(x // 10, x % 10))
