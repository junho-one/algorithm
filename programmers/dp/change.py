def solution(n, money):

    def go(change, idx):
        if change == 0 :
            return 1

        if idx == length :
            return 0

        if dp[change] :
            return dp[change]

        ret = 0
        cnt = change // money[idx]
        for i in range(cnt+1) :
            if change-money[idx]*i >= 0:
                ret += go(change-money[idx]*i, idx+1)

        dp[change] = ret
        return dp[change]

    length = len(money)
    dp = [None] * 100001

    return go(n, 0)

print(solution(5, [1,2,5]))

#
# def solution(n, money):
#     answer = 0
#
#     def go(change):
#
#         if change == 0 :
#             return 1
#
#         if dp[change] :
#             return dp[change]
#
#         ret = 0
#         for m in money :
#             if change - m >= 0 :
#                 cnt = change // m
#
#                 for i in range(1,cnt+1) :
#                     print(change, m, cnt)
#                     ret += go(change-m*i)
#
#         dp[change] = ret
#         return dp[change]
#
#
#     dp = [None] * 100001
#
#     return go(n)
#
# print(solution(5, [1,2,5]))