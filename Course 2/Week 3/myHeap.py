import os
import heapq
from week3_quicksort import QuickSort


class Min_Heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) / 2

    def insertKey(self, k):
        # heapq.heappush(self.heap, k)

        self.heap.append(k)
        i = len(self.heap) - 1

        # insert and end and keep bubbling up
        while i != 0:
            if self.heap[i] < self.heap[self.parent(i)]:
                self.heap[i], self.heap[self.parent(
                    i)] = self.heap[self.parent(i)], self.heap[i]

            i = self.parent(i)

    def extractMin(self):
        # return heapq.heappop(self.heap)
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]

        # balance the tree
        i = 0
        # insert and end and keep bubbling up
        while i < len(self.heap):
            # print i, 2 * i + 1, 2 * i + 2
            left = 2 * i + 1
            right = 2 * i + 2
            # largest = self.heap[i]
            smallest = i

            if left < len(self.heap):
                if self.heap[smallest] >= self.heap[left]:
                    smallest = left

            if right < len(self.heap):
                if self.heap[smallest] >= self.heap[right]:
                    smallest = right

            # now swap smallest and parent
            if smallest != i:
                self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            # print "smallest child =", smallest
            i = i + 1

        return min_val

        vals = [v[1] for v in self.heap]
        # print self.heap, vals.index(vertex)
        return vals.index(vertex)

    def getMin(self):
        return self.heap[0]

    def __str__(self):
        return str(self.heap)

    def __repr__(self):
        print str(self.heap)

    def __len__(self):
        return len(self.heap)


class Max_Heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) / 2

    def insertKey(self, k):
        # heapq.heappush(self.heap, k)

        self.heap.append(k)
        i = len(self.heap) - 1

        # insert and end and keep bubbling up
        while i != 0:
            if self.heap[i] > self.heap[self.parent(i)]:
                self.heap[i], self.heap[self.parent(
                    i)] = self.heap[self.parent(i)], self.heap[i]

            i = self.parent(i)

    def extractMax(self):
        # return heapq.heappop(self.heap)
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        del self.heap[-1]

        # balance the tree
        i = 0
        # insert and end and keep bubbling up
        while i < len(self.heap):
            # print i, 2 * i + 1, 2 * i + 2
            left = 2 * i + 1
            right = 2 * i + 2
            # largest = self.heap[i]
            largest = i

            if left < len(self.heap):
                if self.heap[largest] <= self.heap[left]:
                    largest = left

            if right < len(self.heap):
                if self.heap[largest] < self.heap[right]:
                    largest = right

            # now swap largest and parent
            if largest != i:
                self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            # print "largest child =", largest
            i = i + 1

        return min_val

    def getMax(self):
        return self.heap[0]

    def __str__(self):
        return str(self.heap)

    def __repr__(self):
        print str(self.heap)

    def __len__(self):
        return len(self.heap)


if __name__ == '__main__':
    heapObj = Min_Heap()
    heapObj.insertKey(1)
    heapObj.insertKey(2)
    heapObj.insertKey(3)
    heapObj.insertKey(4)
    print heapObj.extractMax()
    # heapObj.insertKey(7)
    # heapObj.insertKey(8)
    # heapObj.insertKey(6)
    # heapObj.insertKey(1)
    # heapObj.insertKey((3, 1))
    # heapObj.insertKey((2, 2))
    # heapObj.insertKey((15, 3))
    # heapObj.insertKey((5, 4))
    # # decrease value of the ith element in the heap
    # heapObj.decreaseKey(3, (1, 4))
    # print heapObj.heap
    # print heapObj.heap
    # heapObj.extractMin()
    # print heapObj.heap
    # # delete the ith element from the heap
    # heapObj.deleteKey(1)

    maxheap = Max_Heap()
    maxheap.insertKey(5)
    maxheap.insertKey(6)
    maxheap.insertKey(7)
    # maxheap.insertKey(2)
    # maxheap.insertKey(7)
    maxheap.insertKey(8)
    print maxheap.heap
    # print maxheap.extractMax()
    # print maxheap.heap
