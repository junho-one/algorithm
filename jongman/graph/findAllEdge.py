def dfs2(here) :
    global cnt
    discovered[here] = cnt
    cnt += 1

    for next in graph[here] :

        if discovered[next] == -1 :
            # tree edge
            dfs2(next)

        elif discovered[here] < discovered[next] :
            # forward edge

        elif discovered[here] > discovered[next] and finished[next] == 0 :
            # back edge

        elif discovered[here] > discovered[next] and finished[next] == 1 :
            # cross edge

    finished[here] = 1

    