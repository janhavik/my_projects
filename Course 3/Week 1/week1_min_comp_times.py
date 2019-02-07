import os
import pprint
from myHeap import Max_Heap


def readFile(filename):

    jobs = []
    with open(filename) as fp:
        lines = fp.readlines()
        number_of_jobs = int(lines[0])

        for everyline in lines[1:]:
            everyline = everyline.strip().split(" ")
            jobs.append(tuple([int(everynum) for everynum in everyline]))

    return (jobs, number_of_jobs)


def schedule_difference(jobs, number_of_jobs):

    Q = Max_Heap()
    differences = [(j[0] - j[1], j[0], j[1]) for j in jobs]
    for everyjob in differences:
        Q.insertKey(everyjob)

    job_schedule = []
    while Q:
        job = Q.extractMax()
        job_schedule.append(job)

    difference_unique = []
    for everydiff in job_schedule:
        if everydiff[0] not in difference_unique:
            difference_unique.append(everydiff[0])

    # print job_schedule
    # print "*" * 30

    for everydiff in difference_unique:
        a = [i for i in job_schedule if i[0] == everydiff]
        index_to_start = job_schedule.index(a[0])
        if len(a) > 1:
            temp = sorted(a, key=lambda x: x[1], reverse=True)
            for everyval in range(0, len(temp)):
                job_schedule[index_to_start + everyval] = temp[everyval]

    # print job_schedule
    # print "*" * 30

    completion_time = 0
    for i in range(0, len(job_schedule)):
        completion_time = completion_time + \
            job_schedule[i][1] * sum([job[-1] for job in job_schedule[:i + 1]])

    return (job_schedule, completion_time)


def schedule_ratio(jobs, number_of_jobs):

    Q = Max_Heap()
    differences = [(j[0] / float(j[1]), j[0], j[1]) for j in jobs]
    for everyjob in differences:
        Q.insertKey(everyjob)

    job_schedule = []
    while Q:
        job_schedule.append(Q.extractMax())

    # print job_schedule

    completion_time = 0
    for i in range(0, len(job_schedule)):
        completion_time = completion_time + \
            job_schedule[i][1] * sum([job[-1] for job in job_schedule[:i + 1]])

    return (job_schedule, completion_time)


# filename = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course3\\assignment1SchedulingAndMST\\questions1And2\\input_random_11_40.txt"
filename = "jobs.txt"
jobs, number_of_jobs = readFile(filename)
print schedule_difference(jobs, number_of_jobs)[-1]
print schedule_ratio(jobs, number_of_jobs)[-1]
# 69119377652
# 67311454237

# pathdir = "F:\\Learning\\coursera\\Algorithms Exercises\\stanford-algs\\testCases\\course3\\assignment1SchedulingAndMST\\questions1And2"

# resultdir = open("Q1_3Results.txt", "w")

# for everyele in os.listdir(pathdir):
#     if "input" in everyele:

#         jobs, number_of_jobs = readFile(os.path.join(pathdir, everyele))
#         print everyele

#         with open(os.path.join(pathdir, everyele.replace("input", "output"))) as fp:
#             lines = fp.readlines()
#             result_required_diff = int(lines[0].strip())
#             result_required_ratio = int(lines[1].strip())

#         job_schedule_diff, comp_diff = schedule_difference(
#             jobs, number_of_jobs)
#         job_schedule_ratio, comp_ratio = schedule_ratio(
#             jobs, number_of_jobs)

#         resultdir.write("Result_Diff=%s, Result_Ratio=%s, Filename=%s, Required_Diff=%s, Ratio_Diff=%s, Obtained_Diff=%s, Obtained_Ratio=%s\n" %
#                         (result_required_diff == comp_diff, result_required_ratio == comp_ratio, everyele, result_required_diff, result_required_ratio, comp_diff, comp_ratio))

# resultdir.write("\n")
