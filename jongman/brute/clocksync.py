# 종만북

import sys

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

def return_switch(num, time) :

    for _ in range(time) :
        for i in switch[num] :
            clocks[i] = clocks[i] - 1
            if clocks[i] == -1 :
                clocks[i] = 3

def syncClock(now) :

    if any(clocks) == False :
        return 0

    if now == 10 :
        return float('inf')

    ret = float('inf')

    # for i in range(0,4) :
    #     push_switch(now, i)
    #     ret = min(ret, i + syncClock(now+1))
    #     return_switch(now,i)


    for i in range(0,4) :
        ret = min(ret, 1 + syncClock(now+1))
        push_switch(now, 1)
        # return_switch(now,i)


    return ret

for _ in range(N) :

    clocks = list(map(int,sys.stdin.readline().rstrip().split()))
    clocks = [ i//3 % 4 for i in clocks ]

    # print(clocks)
    print(syncClock(0))


# 1
# 12 6 6 6 6 6 12 12 12 12 12 12 12 12 12 12
