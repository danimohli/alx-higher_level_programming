#!/usr/bin/python3


if __name__ == "__main__":

    import sys

    t_len = len(sys.argv) - 1
    if t_len == 0:
        print("0 arguments.")
    elif t_len == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(t_len))
    for x in range(t_len):
        print("{}: {}".format(x + 1, sys.argv[x + 1]))
