# 프로그래머스 게임 맵 최단거리

from collections import deque

def solution(maps):

    def bfs(start, end):
        queue = deque()
        queue.append([start[0], start[1], 1])

        while queue:
            x, y, level = queue.popleft()

            if (x, y) == end:
                return level

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nx = x + dx
                ny = y + dy

                if 0 <= nx < row and 0 <= ny < col and maps[nx][ny] == 1:
                    maps[nx][ny] = level + 1
                    queue.append([nx, ny, level + 1])

        return - 1

    row = len(maps)
    col = len(maps[0])

    return bfs((0, 0), (row - 1, col - 1))