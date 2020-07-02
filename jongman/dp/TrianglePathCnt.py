import sys

# 1개
T = int(sys.stdin.readline().rstrip())

def trianglePath(x,y) :

    if x == N-1 :
        dp[x][y] = matrix[x][y]
        return dp[x][y]

    if dp[x][y] :
        return dp[x][y]

    ret = max(trianglePath(x+1,y), trianglePath(x+1,y+1)) + matrix[x][y]

    dp[x][y] = ret
    return dp[x][y]


def trianglePathCNT(x,y) :

    if x == N-1 :
        return 1

    if dp2[x][y] :
        return dp2[x][y]

    left = dp[x+1][y]
    right = dp[x+1][y+1]

    ret = 0
    if left >= right :
        ret += trianglePathCNT(x+1,y)

    if right >= left :
        ret += trianglePathCNT(x+1,y+1)

    dp2[x][y] = ret

    return dp2[x][y]

for _ in range(T) :

    N = int(sys.stdin.readline().rstrip())
    matrix = []

    dp = [ [None for _ in range(N)] for _ in range(N)]
    dp2 = [[None for _ in range(N)] for _ in range(N)]

    for _ in range(N) :
        matrix.append(list(map(int,sys.stdin.readline().rstrip().split())))

    trianglePath(0,0)
    # for i in range(N) :
    #     print(dp[i])

    print(trianglePathCNT(0,0))


# 최대 합의 경로를 찾으려면 인덱스마다 구해 놓은 최대합이 있으면 찾기 수월하다.
# 만약 (0,0) 위치에서의 최대합의 경로는 (1,0)에서 왔거나 (1,1)에서 왔거나 이다
# 그런데 (1,0)에서의 최대합이 (1,1) 보다 크다면 (1,1)에서 온 경로는 최대합이 될 수 없다.
# 만약 (1,0)과 (1,1)에서의 최대합이 같다면 두 경로 모두 쓰일 수 있다.
# 이렇게 반복해서 맨 마지막까지 내려가면 된다.

# 이 가정을 이용해 점화식을 세우면 된다.


