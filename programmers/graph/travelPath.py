# 여행 경로

# 오일러 서킷, 오일러 트레일을 찾는 문제이다.
# 시작점이 ICN으로 고정이니까 그냥 오일러 서킷을 찾는 코드를 짠 뒤 ICN으로 시작하면 된다.

from collections import defaultdict

def solution(tickets):
    def go(vertex):

        while graph[vertex]:
            next = graph[vertex].pop()
            go(next)

        answer.append(vertex)

    graph = defaultdict(list)
    answer = []

    for start, end in tickets:
        graph[start].append(end)

    for key, val in graph.items():
        val.sort(reverse=True)

    go("ICN")
    return list(reversed(answer))