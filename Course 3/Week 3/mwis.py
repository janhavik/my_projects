import os


def readWeights(filename):

    weights = {}
    with open(filename) as fp:
        lines = fp.readlines()
        num_vertex = int(lines[0])
        for i in range(len(lines[1:])):
            weights[i + 1] = (int(lines[i + 1]))

    return (num_vertex, weights)


def MWIS(num_vertex, weights):

    A = {0: 0, -1: 0, 1: weights[1]}
    for i in range(2, num_vertex + 1):
        G_i = A[i - 1]
        G_i_1 = A[i - 2] + weights[i]
        A[i] = max(G_i, G_i_1)

    # print A

    S = []
    i = num_vertex
    while i >= 1:
        # print i, A[i - 1], A[i - 2] + weights[i]
        # case 1 wins, vn is not part of the group
        if A[i - 1] > A[i - 2] + weights[i]:
            i = i - 1
        else:
            S.append(i)
            i = i - 2

    ans = ""
    ans = ans + ("1" if 1 in S else "0")
    ans = ans + ("1" if 2 in S else "0")
    ans = ans + ("1" if 3 in S else "0")
    ans = ans + ("1" if 4 in S else "0")
    ans = ans + ("1" if 17 in S else "0")
    ans = ans + ("1" if 117 in S else "0")
    ans = ans + ("1" if 517 in S else "0")
    ans = ans + ("1" if 997 in S else "0")

    return (S, ans)


# filename = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course3\\assignment3HuffmanAndMWIS\\question3\\input_random_2_10.txt"
filename = "mwis.txt"
num_vertex, weights = readWeights(filename)
print MWIS(num_vertex, weights)
# 10100110

# pathdir = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course3\\assignment3HuffmanAndMWIS\\question3"

# resultdir = open("Q3Results.txt", "w")

# for everyele in os.listdir(pathdir):
#     if "input" in everyele:

#         with open(os.path.join(pathdir, everyele.replace("input", "output"))) as fp:
#             lines = fp.readlines()
#             result_required_diff = lines[0].strip()

#         num_vertex, weights = readWeights(os.path.join(pathdir, everyele))
#         (S, res) = MWIS(num_vertex, weights)
#         print everyele, result_required_diff == res

#         resultdir.write("res=%s, Filename=%s, Required_Spacing=%s, Obtained_Spacing=%s\n" %
#                         (result_required_diff == res, everyele, result_required_diff, res))

# resultdir.write("\n")
