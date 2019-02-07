import os
import pprint
import time


def readFile(filename):
    with open(filename) as fp:
        lines = fp.readlines()
        knapsack_size_W, knapsack_items_n = int(
            lines[0].split(" ")[0]), int(lines[0].split(" ")[1])

        items = []
        for everyline in lines[1:]:
            items.append([int(i) for i in everyline.split(" ")])

    return (items, knapsack_items_n, knapsack_size_W)


def print_A(A):
    for e in A:
        print e


def knapsack(items, knapsack_items_n, knapsack_size_W):

    A = []

    for k in range(knapsack_items_n + 1):
        A.append([0] + [None] * (knapsack_size_W))

    for i in range(1, knapsack_items_n + 1):
        v_i = items[i - 1][0]
        w_i = items[i - 1][1]
        for x in range(knapsack_size_W + 1):
            # print "i=", i, "x=", x, "w_i=", w_i, "x-w_i=", x - w_i, "Vi=", v_i
            if w_i > x:
                A[i][x] = A[i - 1][x]
            else:
                A[i][x] = max([A[i - 1][x], (A[i - 1][x - w_i]
                                             if A[i - 1][x - w_i] else 0) + v_i])

    # print_A(A)

    # reconstruction algorithm
    cap = knapsack_size_W
    path = []
    for i in range(knapsack_items_n, 0, -1):
        if A[i][cap] > A[i - 1][cap]:
            path.append(i)  # case 2 succeeded
            cap = cap - items[i - 1][1]

    # print path
    print A[-1]
    # return (A[knapsack_items_n][knapsack_size_W], path)


def knapsack_reduced(items, knapsack_items_n, knapsack_size_W):

    A = [0] + [None] * (knapsack_size_W)    # store previous op

    curr_A = [0] + [None] * (knapsack_size_W)
    for i in range(1, knapsack_items_n + 1):
        v_i = items[i - 1][0]
        w_i = items[i - 1][1]
        for x in range(knapsack_size_W + 1):
            # print "i=", i, "x=", x, "w_i=", w_i, "x-w_i=", x - w_i, "Vi=", v_i
            if w_i > x:
                curr_A[x] = A[x]
            else:
                curr_A[x] = max([A[x], (A[x - w_i]
                                        if A[x - w_i] else 0) + v_i])

        # print A, curr_A
        A = curr_A[:]

    print A[-1]


# filename = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course3\\assignment4Knapsack\\input_random_40_1000000_2000.txt"
filename = "knapsack_big.txt"

t = time.time()
items, knapsack_items_n, knapsack_size_W = readFile(filename)
print "Read file done", time.time() - t
t = time.time()
print knapsack_reduced(items, knapsack_items_n, knapsack_size_W)
print "Computation done", time.time() - t
# print knapsack(items, knapsack_items_n, knapsack_size_W)
# 2493893

# pathdir = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course3\\assignment4Knapsack"

# resultdir = open("Q1Results.txt", "w")

# for everyele in os.listdir(pathdir):
#     if "input" in everyele:

#         with open(os.path.join(pathdir, everyele.replace("input", "output"))) as fp:
#             lines = fp.readlines()
#             result_required_diff = int(lines[0].strip())

#         items, knapsack_items_n, knapsack_size_W = readFile(
#             os.path.join(pathdir, everyele))
#         (S, res) = knapsack(items, knapsack_items_n, knapsack_size_W)
#         print everyele, result_required_diff == S

#         resultdir.write("res=%s, Filename=%s, Required_Spacing=%s, Obtained_Spacing=%s\n" %
#                         (result_required_diff == S, everyele, result_required_diff, S))

# resultdir.write("\n")
