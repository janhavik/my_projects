import os
import heapq


class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) / 2

    def insertKey(self, k):
        heapq.heappush(self.heap, k)

    def extractMin(self):
        if self.heap:
            return heapq.heappop(self.heap)

    def getMin(self):
        return self.heap[0]

    def decreaseKey(self, i, val):

        # print i, self.heap
        self.heap[i] = val  # inserted new value in heap

        # now maintain heap property
        # swap parent with i everytime till heap stabilizes
        while i != 0 and self.heap[self.parent(i)][0] > self.heap[i][0]:
            # print i
            # print self.heap
            self.heap[self.parent(i)], self.heap[i] = \
                self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)

    def deleteKey(self, i):
        # make it the smallest and extract it
        val = self.heap[i]
        self.decreaseKey(i, (float('-inf'), val[1]))
        self.extractMin()

    def find_index(self, vertex):

        vals = [v[1] for v in self.heap]
        # print self.heap, vals.index(vertex)
        return vals.index(vertex)

    def __str__(self):
        return str(self.heap)

    def __repr__(self):
        print str(self.heap)

    def __len__(self):
        return len(self.heap)

    def isInHeap(self, vertex):
        return True if vertex in [v[1] for v in self.heap] else False


if __name__ == '__main__':
    heapObj = Heap()
    heapObj.insertKey((3, 1))
    heapObj.insertKey((2, 2))
    heapObj.insertKey((15, 3))
    heapObj.insertKey((5, 4))
    # decrease value of the ith element in the heap
    heapObj.decreaseKey(3, (1, 4))
    print heapObj.heap
    print heapObj.getMin()
    # delete the ith element from the heap
    heapObj.deleteKey(1)
    print heapObj.heap
