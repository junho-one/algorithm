def solution(sticker):
    if len(sticker) <= 2:
        answer = 0
        for s in sticker:
            answer = max(s, answer)
        return answer

    else:
        dp1 = [None] * 100002
        dp1[0] = sticker[0]
        dp1[1] = sticker[0]
        for i in range(2, len(sticker) - 1):
            dp1[i] = max(dp1[i - 2] + sticker[i], dp1[i - 1])

        dp2 = [None] * 100002
        dp2[0] = 0
        dp2[1] = sticker[1]

        for i in range(2, len(sticker)):
            dp2[i] = max(dp2[i - 2] + sticker[i], dp2[i - 1])

        return max(dp1[len(sticker) - 2], dp2[len(sticker) - 1])

# 이 문제의 핵심은 첫번째 스티커를 포함하는 경우, 포함하지 않는 경우 2가지를 계산한 후 최대값을 찾는 것이다.
# 첫번째 스티커를 포함한다면 마지막 스티커는 절대 포함할 수 없고, 포함하지 않는다면 마지막 스티커를 포함할 수도 있고 안할 수도 있다.

# 다음 식을 도출해내야 한다. max(dp[i-2] + sticker[i], dp[i-1])
# 현재 스티커를 넣을지 말지를 결정할 때, i-1까지의 합이 i를 넣는거보다 크다면 안넣는다.
