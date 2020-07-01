#백준 1074 : Z

import sys

# N개
N, r, c = map(int, sys.stdin.readline().rstrip().split(" "))

size = pow(2,N)

def go(x,y, size) :

    half = size // 2
    quad = 1

    if x == r and y == c :
        return True

    if c >= y + half :
        quad+=1
        y = y+half
    if r >= x + half :
        quad+=2
        x= x+half

    quadrants.append(quad)

    go(x,y,half)



quadrants = []
go(0,0,size)
total = 0

for quad in quadrants :

    size = size//2
    total += size * size * (quad - 1)

print(total)



# 한변의 크기가 2^15까지 나올 수 있기 때문에 모든 행렬을 탐색하면 시간초과가 된다.
# 문제에서 항상 네모 영역을 4등분해서 Z자로 탐색하는 규칙을 갖고 있다.
# 그렇다면 내가 알고자 하는 좌표가 몇사분면에 존재하는지 안다면 모든 행렬을 탐색하지 않고 몇번째 순서인지 알아낼 수 있다.
# 입력받은 행렬크기에서부터 시작해서 특정 위치를 찾을 때까지 사분면을 찾는 행위를 재귀를 통해 반복하면 된다.
