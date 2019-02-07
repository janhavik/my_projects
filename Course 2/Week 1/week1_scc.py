import sys
import pickle
import threading

sys.setrecursionlimit(800000)
threading.stack_size(67108864)

nodes = 875715
visited = []
finishingtimes = []
current_node = ''
# filename_ip = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course2\\assignment1SCC\\input_mostlyCycles_68_320000.txt"
filename_ip = "SCC.txt"
sccs = []
final_sccs = []


def readGraph(filename):

    graph = {everyval: [] for everyval in range(1, nodes)}

    with open(filename) as fp:
        for everyline in fp:
            everyline = everyline.strip()

            key, value = int(everyline.split(" ")[0]), int(
                everyline.split(" ")[1])

            graph[key].append(value)

    return graph


def main():

    global visited, finishingtimes, sccs, final_sccs

    graph = readGraph(filename_ip)
    print "Reading graph completed\n"

    visited = [False] * len(graph)
    DFS_loop(graph)

    print "*************1st PASS FINISHED****************"

    graph_rev = reversegraph(graph)

    visited = [False] * len(graph)

    while finishingtimes:
        node = finishingtimes.pop()
        if not visited[node - 1]:
            DFS(graph_rev, node, finish=False)

            if len(sccs) == 1 and not graph[sccs[0]]:
                pass
            else:
                # print "Node=%d, Edges=%s" % (node, len(sccs))
                final_sccs.append(len(sccs))

            sccs = []

    print sorted(final_sccs)[-10:]
    print "*" * 30

    # with open(filename_ip.replace("input", "output")) as fp:
    #     print "Required Values are %s" % fp.read()


def reversegraph(graph):

    new_graph = {everyval: [] for everyval in range(1, nodes)}
    for everynode in graph:
        for everyhead in graph[everynode]:
            new_graph[everyhead].append(everynode)

    return new_graph


def DFS_loop(graph):

    global current_node, visited
    for everynode in range(nodes - 1, 0, -1):
        if not visited[everynode - 1]:
            DFS(graph, everynode)


def DFS(graph, vertex, finish=True):

    global visited, finishingtimes, sccs
    visited[vertex - 1] = True

    if not finish:
        sccs.append(vertex)

    for everynode in graph[vertex]:
        if not visited[everynode - 1]:
            DFS(graph, everynode, finish=finish)

    if finish:
        finishingtimes.append(vertex)


thread = threading.Thread(target=main)
thread.start()
