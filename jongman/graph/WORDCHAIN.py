import sys
import copy

def dfs(word, vertex) :
    print(word, vertex, graph[vertex])
    for next, next_word in graph[vertex] :
        if visited.get(vertex,next) and visited[vertex,next] :
            visited[vertex,next] = False
            dfs(next_word, next)

    print(word)

T = int(sys.stdin.readline().rstrip())


for _ in range(T) :
    N = int(sys.stdin.readline().rstrip())
    words = {}
    graph = {}
    in_edge = {}
    out_edge = {}
    visited = {}

    for _ in range(N) :
        word = sys.stdin.readline().rstrip()

        if graph.get(word[0]):
            graph[word[0]].add((word[-1],word))
        else :
            graph[word[0]] = set()
            graph[word[0]].add((word[-1],word))


        if in_edge.get(word[-1]) :
            in_edge[word[-1]] += 1
        else :
            in_edge[word[-1]] = 1

        if out_edge.get(word[0]):
            out_edge[word[0]] += 1
        else:
            out_edge[word[0]] = 1

        visited[(word[0], word[-1])] = True

    in_key = list(sorted(in_edge.keys()))
    out_key = list(sorted(out_edge.keys()))

    print(in_edge, out_edge)
    if in_key == out_key :

        candidates_start = []
        candidates_end = []
        for char in in_key :

            if out_edge[char] != in_edge[char] :
                if out_edge[char] - in_edge[char] == 1 :
                    candidates_start.append(char)
                elif in_edge[char] - out_edge[char] == 1 :
                    candidates_end.append(char)
                else :
                    print("IMPOSSIBLE")
                    break

        else :

            if len(candidates_start) == 1 and len(candidates_end) == 1 :
                graph[candidates_end[0]] = set()
                graph[candidates_end[0]].add((candidates_start[0],""))
                visited[candidates_end[0], candidates_start[0]] = True
                dfs("",candidates_start[0])

            elif len(candidates_start) == 0 and len(candidates_end) == 0 :
                print("SUCK")

                dfs("",in_key[0])

            else :
                print("IMPOSSIBLE")

    else :
        print("IMPOSSIBLE")