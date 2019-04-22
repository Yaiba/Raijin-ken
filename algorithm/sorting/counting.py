#coding: utf-8
'''
'''

from collections import defaultdict
from random import randint

def counting_general(A, key=lambda x: x):
    B, C = [], defaultdict(list)
    for x in A:
        C[key(x)].append(x)
    for k in range(min(C), max(C)+1):
        B.extend(C[k])
    return B


def counting_classic(seq, max_val):
    counts = [0 for _ in xrange(max_val+1)]

    for elem in seq:
        counts[elem] += 1

    # cal elem's index in new order
    for index in xrange(1, max_val+1):
        counts[index] += counts[index-1]  # counts[index] represent the num of elems that <= index(elem)

    L = [0 for _ in xrange(len(seq))]
    for elem in seq:
        index = counts[elem] - 1        # no elem counts=0
        L[index] = elem
        counts[elem] -= 1

    return L


if __name__ == "__main__":
    MAX = 1000
    sp = [randint(0, MAX) for x in range(10)]
    print "before:\n", sp
    #print "after:\n", counting_general(sp)
    print "after:\n", counting_classic(sp, MAX)
