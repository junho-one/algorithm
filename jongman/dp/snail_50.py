import sys

def snail(days, climbs) :

    if days == M :
        if climbs >= N :
            return 1
        else :
            return 0

    if dp[days][climbs] :
        return dp[days][climbs]

    ret = snail(days + 1, climbs + 1) + snail(days+1, climbs+2)

    dp[days][climbs] = ret

    return dp[days][climbs]



# 1개
T = int(sys.stdin.readline().rstrip())

for _ in range(T) :

    N, M = map(int, sys.stdin.readline().rstrip().split(" "))
    dp = [ [None for _ in range(1001)] for _ in range(2001)]
    print( snail(0,0) / pow(2,M))



# 비, 맑음의 확률이 50%이다. 이럴 때는 경우의 수로 계산할 수 있다.
# 두 날씨의 확률이 다를 때는 확률로 계산해야 함
