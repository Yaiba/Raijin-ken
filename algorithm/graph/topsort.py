#coding:utf-8
"""
DAG
if node A points to B, (ie. A depends on B),
A could be placed anywhere in the order as long as A is before B
"""

from random import shuffle, randint

from graph_generator import dag

def naive_topsort(G, S=None):
    """
    T(n) = T(n-1) + n,  O(n*n)

    remove a (random)node from graph
    insert it after all nodes depend on it

    NOTE:
         this is wrong
    order  [5, 2, 4, 3, 6, 8, 9, 7, 1, 0]
    G = {0: {}, 1: {0: 10}, 2: {0: 3, 3: 5, 4: 8}, 3: {0: 7, 6: 2}, 4: {8: 1, 3: 7}, 5: {0: 3, 9: 5, 2: 8}, 6: {8: 2}, 7: {1: 8}, 8: {9: 10, 1: 3}, 9: {1: 8, 7: 3}}
    [8, 9]
    [8, 9, 7]
    [6, 8, 9, 7]
    [5, 6, 8, 9, 7]
    [4, 5, 6, 8, 9, 7]                    # 5 is indirectly depends on 4, but could not be determined by now
    [4, 3, 5, 6, 8, 9, 7]
    [4, 3, 5, 2, 6, 8, 9, 7]
    [4, 3, 5, 2, 6, 8, 9, 7, 1]
    [4, 3, 5, 2, 6, 8, 9, 7, 1, 0]
    sorted [4, 3, 5, 2, 6, 8, 9, 7, 1, 0]
    """
    if S is None: S = set(G)
    if len(S) == 1: return list(S)
    v = S.pop()                    # reduction: remove a (random)node
    res = naive_topsort(G, S)      # recursion(assumption: n-1 is done)
    pos = 0
    for i, u in enumerate(res):    # find right pos, it is linear
        if v in G[u]: pos = i+1
    res.insert(pos, v)             # place V after all nodes depend on V
    return res

def topsort(G):
    """
    T(n) = T(n-1) + 1, O(n)

    remove a node from graph(ensure the rest is still a DAG)

    the node has no in-edges is safe to remove(also safe place it first)
    then remove all its out-edges, the remaining graph is still DAG
    """
    count = dict((u, 0) for u in G)
    for u in G:
        for v in G[u]:
            count[v] += 1
    nodes_to_remove  = [u for u in G if count[u] == 0]
    res = []
    while nodes_to_remove:
        u = nodes_to_remove.pop()
        res.append(u)
        for v in G[u]:
            count[v] -= 1
            if count[v] == 0:
                nodes_to_remove.append(v)
    return res


if __name__ == "__main__":
    nodes = range(10)
    shuffle(nodes)
    print "before:\n", nodes
    dag = dag(nodes)
    print dag
    print "after:\n", topsort(dag)
    assert nodes == topsort(dag)
    #assert nodes == naive_topsort(dag)
