import sys

# 1개
T = int(sys.stdin.readline().rstrip())

def trianglePath(x,y) :

    if x == N-1 :
        return matrix[x][y]

    if dp[x][y] :
        return dp[x][y]

    ret = max(trianglePath(x+1,y), trianglePath(x+1,y+1)) + matrix[x][y]

    dp[x][y] = ret
    return dp[x][y]


for _ in range(T) :

    N = int(sys.stdin.readline().rstrip())
    matrix = []

    dp = [ [None for _ in range(N)] for _ in range(N)]

    for _ in range(N) :
        matrix.append(list(map(int,sys.stdin.readline().rstrip().split())))

    print(trianglePath(0,0))
