#!/usr/bin/env python
#coding: utf-8

# compare position i,i+1, swap if necessary, every iteration determine a number's position
# n: total number
# O(N*N)

def bubble(src):
    length = len(src)
    loop_count = 0
    print "length : ", length
    for i in range(1, length): # n-1 times
        print "i - - ", i
        # numbers to be compared decrease by 1 every iteration, i represent ith times iteration
        for j in range(length - i):
            print j
            if src[j] > src[j+1]:
                src[j], src[j+1] = src[j+1], src[j]
            loop_count += 1
    print "bubble loop : ", loop_count
    return src

def bubble1(src):
    """loop as few as possible
    e.g. if last time no swapped items, order is done
    """
    length = len(src)
    loop_count = 0

    while True:
        swapped = False
        for i in range(1, length-1):
            if src[i] > src[i+1]:
                src[i], src[i+1] = src[i+1], src[i]
                swapped = True
            loop_count += 1
        if not swapped:
            break
        length -= 1

    print "bubble1 loop : ", loop_count
    return src


if __name__ == "__main__":
    src = [3,44,38,5,47,15,36]
    print bubble(src)
    print bubble1(src)
