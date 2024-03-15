#!/usr/bin/python3

import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":

    if len(sys.argv) != 4:
        print("Usage:", sys.argv[0], "<a> <operator> <b>")
        exit(1)

    a, sign, b = int(sys.argv[1]), sys.argv[2], int(sys.argv[3])
    sign_u = {'+': add, '-': sub, '*': mul, '/': div}

    if sign not in sign_u:
        print("Unknown operator. Only: +, -, * and / available")
        exit(1)
    print('{:d} {} {:d} = {:d}'.format(a, sign, b, sign_u[sign](a, b)))
