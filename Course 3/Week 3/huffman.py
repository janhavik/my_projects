import os
import pprint
from myHeap import Min_Heap

codes = {}


def readWeights(filename):

    weights = []
    with open(filename) as fp:
        lines = fp.readlines()
        num_weights = int(lines[0])
        for i in range(len(lines[1:])):
            weights.append([int(lines[i + 1]), [i + 1, ""]])

    return (num_weights, weights)


def Huffman(num_weights, weights):

    Q = Min_Heap()
    for everyweight in weights:
        Q.insertKey(everyweight)

    while len(Q) >= 2:
        left = Q.extractMin()
        right = Q.extractMin()

        parent_node_weight = [left[0] + right[0]]

        left = [left[0]] + [[i[0], "0" + i[1]] for i in left[1:]]
        right = [right[0]] + [[i[0], "1" + i[1]] for i in right[1:]]
        parent_node = left[1:] + right[1:]
        Q.insertKey(parent_node_weight + parent_node)

    codes_raw = Q.extractMin()[1:]
    codes = {i[0]: i[1] for i in codes_raw}
    lens = [len(i[1]) for i in codes_raw]
    return (min(lens), max(lens), codes)


# filename = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course3\\assignment3HuffmanAndMWIS\\question1And2\\input_random_17_160.txt"
filename = "huffman.txt"
num_weights, weights = readWeights(filename)
min_len, max_len, codes = Huffman(num_weights, weights)
print max_len, min_len
# 19 9
