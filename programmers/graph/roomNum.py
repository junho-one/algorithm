from collections import defaultdict

answer = 0
def solution(arrows):
    global answer
    graph = defaultdict(set)
    move = {0: (0, 1), 1: (1, 1), 2: (1, 0), 3: (1, -1), 4: (0, -1), 5: (-1, -1), 6: (-1, 0), 7: (-1, 1)}

    now = (0, 0)
    visited = {}
    visited[now] = None

    for arr in arrows:
        dx, dy = move[arr]
        next = (now[0] + dx, now[1] + dy)

        graph[now].add(next)

        now = next
        visited[next] = None

    def dfs(vertex) :
        global answer
        visited[vertex] = False

        for next in graph[vertex] :
            if next != vertex :
                if visited[next] == None  :
                    dfs(next)

                elif visited[vertex] == False :
                    answer += 1


        visited[vertex] = True

    for key in visited.keys() :
        if visited[key] == None :
            dfs(key)

    return answer

print(solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))