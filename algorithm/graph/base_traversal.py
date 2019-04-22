#coding:utf-8
"""
get all connected subgraph(components), undirected graph
O(E+V)   every edge and node has to be explored
"""

def walk(G, s, zone=set()):             # S -> forbidden zone
    vsted, to_vst = dict(), set()
    vsted[s] = None
    to_vst.add(s)
    while to_vst:
        u = to_vst.pop()
        for v in G[u].difference(vsted, zone):
            vsted[v] = u                # v comes from u
            to_vst.add(v)
    return vsted

def all_components(G):
    seen = set()
    all_comp = []
    for u in G:
        if u in seen: continue
        sub = walk(G, u)
        seen.update(sub)
        all_comp.append(sub)
    return all_comp


if __name__ == "__main__":
    G = {'a': set('bc'),   # abc
         'b': set('ac'),
         'c': set('ab'),
         'd': set('e'),    # de
         'e': set('d'),
         'f': set('gh'),   # fghi
         'g': set('fi'),
         'h': set('fi'),
         'i': set('gh')}

    print all_components(G)
