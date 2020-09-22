import sys
from collections import defaultdict

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    N, D, P = map(int, sys.stdin.readline().rstrip().split(" "))

    matrix = defaultdict(list)
    for now in range(N) :
        for idx, val in enumerate(list(map(int, sys.stdin.readline().rstrip().split(" ")))) :
            if val == 1 :
                matrix[now].append(idx)

    T = int(sys.stdin.readline().rstrip())

    towns = map(int, sys.stdin.readline().rstrip().split(" "))

    def go(now, day) :
        if day == 0 :
            if now == town :
                return 1
            else :
                return 0

        if dp[now][day] :
            return dp[now][day]

        prob = 0
        for next in matrix[now] :
            prob += go(next, day-1) / len(matrix[now])

        dp[now][day] = prob
        return prob

    for town in towns :
        dp = [[None for _ in range(D+1)] for _ in range(N)]
        print( go(P, D) , end = " ")
