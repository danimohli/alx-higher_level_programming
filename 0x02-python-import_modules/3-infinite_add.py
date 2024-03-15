#!/usr/bin/python3
import sys

if __name__ == "__main__":
    t_len = len(sys.argv) - 1

    n = 0

    for x in range(t_len):
        n += int(sys.argv[x + 1])
    print("{:d}".format(n))
