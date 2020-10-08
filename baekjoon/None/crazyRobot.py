# 백준 1405 미친 로봇
import copy
import sys
Num, E,W,S,N = map(int, sys.stdin.readline().rstrip().split())

E = E/100
W = W/100
S = S/100
N = N/100

matrix = [[False for _ in range(30)] for _ in range(30)]

def go(loc, n) :

    if n == 0 :
        return 1

    x,y = loc

    prob = 0
    for dx, dy, p in [(1,0,E),(-1,0,W),(0,1,N),(0,-1,S)] :
        nx = x+dx
        ny = y+dy
        if matrix[nx][ny] is False :
            matrix[nx][ny] = True
            prob += (go((nx,ny), n-1)) * p
            matrix[nx][ny] = False

    return prob

matrix[0][0] = True
print(go((0,0), Num))

# matrix를 사용하나 set을 사용하나 대충 시간복잡도가 1이니까 비슷한 속도가 나오나 ?

# # 백준 1405 미친 로봇
# import copy
# import sys
# Num, E,W,S,N = map(int, sys.stdin.readline().rstrip().split())
#
# E = E/100
# W = W/100
# S = S/100
# N = N/100
#
# def go(loc, n) :
#     if n == 0 :
#         return 1
#
#     x,y = loc
#
#     prob = 0
#     for dx, dy, p in [(1,0,E),(-1,0,W),(0,1,N),(0,-1,S)] :
#         nx = x+dx
#         ny = y+dy
#         if (nx,ny) not in visited :
#             visited.add((nx,ny))
#             prob += (go((nx,ny), n-1)) * p
#             visited.remove((nx,ny))
#
#
#     return prob
#
# visited = set()
# visited.add((0,0))
# print(go((0,0), Num))
