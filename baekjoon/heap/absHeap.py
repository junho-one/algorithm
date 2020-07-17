import sys
import heapq
from collections import defaultdict, deque

# 1개
N = int(sys.stdin.readline().rstrip())

heap = []
data = []
mapped = defaultdict(list)

for _ in range(N) :
    data.append(int(sys.stdin.readline().rstrip()))

for val in data :
    if val == 0 and heap:
        # print(mapped[heapq.heappop()].pop())
        print(heapq.heappop(heap)[1])
    elif val != 0 :
        heapq.heappush(heap,(abs(val),val ))
        # mapped[abs(val)].append(val)
    else :
        print(0)