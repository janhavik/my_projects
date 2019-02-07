from myHeap import Min_Heap, Max_Heap
import os
import random


def readInput(filename):

    with open(filename) as fp:
        numbers = [int(num) for num in fp.readlines()]

    return numbers


def median_maintenance(numbers):

    min_Heap = Min_Heap()
    max_Heap = Max_Heap()
    required_len = len(numbers) / 2
    current_median = 0
    sum_of_medians = 0

    for i in range(0, len(numbers)):

        # insert new element
        if numbers[i] > current_median:
            min_Heap.insertKey(numbers[i])
        else:
            max_Heap.insertKey(numbers[i])

        # balance the heaps
        if (len(min_Heap) - len(max_Heap)) > 1:
            max_Heap.insertKey(min_Heap.extractMin())
        if (len(max_Heap) - len(min_Heap)) > 1:
            min_Heap.insertKey(max_Heap.extractMax())

        # now update the median
        if (len(min_Heap) - len(max_Heap)) == 1:
            current_median = min_Heap.getMin()
        if (len(max_Heap) - len(min_Heap)) == 1 or len(min_Heap) == len(max_Heap):
            current_median = max_Heap.getMax()

        # print "MinHeap=", min_Heap, "Maxheap=", max_Heap, "Current median", current_median
        sum_of_medians = sum_of_medians + current_median

    return sum_of_medians


numbers = readInput("medians.txt")
# numbers = readInput(
#     "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course2\\assignment3Median\\input_random_1_10.txt")
# # numbers = range(1, 10)
# # random.shuffle(numbers)
# # print numbers
print median_maintenance(numbers) % 10000

# pathdir = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course2\\assignment3Median"

# resultdir = open("Results.txt", "w")

# for everyele in os.listdir(pathdir):
#     if "input" in everyele:

#         numbers = readInput(os.path.join(pathdir, everyele))
#         print everyele

#         with open(os.path.join(pathdir, everyele.replace("input", "output"))) as fp1:
#             result_required = int(fp1.read().strip())

#         distances = median_maintenance(numbers) % 10000

#         resultdir.write("Result=%s, Filename=%s, Required=%s, Obtained=%s" %
#                         (result_required == distances, everyele, result_required, distances))

#         # print everyele, result_required == comparisons
#         resultdir.write("\n")


# resultdir.close()
