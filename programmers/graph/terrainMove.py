# 프로그래머스 지형이동
from collections import deque, defaultdict
import heapq

def solution(land, height):
    N = len(land)
    matrix = [[None for _ in range(N)] for _ in range(N)]
    for i in range(N) :
        for j in range(N) :
            matrix[i][j] = [land[i][j],None]


    def bfs(start, num) :
        queue = deque()
        x,y = start
        queue.append((x,y))
        matrix[x][y][1] = num

        neighbors = defaultdict(lambda:float("inf"))
        while queue :
            x,y = queue.popleft()
            for dx, dy in [(0,1),(0,-1),(1,0),(-1,0)] :
                nx = x+dx
                ny = y+dy

                if 0<=nx<N and 0<=ny<N :

                    if matrix[nx][ny][1] != matrix[x][y][1]:
                        neighbors[matrix[nx][ny][1]] = min(neighbors[matrix[nx][ny][1]], abs(matrix[x][y][0] - matrix[nx][ny][0]))

                    if matrix[nx][ny][1] == None and abs(matrix[x][y][0] - matrix[nx][ny][0]) <= height :
                        matrix[nx][ny][1] = num
                        queue.append((nx,ny))

        return neighbors


    num = 0
    graph = {}
    for i in range(N) :
        for j in range(N) :
            if matrix[i][j][1] == None :
                graph[num] = bfs((i,j),num)
                num += 1

    edges = []
    for key1 in graph.keys() :
        for key2 in graph[key1].keys():
            if key1 != None and key2 != None :
                edges.append( (graph[key1][key2], key1, key2) )

    height = {}
    parent = {}
    for i in range(num) :
        parent[i] = i
        height[i] = 0

    def find(n) :
        # print(n)
        while n != parent[n] :
            n = parent[n]
        # print("BF",n)
        return n

    def union(a,b) :
        root_a = find(a)
        root_b = find(b)

        if height[root_a] > height[root_b] :
            parent[root_b] = root_a
        else :
            parent[root_a] = root_b
            if height[root_a] == height[root_b] :
                height[root_b] += 1


    answer = 0
    edges.sort()
    # print(edges)
    for cost, x, y in edges :
        if find(x) != find(y) :
            union(x,y)
            answer += cost
# 크루스칼

    return answer