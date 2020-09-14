import sys
from collections import defaultdict
import heapq

T = int(sys.stdin.readline().rstrip())

def dijkstra(fires, stations) :
    pq = []
    start = stations[0]
    heapq.heappush(pq, (start,0))

    dist = [float('inf')] * (V+1)
    dist[start] = 0

    isStation = [False] * (V+1)
    for station in stations :
        isStation[station] = True

    isFire = [False] * (V+1)
    for fire in fires :
        isFire[fire] = True


    while pq :

        here, cost = heapq.heappop(pq)

        if dist[here] < cost :
            continue

        for next, next_cost in graph[here] :
            if isStation[next] :
                if dist[next] != 0 :
                    dist[next] = 0
                    heapq.heappush(pq, (next, 0))

            else :
                next_dist = next_cost + dist[here]
                if dist[next] > next_dist:
                    dist[next] = next_dist
                    heapq.heappush(pq, (next, next_dist))

    return dist


for _ in range(T) :
    V, E, N, M = map(int, sys.stdin.readline().rstrip().split(" "))

    graph = defaultdict(list)
    for _ in range(E) :
        a,b,t = map(int, sys.stdin.readline().rstrip().split(" "))
        graph[a].append((b, t))
        graph[b].append((a, t))

    fires = list(map(int,sys.stdin.readline().rstrip().split()))
    stations = list(map(int,sys.stdin.readline().rstrip().split()))

    distances = dijkstra(fires, stations)
    answer = 0
    for fire in fires :
        answer += distances[fire]

    print(answer)


# vertex가 최대 1000개, edge가 최대 100만개이다.
# 다익스트라를 여러번 쓰면 시간초과가 나기에 한번의 다익스트라로 풀 수 있는 방법을 생각해봤다.

# 일반 vertex를 만나면 기본 다익스트라에서와 같이
# 현재 vertex까지의 cost와 두 간선의 cost를 더한 값이 다음 vertex가 지금 갖고 있는 dist보다 큰지 작은지를 비교해서 할당하면 된다.
# 하지만 소방서 vertex를 만난다면 소방서 vertex의 dist는 0이어야 한다.
# 그렇기에 처음 만난 소방서라면 우선순위큐에 넣어준다. 그럼 자동으로 이미 계산된 거리보다 두번째 소방서에서 더 가까운 거리는 알고리즘에 의해 갱신되게 된다.

# 책의 해설로는 시작을 소방서 한 지점에서 하는게 아니라 모든 소방서에서 시작하는 것
# 그냥 초기값으로 다 넣어주면 될 듯?
