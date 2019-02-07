import os
import pprint
from UnionFind import UnionFind
from myHeap import Min_Heap


def readGraph(filename):
    edges = []
    with open(filename) as fp:
        lines = fp.readlines()
        num_nodes = int(lines[0])
        for everyline in lines[1:]:
            a = [int(i) for i in everyline.split(" ")][::-1]
            edges.append(tuple(a))

    return (num_nodes, edges)


def sort_edges(edges):
    # Q = Min_Heap()

    # for everyedge in edges:
    #     Q.insertKey(everyedge)

    # sorted_edges = []
    # while Q:
    #     sorted_edges.append(Q.extractMin())
    sorted_edges = sorted(edges, key=lambda x: x[0])

    return sorted_edges


def k_means_clustering(k, num_nodes, edges):

    print edges
    U = UnionFind(num_nodes)
    X = []

    cluster_count = num_nodes
    for everyedge in edges:
        p = everyedge[1] - 1
        q = everyedge[2] - 1

        if cluster_count == k:
            break

        if U.root(p) != U.root(q):
            X.append(everyedge)
            U.union(p, q)
            cluster_count = cluster_count - 1

    print U
    i = 0
    k_min_spacing = float('inf')
    while (i < len(edges)):
        w, p, q = edges[i]
        if U.root(p - 1) != U.root(q - 1):
            print p, q, w
            k_min_spacing = w if w < k_min_spacing else k_min_spacing
        i = i + 1

    return k_min_spacing


filename = "clustering1.txt"
filename = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course3\\assignment2Clustering\\question1\\input_completeRandom_1_8.txt"
num_nodes, edges = readGraph(filename)
print "Done reading"
sorted_edges = sort_edges(edges)
print "Done sorting"
print k_means_clustering(4, num_nodes, sorted_edges)
# 106

# pathdir = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course3\\assignment2Clustering\\question1"

# resultdir = open("Q1Results.txt", "w")

# for everyele in os.listdir(pathdir):
#     if "input" in everyele:

#         print everyele

#         with open(os.path.join(pathdir, everyele.replace("input", "output"))) as fp:
#             lines = fp.readlines()
#             result_required_diff = int(lines[0].strip())

#         num_nodes, edges = readGraph(os.path.join(pathdir, everyele))
#         sorted_edges = sort_edges(edges)
#         res = k_means_clustering(4, num_nodes, sorted_edges)

#         resultdir.write("Result_Spacing=%s, Filename=%s, Required_Spacing=%s, Obtained_Spacing=%s\n" %
#                         (result_required_diff == res, everyele, result_required_diff, res))

# resultdir.write("\n")
