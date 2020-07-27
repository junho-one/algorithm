# 백준 11266 단절점

import sys
# N개
sys.setrecursionlimit(99999)

V, E = map(int, sys.stdin.readline().rstrip().split(" "))

graph = [[] for _ in range(V+1)]
discovered = [-1 for _ in range(V+1)]
isCutEdge = set()
candidates = set()

for _ in range(E) :
    vertex1, vertex2 = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[vertex1].append(vertex2)
    graph[vertex2].append(vertex1)
    candidates.add(vertex1)
    candidates.add(vertex2)


# here를 root로 하는 tree에서 발견된 역방향 간선으로 이어진 정점 중 가장 상위 정점의 discovered 반환
def findCutEdge(here, isRoot) :
    global cnt
    discovered[here] = cnt
    cnt += 1

    # 루트일 때를 위한 값, 루트일 때는 children 수에 영향을 받는다.
    children = []
    ret = discovered[here]

    for next in graph[here] :

        if discovered[next] == -1 :
            children.append(next)
            subtree = findCutEdge(next, False)

            # subtree에서 here보다 선조로가는 역방향 간선이 없다는 것은
            # subtree에서 나아갈 수 있는 벌텍스들의 discovered가 here보다 크다는 뜻.
            # here보다 낮은 값으로 갈 수 있어야 선조와 서브트리가 이어진 것이니까
            if not isRoot and subtree >= discovered[here] :
                # print("ADD", here)
                # isCutVertex[here] = True
                isCutEdge.add((here, next))
            # 현재 here에서 만들어진 서브트리들 중에서 가장 위로 올라갈 수 있는 수를 찾는 것
            ret = min(ret, subtree)

        # 역방향 간선들 중에 가장 위로 올라갈 수 있는 수를 찾음. (= 가장 작은 discvoered)
        else :
            ret = min(ret, discovered[next])

    if isRoot and len(children) >= 2 :
        for child in children :
            isCutEdge.add((here, child))

    return ret



for vertex in list(candidates) :
    if discovered[vertex] == -1 :
        cnt = 1
        findCutEdge(vertex,True)

isCutEdge = list(isCutEdge)
isCutEdge.sort()

print(len(isCutEdge))
for ver in isCutEdge :
    print(ver, end=" ")


# 서브트리에서 갈 수 있는 접점의 discovered가 root의 discovered보다 큰 서브트리가 하나라도 있다면 그 서브트리는 루트에 의해 단절점이 된다.
