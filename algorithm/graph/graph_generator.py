#coding: utf-8

from random import randint

def dag(orders, max_out=3, max_distant=10):
    """directed acyclic graph"""
    length = len(orders)
    G = {orders[length-1]: {}}                                 # last node has no dependencies
    for i in range(length - 1):
        G[orders[i]] = {orders[i+1]: randint(1, max_distant)}  # ensure order
        for _ in range(randint(0, max_out-1)):                 # random extra trivial edges
            to = randint(i+1, length-1)
            G[orders[i]].update({orders[to]: randint(1, max_distant)})
    return G
