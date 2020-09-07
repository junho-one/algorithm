import heapq

def solution(distance, rocks, n):

    rocks.sort()
    rocks = [0] + rocks + [distance]

    lo = 1
    hi = 1000000000

    while lo < hi :
        mid = (lo + hi)//2
        count = n
        prev = rocks[0]

        for rock in rocks[1:] :
            gap = rock - prev

            if gap > mid :
                prev = rock
            else :
                count -= 1


        if count < 0 :
            hi = mid

        else :
            lo = mid + 1

        if lo == hi :
            return lo


print(solution(25, [2,14,11,21,17], 2))


# 이분탐색을 위한 질문으로 바꿔본다면
# 바위 간 간격의 최솟값이 x보다 크거나 같게 되는 집합이 존재하는가

# x를 찾는 거니까 x의 범위를 이분탐색으로 줄여나간다.
# x가 되는지 안되는지 판단하기 위해서 돌을 돌면서 간격이 x보다 작으면 뒤에 있는 돌을 없앤다.
# 만약 n번 지우고도 x보다 작은 간격이 있다면 그 x는 조건에 맞지 않는 값이다.

# rocks는 5만이니까 매번 n의 탐색이 가능하다.
# 돌사이의 거리는 1~10억까지 가능하니 이 값을 이분탐색으로 줄여나가야 한다.
