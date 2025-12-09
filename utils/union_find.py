class UnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))

    def find(self, val:int):
        if self.parents[val] == val:
            return self.parents[val]
        return self.find(self.parents[val])
    
    # return True if merged and False if already in the same group
    def union(self, val_1: int, val_2: int) -> bool:
        root_1 = self.find(val_1)
        root_2 = self.find(val_2)
        if root_1 == root_2:
            return False
        self.parents[root_2] = root_1
        return True











































    # def __init__(self, size: int):
    #     self.parent = list(range(size))
    #     self.rank = [1] * size

    # def find(self, p: int) -> int:
    #     if self.parent[p] != p:
    #         self.parent[p] = self.find(self.parent[p])
    #     return self.parent[p]

    # def union(self, p: int, q: int) -> None:
    #     rootP = self.find(p)
    #     rootQ = self.find(q)
    #     if rootP != rootQ:
    #         if self.rank[rootP] > self.rank[rootQ]:
    #             self.parent[rootQ] = rootP
    #         elif self.rank[rootP] < self.rank[rootQ]:
    #             self.parent[rootP] = rootQ
    #         else:
    #             self.parent[rootQ] = rootP
    #             self.rank[rootP] += 1