import random
import sys

N = 1000
board = [ [0 for _ in range(N)] for _ in range(N) ]
dp = [ [None for _ in range(N)] for _ in range(N) ]

def jump(x,y) :

    if x >= N or y >= N :
        return False

    if x == N-1 and y == N-1 :
        return True

    if dp[x][y] :
        return dp[x][y]

    jumpSize = board[x][y]

    return jump(x+jumpSize,y) or jump(x,y+jumpSize)

for i in range(N) :
    for j in range(N) :
        board[i][j] = random.randrange(1,9)

# for i in range(N) :
#     print(board[i])

print(jump(0,0))