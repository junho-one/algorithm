# 종만북

import sys

sys.setrecursionlimit(10**6)

# 1개
N = int(sys.stdin.readline().rstrip())

switch = [
    [0,1,2],
    [3,7,9,11],
    [4,10,14,15],
    [0,4,5,6,7],
    [6,7,8,10,12],
    [0,2,14,15],
    [3,14,15],
    [4,5,7,14,15],
    [1,2,3,4,5],
    [3,4,5,9,13]
]

def push_switch(num, time) :

    for _ in range(time) :
        for i in switch[num] :
            clocks[i] = ( clocks[i] + 1 ) % 4

def syncClock(now) :

    if any(clocks) == False :
        return 0

    if now == 10 :
        return float('inf')

    ret = float('inf')

    for i in range(0,4) :
        ret = min(ret, i + syncClock(now+1))
        push_switch(now, 1)
    # for문 한바퀴 다 돌면 다시 clocks 상태가 원상복구되니까 clocks를 다시 되돌릴 필요는 없는 듯


    return ret

for _ in range(N) :

    clocks = list(map(int,sys.stdin.readline().rstrip().split()))
    clocks = [ i//3 % 4 for i in clocks ]

    dp = [None for _ in range(len(clocks))]

    ans = syncClock(0)

    if ans == float('inf') :
        print('-1')
    else :
        print(ans)

