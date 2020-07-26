import sys
from collections import defaultdict


def dfs(vertex):
    global flag
    visited[vertex] = False

    adjacent = graph[vertex]

    for node in adjacent:
        if visited[node] is False:
            flag = False

        elif visited[node] is None:
            dfs(node)

    sequence.append(vertex)
    visited[vertex] = True


T = int(sys.stdin.readline().rstrip())

for _ in range(T):

    graph = defaultdict(set)
    N = int(sys.stdin.readline().rstrip())
    words = []
    visited = {}
    for _ in range(N):
        words.append(sys.stdin.readline().rstrip())

    # make graph
    prev = ""
    for word in words:

        for i in range(min(len(prev), len(word))):
            if prev[i] != word[i]:
                graph[prev[i]].add(word[i])
                visited[prev[i]] = None
                visited[word[i]] = None
                break

        prev = word

    # dfs all
    answer = []
    for vertex in visited.keys():
        if visited[vertex] is None:
            sequence = []
            flag = True

            dfs(vertex)

            if flag:
                answer.extend(sequence)
            else:
                break

    if flag:
        alphabet = [a if a not in answer else "" for a in "abcdefghijklmnopqrstuvwxyz"]
        answer.reverse()
        answer = "".join(answer +alphabet)
        print(answer)
    else:
        print("INVALID HYPOTHESIS")


# dfs를 이용해 위상정렬로 풀 수 있는 문제이다.
# 주의해야할 점은 dfs로 그래프를 탐색하면서 cycle의 존재 유무를 파악해줘야한다.
# 그러기 위해서 dfs가 방문한 순간에 visited를 True가 아닌 False로 해놓고 dfs가 끝나는 순간 True로 해준다.
# 그러면 노드가 인접 노드로 dfs 재귀호출을 할 때 visited가 False라면
# 아직 종료되지 않은 노드를 접근하려 한 것이니 사이클이 존재하는 것을 알 수 있다.
# flag를 통해 사이클 유무를 판단하고 종료시켰다.

# 이 부분만 잘 체크하면 위상정렬만 해주고 나머지 알파벳을 넣으면 문제가 해결된다.