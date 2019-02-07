import os
import time
inversions = 0


def sort_array(ip1, ip2):

    sort_ip = list()
    len_ip1 = len(ip1)
    len_ip2 = len(ip2)
    i = 0
    j = 0
    inversions = 0

    while (i < len_ip1 and j < len_ip2):
        if ip1[i] <= ip2[j]:
            sort_ip.append(ip1[i])
            i = i + 1
        else:
            sort_ip.append(ip2[j])
            j = j + 1
            # both arrays are sorted, the minute there is one item greater, it is going to reflect over all the small elements
            inversions = inversions + (len_ip1 - i)
            # inversions = inversions + 1

    sort_ip.extend(ip1[i:])
    sort_ip.extend(ip2[j:])

    # print ip1, ip2, len(ip1), len(ip2), "i=", i, "j=", j, inversions, inversions + i * len_ip1
    print sort_ip
    return (inversions, sort_ip)


def mergeSort(a):

    global inversions
    b = a[:]  # avoid aliasing

    len_b = len(b)
    if len_b <= 1:
        return (inversions, b)

    left_half = b[:len_b / 2]
    right_half = b[len_b / 2:]

    left_half = mergeSort(left_half)[1]
    right_half = mergeSort(right_half)[1]

    # print "Prinitng from merge sort", left_half, right_half, sort_array(left_half, right_half)

    invs, sorted_array = sort_array(left_half, right_half)
    inversions = inversions + invs
    return (inversions, sorted_array)


print mergeSort([5, 3, 8, 9, 1, 7, 0, 2, 6, 4])

# pathdir = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course1\\assignment2Inversions"

# resultdir = open(os.path.join(pathdir, "Results.txt"), "w")

# for everyele in os.listdir(pathdir):
#     if "input" in everyele:
#         with open(os.path.join(pathdir, everyele)) as fp:
#             numbers = [int(f.strip()) for f in fp.readlines()]

#         with open(os.path.join(pathdir, everyele.replace("input", "output"))) as fp1:
#             result_required = int(fp1.read().strip())

#         res = mergeSort(numbers)
#         print res[0]
#         resultdir.write("Result=%s, Filename=%s, Inversions=%s, SortedNumbers=%s" %
#                         (result_required == res[0], everyele, res[0], res[1]))
#         inversions = 0
#         resultdir.write("\n")

# resultdir.close()
