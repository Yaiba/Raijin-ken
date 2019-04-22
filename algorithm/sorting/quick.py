#!/usr/bin/env python
# worst O(N*N)
# avg O(N*log(N)) import time

def quick1(target, left, right):
    if left > right:
        return

    # to determin in which the "flag" supposed to be, (eg, [small_numbers, flag, big_numbers])
    flag = target[left]
    i, j = left, right
    while(i!=j):
        # left side as the mark to compare, so move right side first to keep
        # number that i (left)point to always smaller than the flag number.
        # take [6,1,2,7,7,10,8], if move left first, after first 'swap' is [7,1,2,6,7,10,8], which is wrong
        while(target[j] >= flag and i < j):
            j -= 1
        while(target[i] <= flag and i < j):
            i += 1
        if i < j:
            target[i] , target[j] = target[j], target[i]

    # when i=j, means two sentry meet, then the slot they meet is the slot where "flag" should be  
    target[left], target[i] = target[i], target[left]

    print target
    quick1(target, left, i-1)
    quick1(target, i+1, right)

def quick2(target):
    """which is space inefficient, but easy to understand"""
    if len(target) <= 1:
        return target
    else:
        pivot = target[0]
        big_numbers = [x for x in target[1:] if x > pivot]
        small_numbers = [x for x in target[1:] if x <= pivot]
        return quick2(small_numbers) + [pivot] + quick2(big_numbers)

def main():
    target = [7,3,0,6,3,8,4,1,9,7,12,6]
    target = [6,1,2,7,7,10,8]
    print target, "- >"
    quick1(target, 0, len(target)-1)
    print "quick1    : ", target
    print "quick2    : ", quick2(target)

if __name__ == "__main__":
    main()
