#!/usr/bin/python
#coding:utf-8
'''
The selection sort.

find the largest element, place it at position n, then sort the remaining
'''

from random import randint

def sel_sort_rec(seq, i):
    if i==0: return
    _max = i
    for j in range(i):
        if seq[j] > seq[_max]: _max = j
    seq[i], seq[_max] = seq[_max], seq[i]
    sel_sort_rec(seq, i-1)


def selectionSort(l):
    length = len(l)
    for i in range(length-1, 0, -1):
        _max = i
        for j in range(i):
            if seq[j] > seq[_max]: _max = j
        seq[i], seq[_max] = seq[_max], seq[i]


if __name__ == '__main__':
    sp = [randint(0,1000) for x in range(10)]

    print 'before:\n', sp
    sel_sort_rec(sp, len(sp)-1)
    #selectionSort(sp)
    print 'after sort:\n', sp
