import heapq

def solution(distance, rocks, n):
    answer = 0

    rocks = [0] + sorted(rocks) + [distance]
    heap = []
    for i in range(1, len(rocks)) :
        heap.append( (rocks[i] - rocks[i-1], i-1, i))
    print(heap)
    heapq.heapify(heap)
    print(heap)

    deleted = set()

    for _ in range(n) :

        dist, left, right = heapq.heappop(heap)


        if (left, right) not in deleted :


    return heapq.heappop(heap)

print(solution(25, [2,14,11,21,17], 2))