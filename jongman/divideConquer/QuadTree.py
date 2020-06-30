import sys

def makeQT(i,j,size) :

    one = matrix[i][j]
    flag = True

    for x in range(size) :
        for y in range(size) :
            if one != matrix[i+x][j+y] :
                flag = False

    if flag == True :
        return one

    else :
        half = size//2
        upperLeft = makeQT(i,j,half)
        upperRight = makeQT(i,j+half,half)
        lowerLeft = makeQT(i+half,j,half)
        lowerRight = makeQT(i+half,j+half,half)

        return "(" + upperLeft + upperRight + lowerLeft + lowerRight +")"


def decodeQT(str, i, j, size) :
    global it

    head = str[it]
    it += 1
    half = size // 2

    if head == "(" :

        decodeQT(str, i,j,half)
        decodeQT(str, i, j + half, half)
        decodeQT(str, i+half, j, half)
        decodeQT(str, i + half, j + half, half)
        it += 1 # )를 없애기 위해

    elif head == '1' or head == '0':
        for dx in range(size) :
            for dy in range(size) :
                decoded_matrix[i+dx][j+dy] = head

N = int(sys.stdin.readline().rstrip())
matrix = []

for _ in range(N) :
    matrix.append(list(sys.stdin.readline().rstrip()))


quadTree = makeQT(0,0,len(matrix))
decoded_matrix = [ [0 for _ in range(N)] for _ in range(N)]


it = 0
decodeQT(quadTree,0,0,N)

print(quadTree)

for i in range(N) :
    print(decoded_matrix[i])

