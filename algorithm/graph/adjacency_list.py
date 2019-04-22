#!/usr/bin/env python
#coding: utf-8
"""
One of the most intuitive ways of implementing graphs is using adjacency lists.
For each node, we can access a list (or set or other container or iterable) of its neighbors.

A graph G = (V, E), V is node, E is edge(or arc in directed graph) between node.
N(v) represent the neighbors of node v.

0 represent theta
O represent oh
"""
a, b, c, d, e, f, g, h = range(8)

# directed graph
# neighbor check is: c in N[a]
# degree: len(N[a])

N = [
    {b, c, d, e, f},   # a's neighbors, membership checking(c in N[a]) is 0(1)
                       #    it is constant(dict,set is implemented using 'hash tables')
    {c, e},            # b's
    {d},               # c
    {e},               # d
    {f},               # e
    [c, g, h],         # f, list or set doesn't matter, order is arbitrary
                       #    but membership checking(c in N[f]) is 0(n)
    {f, h},            # g
    {f, g}             # h
    ]

# weighted directed graph
# key is node, value is edge weight
# edge weith: N[a][b]
WN = [
    {b:2, c:1, d:3, e:9, f:4}, #a
    {c:4, e:3},                #b
    {d:8},                     #c
    {e:7},                     #d
    {f:5},                     #e
    {c:2, g:2, h:2},           #f
    {f:1, h:6},                #g
    {f:9, g:8}                 #h
    ]

# if you want node labels, could use dict
NN = {
      'a': set('bcdef'),
      'b': set('ce'),
      'c': set('d'),
      'd': set('e'),
      'e': set('f'),
      'f': set('cgh'),
      'g': set('fh'),
      'h': set('fg')
      }
