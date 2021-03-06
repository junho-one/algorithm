import sys
sys.setrecursionlimit(10**6)

# 1개

# def tiling2(start) :
#
#     if dp[start] :
#         return dp[start]
#
#     if N-start <= 1 :
#         return 1
#
#     ret = 0
#     for i in range(1,3):
#         if start+i <= N :
#             ret =  (ret%10007 + tiling2(start+i)%10007) % 10007
#
#     dp[start] = ret
#     return dp[start]
#
# ans = 0
# print(tiling2(0))


def tiling2(width) :

    if width <= 1 :
        return 1

    if dp[width] :
        return dp[width]

    ret = ( tiling2(width-2)  + tiling2(width-1) ) % 1000000007

    dp[width] = ret

    return dp[width]



T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    N = int(sys.stdin.readline().rstrip())
    dp = [None for _ in range(1001)]
    print(tiling2(N))