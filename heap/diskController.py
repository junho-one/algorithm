import heapq


def solution(jobs):
    answer = 0
    heap = []
    N = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[0])


    i = 0
    jobIdx = 0
    using = 0
    endTime = 0
    while jobIdx < len(jobs) or heap :
        # print(heap, endTime)
        if jobIdx < len(jobs) and i <= jobs[jobIdx][0] :
            heapq.heappush(heap, ( jobs[jobIdx][1], jobs[jobIdx][0]) )
            jobIdx += 1

        if i >= heap[0][1] and i >= endTime:
            takenTime, startTime = heapq.heappop(heap)
            endTime = i + takenTime

        if i <= endTime :
            answer = answer + 1 + len(heap)

        i += 1


    mean = int( (answer + takenTime) / N )

    return mean


print( solution([[0, 3], [1, 9], [2, 6]]) )
