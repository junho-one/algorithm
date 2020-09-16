# 백준 1810 : 징검다리 건너기 2
# 2816ms

import sys
from collections import defaultdict
import heapq
import math
import bisect

# N개
N, F = map(int, sys.stdin.readline().rstrip().split(" "))
graph = defaultdict(list)

stones = {}

stones[0] = [[0],0]
for _ in range(N) :
    a,b = map(int, sys.stdin.readline().rstrip().split(" "))
    if not stones.get(b) :
        stones[b] = [[],0]
    stones[b][0].append(a)

for key in stones.keys() :
    stones[key][0].sort()
    stones[key][1] = len(stones[key][0])

costs = defaultdict(lambda : float("inf"))
y_keys = list(stones.keys())
y_keys.sort()
y_len = len(y_keys)
heap = [(0,0,0)]
costs[(0,0)] = 0

answer = []
while heap :

    cost,x,y = heapq.heappop(heap)

    if y == F :
        answer.append(round(cost))

    for dy in [-2,-1,0,1,2] :
        if bisect.bisect_left(y_keys, y+dy) < y_len and y_keys[bisect.bisect_left(y_keys, y+dy)] == y+dy :

            for dx in [-2, -1, 0, 1, 2] :
                if bisect.bisect_left(stones[y+dy][0], x+dx) < stones[y+dy][1] and stones[y+dy][0][bisect.bisect_left(stones[y+dy][0], x+dx)] == x + dx:

                    next_cost = cost + math.sqrt(dx**2+dy**2)
                    if next_cost < costs[(x+dx,y+dy)] :
                        costs[(x+dx,y+dy)] = next_cost
                        heapq.heappush(heap, (next_cost, x+dx, y+dy))

if answer :
    print(min(answer))
else :
    print(-1)

# dictionary size가 5만이라 접근하는데 오래 걸릴 것이라고 생각하고,
# 이분탐색으로 logN에 접근하는 방법을 사용했는데 더 오래 걸린다.
# dictionary 접근이 O(1)로 잘 최적화돼 있어서 시간이 더 빠른듯.
