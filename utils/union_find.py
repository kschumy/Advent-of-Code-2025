class UnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.num_of_elements = n

    def find(self, val:int) -> int:
        if self.parents[val] != val:
            self.parents[val] = self.find(self.parents[val])
        return self.parents[val]

    def union(self, val_1: int, val_2: int) -> None:
        root_1 = self.find(val_1)
        root_2 = self.find(val_2)
        if root_1 != root_2:
            self.parents[root_2] = root_1
            self.num_of_elements -= 1

    def is_unified(self) -> bool:
        return self.num_of_elements == 1