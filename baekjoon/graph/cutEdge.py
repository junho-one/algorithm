import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

# here를 root로 하는 tree에서 발견된 역방향 간선으로 이어진 정점 중 가장 상위 정점의 order 반환
def dfs(here, parent):
	global cnt
	cnt += 1
	order[here] = cnt
	ret = order[here]

	for next in graph[here] :
		# 이부분을 next is parent로 하면 틀린 답이 나온다.
		# is 연산자는 같은 값을 갖더라도 오브젝트가 다르면 False
		# 같은 값을 참조하는지 여부에 따라 True/Falsed인듯?
		# list1=[1,2] list2=[1,2] 여도 list1 is list2는 False이다.
		if next == parent :
			continue

		if order[next] :
			ret = min(ret, order[next])
			continue

		subtree = dfs(next, here)
		ret = min(subtree, ret)

		# 부모로 바로가는 간선(현재간선)을 제외하고 서브트리의 간선 중 부모보다 선조로 갈 수 없으면
		if subtree > order[here] :
			cutEdge.add(tuple(sorted([here,next])))

	return ret


# N개
V,E = map(int, sys.stdin.readline().rstrip().split(" "))
graph = defaultdict(set)
cutEdge = set()
candidates = set()

for _ in range(E) :
    a,b = map(int, sys.stdin.readline().rstrip().split(" "))
    graph[a].add(b)
    graph[b].add(a)
    candidates.add(a)
    candidates.add(b)

order = [None] * (V+1)
cnt = 0
idx =0
for vertex in candidates :
    if not order[vertex] :
        dfs(vertex,  None)


print(len(cutEdge))
cutEdge = sorted(cutEdge, key=lambda x : (x[0],x[1]))

for a,b in cutEdge :
    print(a,b)