def solution(n, results):

    winners = {x: set() for x in range(1, n + 1)}
    lossers = {x: set() for x in range(1, n + 1)}

    for win, loss in results:
        winners[win].add(loss)
        lossers[loss].add(win)


    # idx를 포함하고 있는 losser 나 winner를 모두 갱신시키고 다음으로 넘어가는 것
    for idx in range(1, n+1) :
        # idx를 이긴 노드들에 대해 idx가 이긴 노드들을 업데이트
        for win in lossers[idx] :
            winners[win].update(winners[idx])

        # idx에게 진 노드들에 대해 idx를 이긴 노드들을 업데이트
        for loss in winners[idx] :
            lossers[loss].update(lossers[idx])

    answer = 0
    for idx in range(1, n+1) :
        if len( winners[idx] | lossers[idx] ) == (n-1) :
            answer += 1

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
print(solution(8,[[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8]] ))



def solution(n, results):

    matrix = [[False for _ in range(n)] for _ in range(n)]

    for a,b in results :
        matrix[a-1][b-1] = True

    for i in range(n) :
        matrix[i][i] = True

    # 플로이드 와샬은 거쳐가는 노드가 기준이 된다.

    #  거쳐가는
    for t in range(n) :
        # 시작하는
        for s in range(n) :
            # 도착하는
            for e in range(n) :
                # print(matrix[s][t], matrix[t][e], (matrix[s][t] and matrix[t][e]))
                if matrix[s][t] and matrix[t][e]:
                    matrix[s][e] = True

    # 플로이드 워샬은 음수 사이클에서만 잘 안되는듯 ? (찾아내는건 가능한 듯)
    # 여기선 음수 사이클이나 a->b, b->a와 같은 상황이 절대 안일어난다.
    # 현재 위의 플로이드 워샬 알고리즘으로 정점간 연결이 가능한 점들은 모두 연결되어 있다.
    # 1,2,3,4 들이 한번에는 못가지만 몇번 거쳐 5를 가르킬 수 있게 된 것 처럼.
    # 그러니 i로 올 수 있는 정점 수와 갈 수 있는 정점 수가 n이 되면 순위가 메겨진 것
    answer = 0
    for i in range(n) :
        cnt = 0
        for j in range(n) :
            if matrix[i][j] or matrix[j][i] :
                cnt += 1

        if cnt == n :
            answer += 1

    for m in matrix :
        print(m)

    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
# print(solution(8,[[1, 2], [2, 3], [3, 4], [5, 6], [6, 7], [7, 8]] ))


