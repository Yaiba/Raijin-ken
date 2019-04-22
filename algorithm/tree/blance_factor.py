#coding: utf-8

class BT(object):
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.factor = 0
        self.height = 0

def dfs(T):
    if not T:
        return -1
    lh = dfs(T.left)
    rh = dfs(T.right)
    T.factor = lh - rh
    T.height = max(lh, rh) + 1
    return T.height

T = BT(BT(BT(), BT(BT(BT(), BT()), BT())), BT(BT(BT(), BT()), BT(BT(), BT())))

print dfs(T)
print T.factor
