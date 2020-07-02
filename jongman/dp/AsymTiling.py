def allTiling(width) :

    if dp[width] :
        return dp[width]

    if width <= 1 :
        return 1

    ret = ( allTiling(width-2) + allTiling(width-1) ) % 1000000007

    dp[width] = ret
    return dp[width]

def asymTiling(width) :

    if width <= 2 :
        return 0

    if width %2 == 1 :
        # [~~]|[~~] 인 경우
        half = width//2
        return ( allTiling(width) - allTiling(half) + MOD ) % MOD

    # [~~~~][~~~~] , [~~~~]=[~~~~] 인 경우
    ret = allTiling(width) % MOD
    one = allTiling(width//2) % MOD
    two = allTiling(width//2 -1) % MOD

    ret = ( (ret - one) + MOD) % MOD
    ret = ( (ret - two) + MOD) % MOD

    return ret

import sys

T = int(sys.stdin.readline().rstrip())

for _ in range(T):

    N = int(sys.stdin.readline().rstrip())
    MOD = 1000000007
    dp = [None for _ in range(N+1)]
    # print(allTiling(N))
    print(asymTiling(N))


# 비대칭 타일링을 구하기 위해 비대칭 타일을 직접 구하는 방법도 있지만, 전체 타일에서 대칭 타일을 빼면 비대칭 타일의 개수가 나온다
# 특정 width의 타일을 구하는 타일링 재귀는 값을 모두 dp에 저장해두기에 비슷한 값이 들어가면 O(1)로 값을 반환한다.

