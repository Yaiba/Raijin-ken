#!/usr/bin/python
'''
The insertion sort

assume first n-1 elements are already sorted, the insert n in the right place.
'''

from random import randint

def ins_sort_rec(seq, outc):
    if outc == 0: return                          # Base case -- do nothing
    ins_sort_rec(seq, outc-1)
    inc = outc
    while inc > 0 and seq[inc-1] > seq[inc]:      # sort first outc elements
        seq[inc-1], seq[inc] = seq[inc], seq[inc-1]
        inc -= 1


def insertionSort(seq):
    length = len(seq)
    for outc in xrange(1, length):
        inc = outc
        while inc > 0 and seq[inc-1] > seq[inc]:
            seq[inc-1], seq[inc] = seq[inc], seq[inc-1]
            inc -= 1

if __name__ == '__main__':
    sp = [randint(0,1000) for x in range(10)]

    print "before:\n", sp
    ins_sort_rec(sp, len(sp)-1)
    #insertionSort(sp)
    print "after:\n", sp
