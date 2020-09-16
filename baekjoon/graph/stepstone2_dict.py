# 백준 1810 : 징검다리 건너기 2
# 1240ms

import sys
from collections import defaultdict, deque
import math
import heapq

# N개
N, F = map(int, sys.stdin.readline().rstrip().split(" "))
graph = defaultdict(list)

stones = {}
costs = {}
for _ in range(N) :
    a,b = map(int, sys.stdin.readline().rstrip().split(" "))
    stones[(a,b)] = True
    costs[(a,b)] = float("inf")


heap = [(0,0,0)]
stones[(0,0)] = True
costs[(0,0)] = 0

answer = []
while heap :

    cost,x,y = heapq.heappop(heap)

    if y == F :
        answer.append(round(cost))

    for dx in [-2,-1,0,1,2] :
        for dy in [-2,-1,0,1,2] :
            nx = x+dx
            ny = y+dy

            if stones.get((nx,ny)) :
                next_cost = cost + math.sqrt(dx**2 + dy**2)

                if next_cost < costs[(nx,ny)] :
                    costs[(nx,ny)] = next_cost
                    heapq.heappush(heap, (next_cost,nx,ny))

if answer :
    print(min(answer))
else :
    print(-1)

# 그냥 딕셔너리로 돌의 위치를 넣고, 다익스트라 하면 된다.
