import heapq

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

def dijkstra(graph, start) :

    distances = {node : float('inf') for node in graph}
    distances[start] = 0

    heap = []

    heapq.heappush(heap, (distances[start], start))

    while heap :
        now_dist, now_node = heapq.heappop(heap)

        if distances[now_node] < now_dist :
            continue

        for adjacent, weight in graph[now_node].items() :
            distance = now_dist + weight

            if distance < distances[adjacent] :
                distances[adjacent] = distance
                heapq.heappush(heap, (distance, adjacent))

    return distances

print(dijkstra(mygraph, 'A'))