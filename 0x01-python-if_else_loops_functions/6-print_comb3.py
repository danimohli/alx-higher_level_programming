#!/usr/bin/python3

for a in range(9):
    for b in range(10):
        if a < b:
            print("{}{},".format(a, b), end=' ')
print("{}{}".format(a, b))
