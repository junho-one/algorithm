# 종만 조세푸스
import sys
from collections import defaultdict

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    N, K = map(int, sys.stdin.readline().rstrip().split(" "))

    soldiers = list(range(1,N+1))

    # print(soldiers)

    num = len(soldiers)
    idx = 0
    while num > 2 :
        soldiers.pop(idx)
        # print(soldiers, idx)
        num -= 1
        idx = ( idx + K - 1) % num

    for s in soldiers :
        print(s , end=" ")
    # print(soldiers)
