from heappractice import Heap
from math import isinf
import os
import pprint

# filename = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course3\\assignment1SchedulingAndMST\\question3\\input_random_2_10.txt"
filename = "edges.txt"


def readGraph(filename):

    with open(filename) as fp:
        lines = fp.readlines()
        num_nodes, num_edges = int(lines[0].split(
            " ")[0]), int(lines[0].split(" ")[1])
        graph = {everynode: [] for everynode in range(1, num_nodes + 1)}

        for everyline in lines[1:]:
            everyline = everyline.strip().split(" ")

            graph[int(everyline[0])].append([int(everynum)
                                             for everynum in everyline[1:]])
            graph[int(everyline[1])].append(
                [int(everyline[0]), int(everyline[-1])])

    return (num_nodes, graph)


def MST_Prim(graph, num_nodes, source):

    Q = Heap()
    distance_mst = 0
    visited_nodes = [False] * num_nodes
    MST = []

    i = 0
    current_vertex = source
    while i < num_nodes:

        # process if vertex not visited by mst
        if not visited_nodes[current_vertex - 1]:
            # print "Unvisited", current_vertex
            visited_nodes[current_vertex - 1] = True

            # push this into the heap and extract min and set that as the current vertex
            nodes_current_vertex = graph[current_vertex]
            for everynode in nodes_current_vertex:
                Q.insertKey((everynode[-1], everynode[-2], current_vertex))

            # extract min
            next_vertex = Q.extractMin()

            # if vertex is new then add to the MST
            if not visited_nodes[next_vertex[1] - 1]:
                MST.append((next_vertex[1], next_vertex[0]))

            current_vertex = next_vertex[1]
            i = i + 1

        else:
            # if it is univisted, remove it from consideration next by extracting
            # print "Visited", current_vertex
            next_vertex = Q.extractMin()
            if not visited_nodes[next_vertex[1] - 1]:
                MST.append((next_vertex[1], next_vertex[0]))

            current_vertex = next_vertex[1]

    MST.insert(0, (source, 0))
    return (MST, sum([w[-1] for w in MST]))


num_nodes, graph = readGraph(filename)
print MST_Prim(graph, num_nodes, 1)

# -3612829

# pathdir = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course3\\assignment1SchedulingAndMST\\question3"

# resultdir = open("Results.txt", "w")

# for everyele in os.listdir(pathdir):
#     if "input" in everyele:

#         num_nodes, graph = readGraph(os.path.join(pathdir, everyele))
#         print everyele

#         with open(os.path.join(pathdir, everyele.replace("input", "output"))) as fp1:
#             result_required = int(fp1.read().strip())

#         distances = MST_Prim(graph, num_nodes, 1)

#         resultdir.write("Result=%s, Filename=%s, Required=%s, Obtained=%s \n" %
#                         (result_required == distances[-1], everyele, result_required, distances[-1]))

#         # print everyele, result_required == comparisons

# resultdir.write("\n")
