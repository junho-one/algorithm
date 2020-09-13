import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

# here를 root로 하는 tree에서 발견된 역방향 간선으로 이어진 정점 중 가장 상위 정점의 order 반환
def dfs(here, cnt):
    order[here] = cnt

    children = 0
    ret = order[here]

    for next in graph[here] :
        if order[next] :
            # 역행 간선 중에서 가장 위로 올라가는 수를 찾는다.
            ret = min(ret, order[next])

        else :
            children += 1
            subtree = dfs(next, cnt+1)

            # subtree에서 here보다 선조로가는 역방향 간선이 없다는 것은
            # subtree에서 갈 수 있는 vertex들의 order이 모두 부모 order 이하라는 것
            # here보다 낮은 값으로 갈 수 있어야 선조와 서브트리가 이어진 것이니까
            if cnt != 1 and subtree >= order[here] :
                cutVertex.add(here)

            # 현재 here에서 만들어진 서브트리들 중에서 가장 위로 올라갈 수 있는 수를 찾는 것
            ret = min(subtree, ret)

    if cnt == 1 and children >= 2 :
        cutVertex.add(here)

    return ret


# N개
V,E = map(int, sys.stdin.readline().rstrip().split(" "))
graph = defaultdict(list)
cutVertex = set()
candidates = set()

for _ in range(E) :
    a,b = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[a].append(b)
    graph[b].append(a)
    candidates.add(a)
    candidates.add(b)

order = [None] * (V+1)
cnt = 1

for vertex in candidates :
    if not order[vertex] :
        dfs(vertex, 1)

print(len(cutVertex))

for vertex in sorted(list(cutVertex)) :
    print(vertex, end=" ")