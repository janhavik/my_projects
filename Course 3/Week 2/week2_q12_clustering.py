import os
import pprint
from UnionFind import UnionFind
from copy import deepcopy
import traceback
import time


def readGraph(filename):

    edges = []
    with open(filename) as fp:
        lines = fp.readlines()
        num_nodes, dist_bits = int(lines[0].split(
            " ")[0]), int(lines[0].split(" ")[1])
        for everyline in lines[1:]:
            a = everyline.strip().replace(" ", "")
            edges.append(a)

    return (num_nodes, dist_bits, edges)


def create_Graph_HashTable(edges):

    e = {}
    for i in range(0, len(edges)):
        everyedge = edges[i]
        if everyedge in e:
            e[everyedge].append(i)
        else:
            e[everyedge] = [i]

    return e


def hamming(s1, s2):
    assert len(s1) == len(s2)
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def create_hamming_1(root):
    num_bits = len(root)

    hd1 = []
    for i in range(0, num_bits):
        p_1 = format(int(root, 2) ^ 2**i, "0%sb" % num_bits)
        if hamming(root, p_1) == 1:
            hd1.append(p_1)

    return hd1


def create_hamming_2(root):
    num_bits = len(root)

    starting_nums_hd2 = [2**i + 1 for i in range(1, num_bits)]
    masks = [i << j for i in starting_nums_hd2 for j in range(
        num_bits) if (i << j) < (2**num_bits)]
    hd2 = [format(int(root, 2) ^ everymask, "0%sb" % num_bits)
           for everymask in masks]

    return hd2


def k_means_cluster(edges, num_nodes, dist_bits):

    # print pprint.pformat(edges)
    U = UnionFind(num_nodes)
    cluster_count = num_nodes
    # cluster with hamming distance 0
    for everyedge in edges:
        hamming_0 = [everyedge]
        for e in hamming_0:
            try:
                for p in edges[everyedge]:
                    for q in edges[e]:
                        if U.root(p) != U.root(q):
                            U.union(p, q)
                            cluster_count = cluster_count - 1
            except:
                continue

        print "Hamming 0 done"
        hamming_1 = create_hamming_1(everyedge)
        for e in hamming_1:
            try:
                for p in edges[everyedge]:
                    for q in edges[e]:
                        # print p, q
                        if U.root(p) != U.root(q):
                            U.union(p, q)
                            cluster_count = cluster_count - 1
            except:
                continue
        print "Hamming 1 done"

        hamming_2 = create_hamming_2(everyedge)
        for e in hamming_2:
            try:
                for p in edges[everyedge]:
                    for q in edges[e]:
                        # print p, q
                        if U.root(p) != U.root(q):
                            U.union(p, q)
                            cluster_count = cluster_count - 1
            except:
                continue
        print "Hamming 2 done"

    return cluster_count


filename = "clustering2.txt"
# filename = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course3\\assignment2Clustering\\question2\\input_random_36_128_12.txt"
num_nodes, dist_bits, edges = readGraph(filename)
print "Done reading"
edges = create_Graph_HashTable(edges)
print "Created graph dict"
print k_means_cluster(edges, num_nodes, dist_bits)

# pathdir = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course3\\assignment2Clustering\\question2"

# resultdir = open("Q2Results.txt", "w")

# for everyele in os.listdir(pathdir):
#     if "input" in everyele:

#         with open(os.path.join(pathdir, everyele.replace("input", "output"))) as fp:
#             lines = fp.readlines()
#             result_required_diff = int(lines[0].strip())

#         t = time.time()
#         num_nodes, dist_bits, edges = readGraph(
#             os.path.join(pathdir, everyele))
#         edges = create_Graph_HashTable(edges)
#         res = k_means_cluster(edges, num_nodes, dist_bits)
#         print everyele, res == result_required_diff, time.time() - t

#         resultdir.write("Result_Spacing=%s, Filename=%s, Required_Spacing=%s, Obtained_Spacing=%s\n" %
#                         (result_required_diff == res, everyele, result_required_diff, res))

# resultdir.write("\n")
