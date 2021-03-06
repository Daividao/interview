"""
Using DisjointSet with path compression when 1) knowing in advanced the total number of nodes in the set, and 2) frequently union
subsets or checking connectivity between 2 subsets.
"""


class DisjointSet:
    def __init__(self, size):
        self.size = size
        self.rank = [1] * self.size
        self.parent = list(range(size))

    # Amortized O(1).
    # M operations on N nodes is O(N + Mlog*N) very close to constant time.
    def find(self, ind):
        if self.parent[ind] != ind:
            self.parent[ind] = self.find(self.parent[ind])
        return self.parent[ind]

    # Amortized O(1)
    def union(self, ind1, ind2):
        p1 = self.find(ind1)
        p2 = self.find(ind2)
        if p1 == p2:
            return
        if self.rank[p1] >= self.rank[p2]:
            self.parent[p2] = p1
            if self.rank[p1] == self.rank[p2]:
                self.rank[p1] += 1
        else:
            self.parent[p1] = p2

    # Amortized O(1)
    def is_connected(self, ind1, ind2):
        return self.find(ind1) == self.find(ind2)
