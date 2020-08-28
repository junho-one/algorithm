# 프로그래머스 도둑질

# 원형 문제 팁!!!
# 원으로 생각하면 풀기 힘드니까 1. 첫번쨰 집을 훔치는 경우 2. 첫번째 집을 훔치지 않는 경우로 나누어 두가지 경우를 구해보면 된다.

# 점화식이
# 집이 1개이면 그 집을 털고
# 집이 2개이면 더 비싼 집을 털고
# 집이 3개이면 (A,B,C)  A와C의 합과 B 중에 더 비싼 곳을 털면 된다.
def solution(money):
    answer = 0
    N = len(money)
    dp1 = [None for _ in range(N)]
    dp2 = [None for _ in range(N)]

    if N == 1:
        return money[0]
    elif N == 2:
        return max(money[0], money[1])

    # 무조건 0번째 집은 훔치겠다.
    # 2번째 집의 dp를 구할 때 dp[0] + money[2], dp[1] 중 큰 값을 고르는데 무조건 dp[0] + money[2]가 된다.
    # 3번째 집의 dp를 구할때는 dp[1] + money[3], dp[2] 중 큰 값을 고르는데
    # dp[1]은 money[0]과 같으므로 dp[2]와 dp[1]에 모두 0번 집을 고른거와 같은 가격이 들어가 있음
    dp1[0] = money[0]
    dp1[1] = money[0]
    # 0번째 집 훔치면 -1 번째 집은 훔칠 수 없으니 N-1까지만
    for i in range(2, N - 1):
        dp1[i] = max(dp1[i - 2] + money[i], dp1[i - 1])

    # 무조건 0번째 집은 훔치지 않겠다.
    # 2번째 집의 dp를 구할 때 dp[0] + money[2], dp[1] 중 큰 값인데 dp[0]은 money[0]이 아닌 0이라 어느 값을 고르더라도 0번째 집은 선택 안한 가격이다.
    # 2번째 집에서 0번째 집을 안고르는 효과가 나는 것. 그 이후로는 dp[0],dp[1], dp[2]를 쓰기에 money[0]이 사용되는 일은 없다.
    dp2[0] = 0  # -10000 하면 에러
    dp2[1] = money[1]
    for i in range(2, N):
        dp2[i] = max(dp2[i - 2] + money[i], dp2[i - 1])

    return max(dp1[-2], dp2[-1])