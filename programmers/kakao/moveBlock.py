# 프로그래머스 블록 이동하기
from collections import deque
def check_boundary(a, b, n):
    if 0 <= a[0] < n and 0 <= a[1] < n and 0 <= b[0] < n and 0 <= b[1] < n:
        return True
    return False


def solution(board):
    answer = float('inf')
    N = len(board)
    visited = []
    queue = deque()
    queue.append(([(0,0), (0,1), 0]))
    while queue:
        head, tail, level = queue.popleft()
        # print(head, tail)
        if tail == (N-1, N-1):
            answer = min(answer, level)
            # return level

        if [head,tail] in visited :
            continue

        # 움직이는 경우
        for dx,dy in [(1,0), (-1,0), (0,1), (0,-1)] :
            next_head = (head[0] + dx, head[1] + dy)
            next_tail = (tail[0] + dx, tail[1] + dy)

            if check_boundary(next_head, next_tail, N) :
                if board[next_head[0]][next_head[1]] == 0 and board[next_tail[0]][next_tail[1]] == 0:
                    queue.append([min(next_head, next_tail), max(next_head, next_tail), level + 1])


        # 각도를 바꾸는 경우
        if abs(head[0] - tail[0]) == 0:
            # ㅡ
            for dm in [(1, 0), (-1, 0)]:
                next_head = (head[0] + dm[0], head[1] + dm[1])
                next_tail = (tail[0] + dm[0], tail[1] + dm[1])

                if check_boundary(next_head, next_tail, N):
                    if board[next_head[0]][next_head[1]] == 0 and board[next_tail[0]][next_tail[1]] == 0:
                        queue.append([min(next_head, head), max(next_head, head), level + 1])
                        queue.append([min(next_tail, tail), max(next_tail, tail), level + 1])
        else:
            # |
            for dm in [(0, 1), (0, -1)]:
                next_head = (head[0] + dm[0], head[1] + dm[1])
                next_tail = (tail[0] + dm[0], tail[1] + dm[1])

                if check_boundary(next_head, next_tail, N):
                    if board[next_head[0]][next_head[1]] == 0 and board[next_tail[0]][next_tail[1]] == 0:
                        queue.append([min(next_head, head), max(next_head, head), level + 1])
                        queue.append([min(next_tail, tail), max(next_tail, tail), level + 1])

        visited.append([head,tail])

    return answer

print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))