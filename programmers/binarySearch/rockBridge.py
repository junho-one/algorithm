import heapq

def solution(distance, rocks, n):
    answer = 0

    rocks = [0] + sorted(rocks) + [distance]
    heap = []
    distances = []
    for i in range(1, len(rocks)) :
        heapq.heappush(heap, rocks[i] - rocks[i-1])
        distances.append(rocks[i] - rocks[i-1])
    print(heap)
    print(distances)
    for _ in range(n) :
        d1 = heapq.heappop(heap)
        d2 = heapq.heappop(heap)
        heapq.heappush(heap, d1+d2)

    return heapq.heappop(heap)

print(solution(25, [2,14,11,21,17], 2))