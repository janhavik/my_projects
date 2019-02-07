from heappractice import Heap
from math import isinf
import os
import pprint

# nodes = 12
# filename = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course2\\assignment2Dijkstra\\input_random_16_32.txt"
filename = "test_post.txt"


def readGraph(filename):

    # graph = {everyval: None for everyval in range(1, nodes)}
    graph = {}
    with open(filename) as fp:
        for everyline in fp:
            everyline = everyline.strip().split(" ")
            edges_weights = [[int(everyval.split(",")[0]), int(
                everyval.split(",")[1])] for everyval in everyline[1:]]

            graph[int(everyline[0])] = (edges_weights)

    return graph


def Djikstra(graph, source):

    dist = {everynode: float('inf') for everynode in graph}

    dist[source] = 0
    Q = Heap()

    Q.insertKey((0, source))
    for everynode in graph:
        if everynode != source:
            Q.insertKey((float('inf'), everynode))

    while Q:
        u = Q.extractMin()

        for v in graph[u[1]]:  # for all neighbours of u

            new_dist = (dist[u[1]] + v[1]) if not isinf(dist[u[1]]) else v[1]

            if Q.isInHeap(v[0]):
                print "source=",u, "dest=", v[0], new_dist
                if new_dist < dist[v[0]]:
                    print "Inside if", "source=",u, "dest=", v[0], new_dist
                    dist[v[0]] = new_dist
                    heap_pos_v = Q.find_index(v[0])
                    Q.decreaseKey(heap_pos_v, (new_dist, v[0]))
                    print "Heap", Q
                    print "*"*10

    return dist


graph = readGraph(filename)
print pprint.pformat(graph)
distances = Djikstra(graph, 1)
print distances
# print ",".join([str(val) for val in [distances[7], distances[37], distances[59], distances[82], distances[99], distances[115], distances[133], distances[165], distances[188], distances[197]]])

# pathdir = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course2\\assignment2Dijkstra"

# resultdir = open("Results.txt", "w")

# for everyele in os.listdir(pathdir):
#     if "input" in everyele:

#         graph = readGraph(os.path.join(pathdir, everyele))
#         # print len(graph), everyele

#         with open(os.path.join(pathdir, everyele.replace("input", "output"))) as fp1:
#             result_required = fp1.read().strip()

#         distances = Djikstra(graph, 1)
#         distances = ",".join([str(val) for val in [distances[7], distances[37], distances[59], distances[82],
#                                                    distances[99], distances[115], distances[133], distances[165], distances[188], distances[197]]])

#         resultdir.write("Result=%s, Filename=%s, Required=%s, Obtained=%s" %
#                         (result_required == distances, everyele, result_required, distances))

#         # print everyele, result_required == comparisons
#         resultdir.write("\n")


# resultdir.close()
# # Answer is 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068
