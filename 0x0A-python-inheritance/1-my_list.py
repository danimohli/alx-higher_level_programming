#!/usr/bin/python3

""" print sorted list element"""


class Mylist(list):

    """ class inheritance """

    def print_sorted(self):

        """ print sorted list  """

        print(sorted(self))
