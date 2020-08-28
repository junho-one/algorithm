# 프로그래머스 외벽 점검
def solution(n, weak, dist):

    def dfs(widx) :
        if widx == len(weak) :
            answer.append( sum(1 for i in used if i == None) )
            return True

        for d in range(D) :
            if used[d] :
                start = widx
                distance = used[d]
                while widx < len(weak):
                    if distance >= weak[widx] - weak[start]:
                        widx += 1
                    else :
                        break
                used[d] = None
                dfs(widx)
                used[d] = distance
                widx = start

    weaks = []
    for i in range(len(weak)):
        weaks.append( weak[i:] + list(map(lambda x : x+n, weak[:i])) )

    dist = sorted(dist, reverse=True)
    D = len(dist)
    answer = []

    for weak in weaks :
        used = list(dist)
        dfs(0)

    if answer :
        return min(answer)
    else :
        return -1
print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 5, 6, 10], [1, 2]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
