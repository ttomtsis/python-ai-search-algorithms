class MyNode:

    def __init__(self, n, u, d, l, r, wu, wd, wl, wr):
        self.name = str(n)
        self.up = bool(u)
        self.down = bool(d)
        self.left = bool(l)
        self.right = bool(r)
        self.weight_up = bool(wu)
        self.weight_down = bool(wd)
        self.weight_left - bool(wl)
        self.weight_right = bool(wr)
        print("Node " + n + " Created")
