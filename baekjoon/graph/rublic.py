import sys
from collections import deque


def bfs(start, finish):
    queue = deque()
    start = "".join(start)
    finish = "".join(finish)

    queue.append((finish, -1))
    queue.append((start, 1))

    past[start] = (1,None,None,None,None)
    past[finish] = (-1,None,None,None,None)

    while queue:

        now, level = queue.popleft()
        if level > 0:
            next_level = level + 1
        else:
            next_level = level - 1

        next = list(now)

        for idx, func in enumerate([changeRow, changeCol], start=1):

            for i in range(4):
                for k in range(4):
                    next = func(next, i)
                    key = "".join(next)

                    if past.get(key) is None:
                        past[key] = (next_level, now, idx, i+1, k+1) # parent, i, k
                        queue.append((key, next_level))

                    else:
                        length = abs(past[key][0]) + abs(level) - 1
                        if (past[key][0] < 0 and level > 0) :
                            return now, (idx, i+1, k+1), key, length
                        elif (past[key][0] > 0 and level < 0) :
                            return key, (idx, i+1, 4-(k+1)), now, length

def changeRow(array, num):
    start = num * 4
    for i in range(4):
        array[start], array[start + i] = array[start + i], array[start]
    return array

def changeCol(array, num):
    for i in range(4):
        array[num], array[num + i * 4] = array[num + i * 4], array[num]
    return array

past = {}
square = []
for _ in range(4):
    square.extend(list(map(str, sys.stdin.readline().rstrip().split())))

finish = [str(i) for i in range(1, 17)]

mapper = {str(i):chr(64+i) for i in range(1,17)}
finish = [mapper[num] for num in finish]
square = [mapper[num] for num in square]

start,center,end,length = bfs(square, finish)

print(length)
answer = []
while past.get(start) :
    level, next, rc, i, k = past[start]
    if next is not None :
        answer.append((rc, i, k))
        # print("AP",rc,i,k)
        start = next
    else :
        break

answer = list(reversed(answer))
answer.append((center[0], center[1], center[2]))
# print("CE",center[0], center[1], center[2])
while past.get(end) :
    level, next, rc, i, k = past[end]
    if next is not None :
        answer.append((rc, i, 4-k))
        # print("BA",rc,i,4-k)
        end = next
    else :
        break

for ans in answer :
    print(ans[0], ans[1], ans[2])


# 4x4 숫자가 들어오면 숫자를 일차원 리스트로 만들고 문자열로 만들어 딕셔너리에 키로 사용하는 것이 유용하다.
# 하지만 숫자에 10, 11 같은 두자리 수가 껴있으면 string에서 리스트로 변환했을 때 위치를 찾기 힘들다.
# 모두 한자리로 만들기 위해 숫자를 영어 문자로 바꾸고 시작했다.

# changeRow와 changeCol을 통해 해당 index번째 행이나 열을 한칸씩 돌린다.
# 코드에서는 총 4번씩 돌아가 changeRow가 4*4번, changeCol이 4*4번 발생하지만 이미 나온 문자열은 queue에 들어가지 않으므로 새로 생기는 문자열은 24개(4*3 + 4*3)이다.

# 양방향 탐색을 통해 서치 횟수를 줄였다.
# BFS를 시작 문자열과 끝나는 문자열에서 각각 시작하고 level로 해당 bfs가 몇번째 도는지 기록했다. 이때 시작 문자열에서부터 시작하는 BFS에는 양수의 level, 끝나는 문자열에서 시작하면 음수의 level을 부여했다.
# 현재 BFS에서 새로 만든 문자열이 과거에 만들어졌던 문자열인지 확인한다. 만약 다른 BFS에서 만들어진 문자열을 발견한다면 시작BFS와 끝BFS를 연결하면 최단경로가 찾아진다.
# 이때 과거에 만들어졌었는지 여부에 해당하는 past 딕셔너리에 이 문자열이 어떤 문자열에서 몇번 칼럼이나 로우를 몇번 움직여서 만들어졌는지에 대한 정보를 기록해둔다.
# 두 BFS가 만난다면 past에 담아놓은 정보를 통해 최단 경로에서 사용된 연산들을 뽑아낼 수 있다.

# 이때 시작BFS에서는 만들어진 경로를 역순으로 추적해가며 정보를 뽑아내기 때문에 경로 정보를 모두 뽑아낸 후에 순서를 뒤집어줘야 한다.
# 끝BFS에서는 경로를 역순으로 뽑아내면 시작BFS입장에서는 제대로된 순서이기에 뒤집어 줄 필요가 없다.
# 하지만 끝BFS에 담겨있는 경로는 완성된 문자열을 기준으로 움직인 경로이다. 그러므로 초기 문자열의 기준으로 생각해보면 changeRow,changeCol의 수행횟수를 그대로 쓰는 것이 아닌 4에 횟수를 빼준 값을 사용해야 한다.
