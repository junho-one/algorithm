# 백준 1099 알 수 없는 문장

import sys
from collections import Counter

hyungtaek = sys.stdin.readline().rstrip()

N = int(sys.stdin.readline().rstrip())
strings = []
for _ in range(N):
    strings.append(sys.stdin.readline().rstrip())

dp = [None] * (len(hyungtaek)+1)
cands = []

INF = 987654321
def go(idx):
    if idx == len(hyungtaek):
        return 0

    if dp[idx] is not None :
        return dp[idx]
    ret = INF
    for string in strings :
        slen = len(string)

        if  Counter(hyungtaek[idx:idx+slen]) == Counter(string) :
            cnt = 0
            for i in range(slen) :
                if hyungtaek[idx+i] != string[i] :
                    cnt += 1
            ret = min(ret, go(idx+slen)+cnt)

    dp[idx] = ret
    return ret

go(0)
if dp[0] is not INF:
    print(dp[0])
else :
    print("-1")


# if dp[idx] :
#    return dp[idx]   형식으로 짜면 dp 값이 0 일 때는 이 조건문에 안걸리기에 에러난다. is not None으로 하자
