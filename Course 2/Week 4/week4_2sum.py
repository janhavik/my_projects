import os
import pprint
import traceback


def readInput(filename):

    with open(filename) as fp:
        numbers = [int(num) for num in fp.readlines()]

    return numbers


def two_sum(numbers):

    # initialize hash map
    hash_map = {everynum: True for everynum in numbers}
    hash_map_done = {everynum: False for everynum in numbers}
    count = 0
    validTarget = False

    for target in range(-10000, 10001):
        print "Target=", target
        for everynum in numbers:
            x = everynum
            y = target - x
            try:
                if hash_map[y] and not hash_map_done[x]:
                    # print "Found pairs:", x, y, x+y, target, (x+y)==target
                    hash_map_done[x] = True
                    hash_map_done[y] = True
                    validTarget = True
            except KeyError as e:
                # traceback.print_exc()
                # print "Error obtained", str(e)
                pass

        hash_map = {everynum: True for everynum in numbers}
        hash_map_done = {everynum: False for everynum in numbers}
        count = count + 1 if validTarget else count
        validTarget = False

    return count


numbers = readInput("2sum.txt")
# numbers = readInput(
#     "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course2\\assignment4TwoSum\\input_random_56_80000.txt")

print two_sum(numbers)

# pathdir = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course2\\assignment4TwoSum"

# resultdir = open("Results.txt", "w")

# for everyele in os.listdir(pathdir):
#     if "input" in everyele:

#         numbers = readInput(os.path.join(pathdir, everyele))
#         print everyele

#         with open(os.path.join(pathdir, everyele.replace("input", "output"))) as fp1:
#             result_required = int(fp1.read().strip())

#         distances = two_sum(numbers)

#         resultdir.write("Result=%s, Filename=%s, Required=%s, Obtained=%s" %
#                         (result_required == distances, everyele, result_required, distances))

#         # print everyele, result_required == comparisons
#         resultdir.write("\n")


# resultdir.close()
