# 백준 1783 병든나이트

import sys

# N개
N, M = map(int, sys.stdin.readline().rstrip().split(" "))

keyToDeriv = {1:(-2,1), 2:(-1,2), 3:(1,2), 4:(2,1)}

flag = False
def allPath(x,y,path) :
    global flag
    if len(path) == 4 :
        if len(set(path)) == 4 :
            flag = True
        return len(path)

    ret = len(path)
    for i in range(1,5) :
        dx, dy = keyToDeriv[i]

        if 0 <= x+dx < N and 0 <= y+dy < M :
            ret = max(ret, allPath(x+dx,y+dy,path+[i])) # 이렇게 넣으니까 path를 참조하는게 아니라 새로운 리스트로 들어간다!!

    return ret

max_path_cnt = allPath(N-1,0,[])

if flag :
    ans = M-2

else :
    ans = min(4, max_path_cnt+1)
    # flag가 False면 최대 4임. path 에 4가 있어도

print(ans)


# 만약 나이트가 4가지 경우로 모두 갈 수 있다면 이 나이트의 최대 이동 수는 가로길이 -2가 된다.
# (위로2칸,오른쪽1칸) (아래로2칸,오른쪽1칸)을 쓰면 한칸씩 이동할 수있고 최대 횟수가 된다.
# 그런데 방문 수가 5개 이상이 되려면 4가지 방향으로 한번씩은 가야하니까 오른쪽으로 2칸 이동이 2번은 나올 수 밖에 없다. 그 두번을 마이너스 해주는 것

# 그렇다면 4가지 행동이 한번씩 나올 수 있을 만큼 체스판이 크다면 방문 수는 가로길이에 비례하게 된다.
# 4가지 행동이 나오는 안나오는지는 경우의 수가 적기 때문에 완전탐색으로 해결 가능하다.
# 이때 방문 수가 4이하라면 경로 선택에는 제약이 없다. 4가지 행동이 나올 수 없는 체스판이라면 4이하인 방문수의 최대값을 쓰면 된다.

