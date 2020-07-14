import sys

def LCA(a,b) :

    if a==b :
        return 0

    a_cnt = 0
    b_cnt = 0
    visited = [None for _ in range(N)]
    turn = True

    while a or b :
        if visited[a] :
            return visited[a] + a_cnt
        if visited[b] :
            return visited[b] + b_cnt

        if a and (turn or not b):
            visited[a] = a_cnt
            a = fathers[a]
            a_cnt += 1

        else :
            visited[b] = b_cnt
            b = fathers[b]
            b_cnt += 1

        turn = not turn

    return a_cnt + b_cnt

T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    N, Q = map(int, sys.stdin.readline().rstrip().split(" "))
    fathers = list(map(int, sys.stdin.readline().rstrip().split()))
    fathers.insert(0,None)
    paths = []
    for _ in range(Q) :
        a,b = map(int, sys.stdin.readline().rstrip().split(" "))
        paths.append((a,b))

    for a,b in paths :
        print(LCA(a,b))


# 시간초과, 트리의 최대 높이가 N/2이 되고, 양쪽 끝에서의 공통조상을 찾는 문제가 나온다면 시간초과일 듯
