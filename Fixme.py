#!/usr/bin/python3


def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    evenslist = range(n+1)
    evenslist = filter(lambda x: x % 2 == 0, evenslist)
    return list(evenslist)
