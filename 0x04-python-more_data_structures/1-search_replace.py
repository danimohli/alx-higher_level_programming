#!/usr/bin/python3

# search and replace element in list
# if element available in list
def search_replace(my_list, search, replace):

    newlist = my_list[:]

    for n in range(len(my_list)):
        if newlist[n] == search:
            newlist[n] = replace

    return newlist
