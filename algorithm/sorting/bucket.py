#!/usr/bin/env python
#coding: utf-8
#
# m: bigest number
# n: actual number
# O(m+n+m+n) -> O(2(m+n)) -> O(M+N)

## space inefficient

from random import randint

def bucket_special_case(seq, max_val):
    """
    special: M = MAX_VAL   (ie. every bucket has one elem)
    """
    length = len(seq)
    # bucket num is base on max_val in the seq
    buckets = [0] * (max_val+1)
    for n in seq:               #O(N)
        buckets[n] += 1

    # output dynamic
    #return [i for i, v in enumerate(buckets) if v > 0  for x in range(v)] # m+n

    # output to fixed len(seq)
    res = [0] * length
    cur_index = 0
    for i in xrange(max_val):       # check every posible elem ,  O(M)
        k = cur_index
        while k < cur_index + buckets[i]:  # elem is presented(maybe repeated)
            res[k] = i
            k += 1
        cur_index = k
    return res


def bucket_sort(seq, max_val):
    ''' for max_val is too big
    divide into M buckets, apply sort to every bucket, then merge
    the more bucket the more time efficient, but more space comsumed

    O(N)+O(M)O(N/Mlog(N/M)) = O(N+ Nlog(N/M)) = O(N + NlogN - NlogM)
    '''
    M = max_val / 100
    length = len(seq)

    buckets = [[] for _ in range(M+1)]
    # or bucket = defaultdict(list)

    for elem in seq:                   # O(N)
        buckets[elem/100].append(elem)

    res = []

    for bucket in buckets:             # O(M) * O(N/M*log(N/M))
        # apply sort on every bucket
        res.extend(sorted(bucket))     # quick sort,  O(N/M*log(N/M))

    return res


if __name__ == "__main__":
    N = 10
    MAX = 1000
    sp = [randint(0, MAX) for x in range(N)]
    print "before:\n", sp
    #print "after:\n", bucket_special_case(sp, MAX)
    print "after:\n", bucket_sort(sp, MAX)
