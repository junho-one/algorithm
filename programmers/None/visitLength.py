# 프로그래머스 방문길이

def convertToXY(d):
    if d == 'U':
        return -1, 0
    elif d == 'L':
        return 0, -1
    elif d == 'R':
        return 0, 1
    else:
        return 1, 0


def solution(dirs):
    answer = 0

    matrix = [[None for _ in range(11)] for _ in range(11)]
    x, y = 5, 5

    answer = set()
    for direction in dirs:

        dx, dy = convertToXY(direction)

        nx = x + dx
        ny = y + dy

        if 0 <= nx < 11 and 0 <= ny < 11:
            answer.add((x, y, nx, ny))
            answer.add((nx, ny, x, y))
            x = nx
            y = ny

    return len(answer) // 2

print(solution("ULURRDLLU"))

# dirs이 500밖에 안되기 때문에 경로를 모두 저장해도 시간 안에 풀 수 있다.
# (1,4)->(2,4) 와 (2,4)->(1,4)는 같은 경로기 때문에 한번 움직일 때 둘 다 고려해줘야 한다.
# (이동 전 위치, 이동 후 위치), (이동 후 위치, 이동 전 위치)로 모든 움직인 경로를 집합에 넣고 길이를 구하면 된다.

