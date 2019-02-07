import os
import numpy
comparisons = 0


def find_median(a, b, c):

    temp = [a, b, c]
    temp = sorted(temp)
    return temp[1]


def QuickSort(ip, l, r):

    # base case
    if (r - l) < 2:
        return ip

    partitioned_index = partition(ip, l, r)
    QuickSort(ip, l, partitioned_index)
    QuickSort(ip, partitioned_index + 1, r)


def partition(ip, l1, r1):

    global comparisons
    comparisons = comparisons + (r1 - l1 - 1)
    len_input = r1 - l1 - (1 if (r1 - l1) % 2 == 0 else 0)
    # ip[l1], ip[r1-1] = ip[r1-1], ip[l1] # if pivot element is last element in the array, then swap and keep everything else same

    # print ip
    # take median of the first, middle and last element
    median = find_median(ip[l1],
                         ip[l1 + len_input / 2],
                         ip[r1 - 1])

    index_swap = ip.index(median)
    ip[l1], ip[index_swap] = ip[index_swap], ip[l1]

    p = ip[l1]
    i = l1 + 1

    # partition the array around the pivot
    for j in range(i, r1):

        if ip[j] < p:
            ip[i], ip[j] = ip[j], ip[i]  # swap
            i = i + 1

    ip[l1], ip[i - 1] = ip[i - 1], ip[l1]
    return i - 1


if __name__ == '__main__':
    A = [3,
         2,
         10,
         6,
         7,
         1,
         9,
         5,
         4,
         8]
    QuickSort(A, 0, len(A))
    print A, comparisons

# pathdir = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course1\\assignment3Quicksort"

# resultdir = open(os.path.join(pathdir, "Results.txt"), "w")

# for everyele in os.listdir(pathdir):
#     if "input" in everyele:
#         with open(os.path.join(pathdir, everyele)) as fp:
#             numbers = [int(f.strip()) for f in fp.readlines()]

#         with open(os.path.join(pathdir, everyele.replace("input", "output"))) as fp1:
#             result_required = int(fp1.readlines()[2].strip())

#         QuickSort(numbers, 0, len(numbers))

#         resultdir.write("Result=%s, Filename=%s, Inversions=%s, SortedNumbers=%s" %
#                         (result_required == comparisons, everyele, comparisons, numbers))

#         print everyele, result_required == comparisons
#         comparisons = 0
#         resultdir.write("\n")


# resultdir.close()
