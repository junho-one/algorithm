# 이항계쑤

dp = [ [ 0 for _ in range(1000)] for _ in range(1000)]

def bino(n, r) :

    if r == 0 or n == r :
        return 1

    if dp[n][r] != 0 :
        return dp[n][r]

    dp[n][r] = bino(n-1,r-1) + bino(n-1,r)

    return dp[n][r]

print(bino(25,12))
