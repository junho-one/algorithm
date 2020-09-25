# # 백준 1261 알고스팟

# 1. 힙 이용. (다익처럼)
import sys
import heapq

M, N = map(int, sys.stdin.readline().rstrip().split(" "))

matrix = []

for _ in range(N) :
    matrix.append(list(map(int, list(sys.stdin.readline().rstrip()))))


dist = [ [ float("inf") for _ in range(M)] for _ in range(N)]
dist[0][0] = 0

heap = []
heap.append([0,0,0])
answer = float("inf")

while heap :

    level,x,y = heapq.heappop(heap)

    if (x,y) == (N-1,M-1) :
        answer = level
        break

    for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)] :
        matrix[x][y] = -1
        nx = x+dx
        ny = y+dy

        if 0 <= nx < N and 0<= ny < M and dist[nx][ny] == float("inf") :
            if matrix[nx][ny] == 0 :
                heapq.heappush(heap, [level,nx,ny])
            else :
                heapq.heappush(heap, [level+1,nx,ny])

            dist[nx][ny] = 1

print(answer)

# 이 문제를 시간 안에 풀기 위해 중요한 점.
# 최소 비용을 구하는 것이기에 가능한 경우의 수 중 최소 비용인 경우로 먼저 탐색하게 만든다.
# 최소 비용이 지나간 위치는 갈 필요가 없고, 도착지점에 도착하면 바로 끝내 불필요한 연산을 없앤다.
# 이를 위해 dist와 heap

# 2. 큐를 이용

# import sys
# from collections import deque
#
# M, N = map(int, sys.stdin.readline().rstrip().split(" "))
#
# matrix = []
#
# for _ in range(N) :
#     matrix.append(list(map(int, list(sys.stdin.readline().rstrip()))))
#
# start = [0,0]
# end = (N-1,M-1)
#
# dist = [ [ -1 for _ in range(M)] for _ in range(N)]
# dist[0][0] = 0
#
# queue =deque()
# queue.append(start)
# answer = float("inf")
# while queue :
#
#     x,y = queue.popleft()
#
#     for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)] :
#         nx = x+dx
#         ny = y+dy
#
#         if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1 :
#
#             if matrix[nx][ny] == 0 :
#                 queue.appendleft([nx,ny])
#                 dist[nx][ny] = dist[x][y]
#
#             elif matrix[nx][ny] == 1 :
#                 queue.append([nx,ny])
#                 dist[nx][ny] = dist[x][y] + 1
#
# print(dist[N-1][M-1])



# 벽을 뚫지 않는 경우는 queue에 왼쪽에 넣기에 항상 벽 뚫는 경우보다 먼저 queue에서 나오게 된다.
# 벽을 안뚫는 경우를 모두 탐색하면 그 후에 뚫는 경우를 탐색하게 된다. 이때는 cost + 1
# 그리고 뚫은 다음, 안뚫고 갈 수 있는 곳 먼저 탐색.

# 최소 접근 횟수면 queue에서 먼저 나와 처음 도착하는 경우 빼고는 고려할 필요가 없다.
# 그게 젤 빠른 거니까 (여기선 cost가 적은 거니까)

