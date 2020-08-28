from collections import defaultdict, deque

def different(sent1, sent2) :
    diff = 0
    for i in range(len(sent1)) :
        if sent1[i] != sent2[i] :
            diff += 1

    if diff == 1 :
        return True
    else :
        return False

def solution(begin, target, words):

    def bfs(start) :
        queue = deque()

        visited = {}
        for w in words + [begin] :
            visited[w] = None

        queue.append((start,0))

        while queue :
            now, level = queue.popleft()

            for next in graph[now] :
                if not visited[next] :
                    queue.append((next, level+1))
                    visited[next] = level+1

        if visited.get(target) :
            return visited[target]
        else :
            return None

    graph = defaultdict(list)
    for w1 in words :
        for w2 in words:
            if different(w1, w2)  :
                graph[w1].append(w2)
                graph[w2].append(w1)

    for word in words :
        if different(word, begin) :
            graph[begin].append(word)

    answer = bfs(begin)

    if answer :
        return answer
    else :
        return 0

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
