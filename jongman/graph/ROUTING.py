import sys
from collections import defaultdict, deque
import heapq

def dijkstra_pq(start) :
    dist = [float("inf")] * N
    dist[start] = 1
    queue = []
    heapq.heappush(queue, (1,start))

    while queue :
        cost, vertex = heapq.heappop(queue) # cost는 이 vertex까지 오는 최소비용

        if dist[vertex] < cost :
            continue

        for next_vertex, next_cost in graph[vertex] :

            next_dist = next_cost * cost

            if dist[next_vertex] > next_dist :
                dist[next_vertex] = next_dist
                heapq.heappush(queue, (next_dist, next_vertex) )

    return dist

def dijkstra_no_pq(start) :

    visited = [None] * N
    dist = [float('inf')] * N
    dist[start] = 1

    while True :

        closest = float("inf")
        for idx in range(N) :
            if not visited[idx] and dist[idx] < closest :
                here = idx
                closest = dist[idx]

        if closest == float("inf") :
            break

        visited[here] = True
        for next_vertex, next_cost in graph[here] :

            if visited[next_vertex] :
                continue

            next_dist = dist[here] * next_cost
            dist[next_vertex] = min(dist[next_vertex], next_dist)

    return dist


T = int(sys.stdin.readline().rstrip())

for _ in range(T) :

    N, M = map(int, sys.stdin.readline().rstrip().split(" "))

    graph = defaultdict(list)
    for _ in range(M) :
        a, b, c = map(float, sys.stdin.readline().rstrip().split(" "))
        a = int(a)
        b = int(b)
        graph[a].append((b, c))
        graph[b].append((a, c))

    distance = dijkstra_pq(0)
    print(distance)
    print(distance[-1])


    # distance = dijkstra_no_pq(0)
    # print(distance)
    # print(distance[-1])