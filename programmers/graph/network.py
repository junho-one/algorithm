def solution(n, computers):

    def dfs(vertex):
        visited[vertex] = True

        for idx, con in enumerate(computers[vertex]):
            if con == 1 and not visited[idx]:
                dfs(idx)

    visited = [None] * n
    answer = 0
    for start in range(n) :
        if not visited[start] :
            dfs(start)
            answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))