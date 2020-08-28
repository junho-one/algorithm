# 프로그래머스 가장 먼 노드

from collections import defaultdict
from collections import deque

def solution(n, edge):

    def dijkstra(start):
        queue = deque()
        queue.append((1,0))
        costs = [float('inf')] * (n + 1)

        while queue:

            vertex, cost = queue.popleft()
            if costs[vertex] < cost:
                continue

            for next in graph[vertex]:
                next_cost = cost + 1

                if costs[next] > next_cost:
                    costs[next] = next_cost
                    queue.append((next, next_cost))

        return costs

    graph = defaultdict(list)

    for s, e in edge:
        graph[s].append(e)
        graph[e].append(s)

    costs = dijkstra(1)[2:]
    min_cost = max(costs)
    answer = 0
    for cost in costs :
        if min_cost == cost :
            answer += 1

    return answer