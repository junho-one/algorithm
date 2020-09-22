import sys
from collections import defaultdict

def go(weight, item_num) :

    if dp[weight][item_num] :
        return dp[weight][item_num]

    if item_num == N and weight >= 0 :
        return 0

    now = item[item_num]

    ret = go(weight, item_num + 1)

    if weight - now[0] >= 0 :
        ret = max(ret, go(weight - now[0], item_num + 1) + now[1])

    dp[weight][item_num] = ret
    return ret

def reconstruct(weight, item_num, picked) :

    if item_num == N :
        return

    if go(weight, item_num) == go(weight, item_num+1) :
        reconstruct(weight, item_num + 1, picked)
    else :
        picked.append(item_num)
        reconstruct(weight - item[item_num][0], item_num+1, picked)

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    N, W = map(int, sys.stdin.readline().rstrip().split(" "))

    num = {}
    item = []
    for i in range(N) :
        a,b,c = sys.stdin.readline().rstrip().split(" ")
        num[i] = a
        item.append([int(b), int(c)])

    dp = [ [None for _ in range(N+1)] for _ in range(W+1)]

    total_weight = go(W,0)

    answer = []
    reconstruct(W,0,answer)
    print(total_weight, len(answer))
    for ans in answer :
        print(num[ans])