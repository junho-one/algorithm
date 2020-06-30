import sys

# 1개
N = int(sys.stdin.readline().rstrip())
move = [[(0,0),(0,1),(1,0)], [(0,0),(0,1),(1,1)], [(0,0),(1,0),(1,1)], [(0,0),(1,0),(1,-1)]]


def firstEmpty() :
    for x in range(H) :
        for y in range(W) :
            if matrix[x][y] == '.' :
                return x,y

    return -1,-1

def checkBlock(x,y,num) :

    for dx,dy in move[num] :

        nx = x+dx
        ny = y+dy

        if not (0 <= nx < H and 0 <= ny < W) :
            return False

        if matrix[nx][ny] == '#' :
            return False

    return True

def fillBlock(x,y,num) :

    for dx,dy in move[num] :
        nx = x+dx
        ny = y+dy
        matrix[nx][ny] = '#'

def removeBlock(x,y,num) :

    for dx, dy in move[num]:
        nx = x + dx
        ny = y + dy
        matrix[nx][ny] = '.'


def countBlock() :

    x,y = firstEmpty()

    if  x is -1 and y is -1 :
        return 1

    ret = 0

    for m in range(len(move)) :
        if checkBlock(x,y,m) :
            fillBlock(x,y,m)
            ret += countBlock()
            removeBlock(x,y,m)

    return ret

for _ in range(N) :

    H,W = map(int, sys.stdin.readline().rstrip().split(" "))
    matrix = []

    for _ in range(H) :
        matrix.append(list(sys.stdin.readline().rstrip()))

    emptyCount =  0
    for row in range(H) :
        for col in range(W) :
            if matrix[row][col] == '.' :
                emptyCount+=1

    if emptyCount % 3 == 0 :
        print(countBlock())

    else :
        print("No")


# HxW 크기의 게임판이 주어진다. 게임판은 흰 칸과 검은 칸으로 구성된 격자 모양을 하고 있다.
# 세 칸짜리 L자 모양의 블록을 이용해 게임판의 흰 영역을 모두 블록으로 덮고 싶다.
# 이때 L자 블록은 마음대로 회전해서 놓을 수 있지만, 서로 겹치거나, 검은 칸을 덮거나, 밖으로 나가서는 안된다.
# 게임판이 주어질 때 이를 덮는 방법의 수를 계산하시오

# 이 문제는 subproblem으로 쪼개진다.
# 현재 problem인 빈 공간을 채우는 문제는 적절한 영역에 한 블록이 들어가고, 남은 빈 공간을 채우라는 문제로 쪼개질 수 있다.
# 즉 6개의 블록을 채워야하는 문제 -> 5개의 블록을 채워야하는 문제 로 쪼개지는 것이다.
# 이때 baseline은 board가 모두 검정으로 찬 경우이다.

# 문제가 쪼개지는 것을 확인했으니 블록을 채우는 방법을 생각하면 된다.
# ㄴ 모양 블록이 하나의 빈 공간을 채우는 방법은 12가지가 있다. ㄴ 블록의 회전과 배치가 다양하기에 가능하다.
# 하지만 빈 공간 중 항상 좌측 상단에 존재하는 빈 공간을 먼저 채운다고 가정하면 경우의 수는 4가지로 줄어든다.
# 가장 좌측 상단에 있는 공간은 항상 항상 왼쪽과 위쪽이 검정 칸으로 차있거나 게임판 밖이기 때문이다.

# 항상 좌측 상단의 빈 공간을 찾기위해 firstEmpty함수를 사용한다.
# 이 함수는 이차원 배열을 모두 탐색하면서 가장 처음 빈 공간이 나오는 위치를 반환한다
# 만약 빈 공간이 없다면 baseline에 도달한 것을 의미하므로 재귀를 종료한다.

# 처음으로 나타나는 빈 공간을 찾았으니 빈 공간을 채우기 위해 서로 겹치거나, 검은 칸을 덮거나, 밖으로 나가는지를 체크해야 한다.
# 이를 위해 checkBlock 함수를 사용한다. 모든 상황에서 맞다면 True를 반환하고, 하나라도 걸리는 게 있다면 False를 반환한다.

# checkBlock이 True를 반환한다면 fillBlock을 사용해 L 블록으로 덮어주고, 다시 재귀를 호출한다.
# 재귀함수 밑에는 removeBlock을 이용해 위에서 덮은 L블록을 지워준다. 이렇게 matrix가 재귀를 돌면서 혼용되지 않도록 방지한다.




# 초기 접근 방식
# 처음에는 하나의 빈 공간을 채우는 ㄴ 모양 블록의 가짓수가 12가지라고 생각하여 시간초과가 날 것이라고 생각했다.

# 오답의 원인
# 순서를 강제함으로써 중복제거 + 가짓수 축소

# 순서가 바뀌는 경우도 모두 세기에 순서를 강제해야 한다.
# 여기서는 맨처음 왼쪽 위가 빈 곳을 먼저 채워 넣는 식으로 처리한다.

# 처음에는 하나의 빈 공간을 채우는 ㄴ 모양의 블록의 경우의 수는 원래 12가지라고 생각했지만
# 왼쪽 위로 고정하는 순간 빈 공간을 채우는 가짓수는 4개로 줄어듬. 왼쪽과 위쪽이 항상 차있기 때문에 왼쪽과 위쪽으로 나아가는 방향을 블록은 제외 가능

# 왼쪽 위로 순서를 강제하지 않으니 블록이 들어가야하는 가짓수가 너무 많아짐. 또한 중복처리도 안됨
