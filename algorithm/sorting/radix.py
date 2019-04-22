#coding: utf-8
'''
O(dn)
d: digit size
n: element size
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


key_maker = lambda digit_place, radix: (lambda x: (x / digit_place) % radix)

def radix_sort(target, digit_max, RADIX=10):
    digit_place = 1
    for _ in range(digit_max):
        target = counting_general(target, key_maker(digit_place, RADIX))
        digit_place *= RADIX
    return target


if __name__ == "__main__":
    sp = [randint(0,1000) for x in range(10)]
    print "before:\n", sp
    print "after:\n", radix_sort(sp, 5)
