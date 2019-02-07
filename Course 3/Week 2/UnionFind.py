import pprint

# path compression enabled union find class


class UnionFind:
    def __init__(self, n):
        self.id = range(n)
        self.size = [1] * n

    def root(self, i):
        # find root of i with path compression technique
        while (i != self.id[i]):
            self.id[i] = self.id[self.id[i]]
            i = self.id[i]

        return i

    def find(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if i == j:
            return
        if self.size[i] < self.size[j]:
            # print "i<j, i, j", i, j
            self.id[i] = j
            self.size[j] = self.size[j] + self.size[i]
        else:
            # print "else condition, i, j", i, j
            self.id[j] = i
            self.size[i] = self.size[i] + self.size[j]

    def __str__(self):
        return "ID=%s\nSIZE=%s" % (self.id, self.size)

    def get_num_clusters(self):
        return len(set(self.id))


if __name__ == "__main__":
    u = UnionFind(10)
    u.union(2, 3)
    u.union(3, 6)
    u.union(6, 9)
    print u.find(2, 9)
    print u
    print len(set(u.id))
