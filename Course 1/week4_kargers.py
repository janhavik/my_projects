import re
import random
import os


def get_graph(filename):

    nodelists = {}
    with open(filename) as fp:
        for line in fp.readlines():
            line = [int(i) for i in line.strip().split(" ")]
            nodelists[line[0]] = line[1:]

    return nodelists


def get_random_egde():

    v1 = random.sample(nodelists.keys(), 1)[0]
    v2 = random.sample(nodelists[v1], 1)[0]
    return (v1, v2)


def contract_edge(edge):

    global nodelists

    # print edge
    # print nodelists[edge[0]]

    # merge v2 into v1 and remove v2 from graph
    v1l = nodelists[edge[0]]
    v1l.extend(nodelists[edge[1]])
    del nodelists[edge[1]]

    # print nodelists[edge[0]]

    # replace all occurnces of v2 value with v1
    for k, l in nodelists.iteritems():
        nodelists[k] = [edge[0] if x == edge[1] else x for x in nodelists[k]]

    # Remove all edges of v1 to itself(loops)
    nodelists[edge[0]] = [x for x in nodelists[edge[0]] if x != edge[0]]
    # print nodelists[edge[0]]

    # print "*" * 30


def get_min_cut(filename):

    global nodelists
    minlist = []

    for i in range(0, 40):
        nodelists = get_graph(filename)

        # Keep contracting the graph until we have 2 vertices
        while(len(nodelists) > 2):
            contract_edge(get_random_egde())

        minlist.append(len(nodelists[nodelists.keys()[0]]))

    return minlist[:]


# print "Min cut=%s" % min(get_min_cut("kargerMinCut.txt"))
print "Min cut=%s" % min(get_min_cut("F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course1\\assignment4MinCut\\input_random_1_6.txt"))
# pathdir = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course1\\assignment4MinCut\\"

# resultdir = open(os.path.join(pathdir, "Results.txt"), "w")

# for everyele in os.listdir(pathdir):
#     if "input" in everyele:
#         # with open(os.path.join(pathdir, everyele)) as fp:
#         #     numbers = [int(f.strip()) for f in fp.readlines()]

#         print "Running for %s" % everyele
#         with open(os.path.join(pathdir, everyele.replace("input", "output"))) as fp1:
#             result_required = int(fp1.read().strip())

#         mincut = get_min_cut(os.path.join(pathdir, everyele))

#         resultdir.write("Result=%s, Required=%s, Filename=%s, Micuts obtained=%s, Mincut=%s" %
#                         (result_required == min(mincut), result_required, everyele, mincut, min(mincut)))

#         resultdir.write("\n")

# resultdir.close()
