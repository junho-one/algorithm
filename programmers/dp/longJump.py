# 프로그래머스 멀리 뛰기
import sys

sys.setrecursionlimit(500000)


def solution(n):
    def go(n):
        if n == 1:
            return 1
        if n == 2:
            return 2

        if dp[n]:
            return dp[n]

        dp[n] = (go(n - 2) + go(n - 1)) % 1234567
        return dp[n]

    answer = 0
    dp = [None] * 2000

    return go(n)