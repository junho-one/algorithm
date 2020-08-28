# 등굣길

# 밑에 코드는 되는데 이게 안되는 이유를 모르겠다.
# 물웅덩이를 미리 0으로 해놓고 0이면 패스하는 코드로는 왜 안되지?

# 1,1에서 오른쪽 아래로는 모두 순서대로 방문하기에
# 0 인 경우는 웅덩이인 경우밖에 없다고 생각햇는데 다른 경우가 잇는듯

def solution(m, n, puddles):

    # m이 열을 의미, n이 행을 의미

    matrix = [[None for _ in range(n+1)] for _ in range(m+1)]

    for i in range(m+1) :
        matrix[i][1] = 1

    for j in range(n+1) :
        matrix[1][j] = 1

    for r, c in puddles:
        matrix[r][c] = 0


    for i in range(2,m+1) :
        for j in range(2,n+1) :

            if matrix[i][j] == 0:
                continue
            else :
                matrix[i][j] = (matrix[i][j-1] + matrix[i-1][j]) % 1000000007


    return matrix[m][n] % 1000000007


print(solution(7,5,[[4, 3],[4,5]]))

# bfs에서 최단거리 찾기는 항상 가야하는 길이 방문했던 장소라면 최단거리가 중복되거나 될 수 없지만
# 여기서는 갯수를 찾아야하니까 모두 가야함.

# 이건 되는 코드
# 웅덩이 문제를 유념하자... 이렇게 풀자 그냥 씨빨..
def solution(m,n,puddles) :

    matrix = [[0] * (m + 1) for _ in range(n + 1)]  # 전체 지도를 만든다. 일단 방문한 적이 없으므로 모두 0을 준다.
    matrix[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                matrix[i][j] = 0
            else :
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]

    answer = matrix[n][m]
    return answer % 1000000007





