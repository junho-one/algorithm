# # 백준 교환 1039

import sys
from collections import deque
from itertools import combinations

N,T = sys.stdin.readline().rstrip().split(" ")
M = len(N)
T = int(T)


comb = list(combinations(list(range(M)),2))
queue = deque()
queue.append(N)
answer = []
level = 0
while queue :

    if level == T :
        break

    visited = set()
    qlen = len(queue)
    for _ in range(qlen) :

        now = queue.popleft()
        now_list = list(now)
        for i,j in comb :

            if i == 0 and now_list[j] == '0' :
                continue

            now_list[i], now_list[j] = now_list[j], now_list[i]

            now_str = "".join(now_list)
            if now_str not in visited :
                queue.append(now_str)
                visited.add(now_str)

            now_list[i], now_list[j] = now_list[j], now_list[i]

    level += 1

if queue :
    print(max(queue))
else :
    print("-1")


# 최대 숫자가 1000000이라 사실상 최대 6자리이다.
# 이때 한 단계에서 중복을 없앤다면 나올 수 있는 숫자가 6! = 720이다. 6C2 = 15로 한 사이클에 최대 15*720의 연산.
# 총 10단계니 최대 경우의 수는 10*15*720으로 시간 안에 해결이 가능하다.
