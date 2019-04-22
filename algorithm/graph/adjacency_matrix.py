#!/usr/bin/env python
#coding: utf-8
"""
Other common way of implementing graphs is adjacency matrix.
Each node in graph has one row with every node in graph in one position, the value indicate whether that node is a neighbor.

A graph G = (V, E), V is node, E is edge(or arc in directed graph) between node.

0 represent theta
O represent oh
"""
a, b, c, d, e, f, g, h = range(8)

# undirected graph
# neighbor check: N[a][b]
# degree: sum(N[f])
# if self-loop not allowed, the diagonal is all false
#     a b c d e f g h
N = [[0,1,1,1,1,1,0,0], # a
     [0,0,1,0,1,0,0,0], # b
     [0,0,0,1,0,0,0,0], # c
     [0,0,0,0,1,0,0,0], # d
     [0,0,0,0,0,1,0,0], # e
     [0,0,1,0,0,0,1,1], # f
     [0,0,0,0,0,1,0,1], # g
     [0,0,0,0,0,1,1,0]  # h
    ]


# weighted undirected graph
# neighbor check: W[a][n] < inf
# degree: sum(1 for w in W[a] if w < inf) - 1
_ = float('inf') # represent infinity among floats, ie. nonexistent edge
# 0 represent the distance the itself
#     a b c d e f g h
W = [[0,2,1,3,9,4,_,_], # a
     [_,0,4,_,3,_,_,_], # b
     [_,_,0,8,_,_,_,_], # c
     [_,_,_,0,7,_,_,_], # d
     [_,_,_,_,0,5,_,_], # e
     [_,_,2,_,_,0,2,2], # f
     [_,_,_,_,_,1,0,6], # g
     [_,_,_,_,_,9,8,0]  # h
     ]
