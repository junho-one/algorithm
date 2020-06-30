import sys

N, B = map(int, sys.stdin.readline().rstrip().split(" "))

matrix = []

for _ in range(N) :
    matrix.append(list(map(int,sys.stdin.readline().rstrip().split())))


def matrix_multiply(matrix, matrixB) :

    matrixT = [list(x) for x in zip(*matrixB)]

    result =  [ [ 0 for _ in range(N) ] for _ in range(N) ]

    for i in range(N) :
        for j in range(N) :
            result[i][j] = sum([a*b for a,b in zip(matrix[i],matrixT[j])]) % 1000

    return result

def matrix_power( matrix, n ) :
    if n == 1 :
        return matrix

    if n%2 != 0 :
        return matrix_multiply( matrix_power(matrix, n-1), matrix )

    half = matrix_power(matrix, n//2)

    return matrix_multiply(half,  half)


answer = matrix_power(matrix,B)

for i in range(len(answer)) :
    for j in range(len(answer[i])) :
        print(answer[i][j]%1000, end = " ")
    print("")