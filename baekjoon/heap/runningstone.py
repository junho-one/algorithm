# 백준 1810
import heapq
import sys
from collections import defaultdict
import bisect
import math

N, F = map(int, sys.stdin.readline().rstrip().split(" "))
stones = defaultdict(list)

cost = {}
for _ in range(N) :
    x,y = map(int, sys.stdin.readline().rstrip().split(" "))
    stones[y].append(x)
    cost[y,x] = float('inf')

for y in stones.keys() :
    stones[y].sort()

cost[0,0]= float('inf')
stones[0] = [0]
heap = [(0,0,0)]

answer = float('inf')

while heap :

    now_cost,y,x = heapq.heappop(heap)

    if y == F :
        answer = min(answer, now_cost)
        continue

    if cost[y,x] < now_cost :
        continue

    for dy in [-2,-1,0, 1, 2]:
        for dx in [-2, -1, 0, 1, 2]:

            if stones.get(y+dy) :
                idx = bisect.bisect_right(stones[y+dy], x+dx) -1

                if stones[y+dy][idx] == x+dx :
                    distance = now_cost + math.sqrt(dy**2 + dx**2)

                    if distance < cost[y+dy,x+dx]  :
                        cost[y+dy,x+dx] = distance
                        heapq.heappush(heap, (distance,y+dy,x+dx))

if answer == float('inf') :
    print(-1)
else :
    print(round(answer))

# import bisect
#
# sequence = [1, 3, 4, 5,7,10]
#
# print(bisect.bisect_right(sequence, 8))
# print(bisect.bisect_left(sequence, 8))
# idx = bisect.bisect_left(sequence, 5)
#
# dx = 0x
# while idx :
#     up = idx+dx
#     down = idx-dx
#     print(up, down, sequence[down])
#     if down < 0 and up > len(sequence) :
#         break
#
#     dx+=1