# 프로그래머스 정수 삼각형
import sys
sys.setrecursionlimit(500000)

def solution(triangle):
    def go(level, idx):
        if level == N :
            return 0
        if dp[level][idx] :
            return dp[level][idx]

        ret = 0
        for i in range(idx, idx + 2):
            ret = max(ret, go(level + 1, i))

        dp[level][idx] = ret + triangle[level][idx]
        return dp[level][idx]

    N = len(triangle)
    dp = [[None for _ in range(N)] for _ in range(N)]
    return go(0, 0)

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))