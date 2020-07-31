# 카카오 여름인턴 4번

from collections import deque
import heapq
def solution(board):

    def bfs() :
        start = (0,0)
        end = (N-1,N-1)

        for x in range(N) :
            for y in range(N) :
                if board[x][y] == 0 :
                    board[x][y] = float('inf')

        queue = deque()
        queue.append((0,(0,0),(0,0)))
        # board[0][0] = 1

        while queue :

            cost, now, prev = queue.popleft()

            now_x = now[0]
            now_y = now[1]
            prev_x = prev[0]
            prev_y = prev[1]

            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)] :
                next_x = now_x+dx
                next_y = now_y+dy

                if 0 <= next_x < N and 0 <= next_y < N and board[next_x][next_y] != 1:
                    next_cost = cost + 100

                    if abs(next_x-prev_x) == 1 and abs(next_y-prev_y) == 1:
                        next_cost += 500

                    if next_cost <= board[next_x][next_y] :
                        queue.append( (next_cost, (next_x,next_y), now) )
                        board[next_x][next_y] = next_cost

                    # board[next_x][next_y] = 1
        return board[N-1][N-1]

    N = len(board)
    return bfs()


print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]))