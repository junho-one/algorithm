import sys

# 1개
N = int(sys.stdin.readline().rstrip())
matrix = []
for _ in range(N) :
    matrix.append(list(map(int,sys.stdin.readline().rstrip().split())))

count = {}
count[0] = 0
count[1] = 0
count[-1] = 0


def checkAll(x,y,size) :
    first = matrix[x][y]
    for dx in range(size) :
        for dy in range(size) :
            if first != matrix[x+dx][y+dy] :
                return False
    return True

def go(x,y,size) :

    if checkAll(x,y,size) :
        count[matrix[x][y]] += 1
        return True

    triple = size//3

    go(x,y,triple)
    go(x+triple,y,triple)
    go(x+2*triple,y,triple)
    go(x,y+triple,triple)
    go(x+triple,y+triple,triple)
    go(x+triple*2,y+triple,triple)
    go(x,y+triple*2,triple)
    go(x+triple,y+triple*2,triple)
    go(x+triple*2,y+triple*2,triple)

go(0,0,N)
print(count[-1])
print(count[0])
print(count[1])


# 한변의 크기는 최대 3^7이다.
# 재귀를 한번 돌때마다 9개의 부분문제로 쪼개진다.
# 이때 한번의 재귀 마다 한변의 길이는 3으로 나눠진다. 최대 3^7이니 재귀가 도는 최대 횟수는 7번이다.
# 그러면 최대 연산량은 9^7이 되고 1억보다 작으니 2초안에 돌 수 있다.

# 현재 문제가 해결할 수 없다면 9개의 부분문제로 쪼개고 부분 문제를 해결한 뒤 합쳐 현재 문제를 해결해 나간다.
# 만약 현재 종이가 같은 수로 채워져 있다면 해당 숫자의 카운트를 1을 해주고 현재 재귀를 끝낸다.
# 하지만 같은 수로 채워져 있지 않다면 9개의 문제로 분할한 뒤 위의 행위를 반복한다.
