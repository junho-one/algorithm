import sys
import copy

def dfs(vertex, word) :
    # print(vertex, graph[vertex])

    while graph[vertex] :
        next_vertex, next_word = graph[vertex].pop()
        # print(next_vertex, next_word)
        dfs(next_vertex, next_word)

    answer.append(word)


T = int(sys.stdin.readline().rstrip())

for _ in range(T) :
    N = int(sys.stdin.readline().rstrip())
    words = {}
    graph = {}
    in_edge = {}
    out_edge = {}
    visited = {}

    for alphabet in 'abcdefghijklmnopqrstuvwxyz' :
        graph[alphabet] = []
        in_edge[alphabet] = 0
        out_edge[alphabet] = 0

    for _ in range(N) :
        word = sys.stdin.readline().rstrip()

        graph[word[0]].append((word[-1],word))
        in_edge[word[-1]] += 1
        out_edge[word[0]] += 1


    answer = []

    candidates = []
    for alphabet in 'abcdefghijklmnopqrstuvwxyz' :
        # print(in_edge[alphabet], out_edge[alphabet])
        if in_edge[alphabet] != out_edge[alphabet] :
            candidates.append(alphabet)

    if len(candidates) == 2 :

        start = None
        end = None

        for alphabet in candidates:
            if in_edge[alphabet]+1 == out_edge[alphabet] :
                start = alphabet

            if in_edge[alphabet] == out_edge[alphabet]+1 :
                end = alphabet

        if start and end :
            # print("?")
            # graph[end].append((start, ""))
            # 문제 해설에서는 끝점과 시작점을 연결하는 엣지를 연결해야 한다고 하는데
            # 이런 간선 넣으면 두번째 예제에서 'aa', '', 'bb', 'ab' => ab bb aa로 되는 에러가 발생하는 듯.
            dfs(start,"")

    elif len(candidates) == 0 :
        for alphabet in 'abcdefghijklmnopqrstuvwxyz' :
            # print(alphabet)
            if in_edge[alphabet] is not 0 :
                # print("HINH")
                dfs(alphabet,"")
                break


    if answer :
        print( " ".join(reversed(answer)).strip())
    else :
        print("IMPOSSIBLE")

