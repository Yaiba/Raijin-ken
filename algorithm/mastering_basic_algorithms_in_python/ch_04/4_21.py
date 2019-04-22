#coding: utf-8
"""
4-21.
An interval can be represented, for example, as a pair of numbers,
such as (3.2, 4.9). Let’s say you have a list of such intervals (where no
intervals are identical), and you want know which intervals that fall inside
other intervals. An interval (u,v) falls inside (x,y) when x<=u and v<=y.
How would you do this efficiently?
-------
A simple inductive solution would be to remove one interval, solving the
problem for the rest, and then checking whether the initial interval should be
added back. The problem is that you’d have to check this interval against all
the others, giving a quadratic running time overall. You can improve this
running time, however. First, sort the intervals by their left endpoints, and
use the induction hypothesis that you can solve the problem for the n–1 first
intervals. Now, extend the hypothesis: Assume that you can also find the largest
right endpoint among the n–1 intervals. Do you see how the inductive step can
now be performed in constant time?
"""

from operator import itemgetter


def naive_check(seq):
    for a in seq:
        print a, ">>",
        for b in seq:
            if a == b: continue
            if a[0] >= b[0] and a[1] <= b[1]:
                print b,
        print

def check(seq):
    seq = sorted(seq, key=itemgetter(0))     # sort by left endpoint

if __name__ == "__main__":
    intervals = [(2,4), (1,4), (6,8), (2, 3), (0,4), (5, 10), (3, 7)]
    naive_check(intervals)
