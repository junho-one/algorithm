# # 백준 1477 : 휴게소 세우기

import sys
N,M,L = map(int, sys.stdin.readline().rstrip().split())

road = list(map(int, sys.stdin.readline().rstrip().split()))
road.sort()
road.append(L)

intervals = []

prev = 0
for ra in road :
    intervals.append( ra - prev )
    prev = ra

intervals.sort(reverse=True)

left = 0
right = 1000

while left <= right :

    if left == right :
        mid = left
        break

    mid = (left+right)//2
    possible = M
    flag = True
    for val in intervals :
        if val > mid :
            cnt = val // mid
            if val % mid == 0 :
                cnt -= 1

            possible -= cnt
        if possible < 0 :
            flag = False
            break

    if flag == True :
        right = mid

    else :
        left = mid+1

print(mid)
