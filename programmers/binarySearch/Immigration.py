# 프로그래머스 입국심사
# 이분 탐색 문제에서는 xxxxxxxxxooooooooo를 생각하자

# 캐치해야할 사항은 심사관은 모두 같은 시간을 할당받는다.
# 거기서 모두가 할당 받는 시간에서 각 심사관들은 몇명을 처리하는가.
# 이렇게 처리하는 사람의 수가 n을 넘으면서 가장 작은 수가 될 떄는 언제인가.

# 시간 축---------- 이라면
# xxxxxxxxooooooo 되는 시점. 처음 o가 나오는 곳을 찾아야 함.

def solution(n, times):
    answer = 0

    # 가장 적게 걸리는 시간, 가장 많이 걸리는 시간
    lo = 1
    hi = max(times) * n

    while lo <= hi :
        mid = (lo+hi)//2
        finish = 0
        for t in times :
            finish += (mid // t)

        # 여기서 mid가 정답일 수도 있고, 아닐 수도 있다.
        if n <= finish :
            hi = mid -1
            answer = mid

        # 이경우에는 mid가 x이니 무조건 답이 아니다. mid+1부터 답이 될 가능성이 있다.
        else :
            lo = mid + 1


    return answer

# 이분 탐색 코드 작성시 주의할 점은 무한 루프에 빠지지 않도록 하여야 함
# 27, 28이라면 27+28 // 2 는 계속해서 27이 나온다. 그렇기에 lo = mid로만 넣으면 안되고 +1을 해줘야 함
print(solution(6,[7,10]))

# 이 코드로 해도 성공
# xxxxxxxxooooooo
# mid가 o이면 hi를 mid로 옮김. x면 mid는 아니니 mid+1로 옮김.
# mid가 x 일 때만 옮기면서 점치 lo를 커지게 해서 lo == hi가 되면 그게 정답
def solution(n, times):
    lo = 1
    hi = max(times) * n

    while lo < hi :
        mid = (lo+hi)//2
        finish = 0
        for t in times :
            finish += (mid // t)
        if n <= finish :
            hi = mid
        else :
            lo = mid + 1

        # 이 코드가 없으면 x가 lo=28이고 o가 hi=29일 때 mid는 28로 x이다.
        # 그런데 위 코드에서 mid+1이 lo가 되면서 lo == hi가 같아지지만 mid 는 28이다. 그래서 밑에 코드를 추가해 줘야 함.
        if lo == hi :
            return lo

    return None


print(solution(6,[7,10]))


# 기본 bin search
# def binary_search(target, data):
#     data.sort()
#     start = 0
#     end = len(data) - 1
#
#     while start <= end:
#         mid = (start + end) // 2
#
#         if data[mid] == target:
#             return mid # 함수를 끝내버린다.
#         elif data[mid] < target:
#             start = mid + 1
#         else:
#             end = mid -1
#
#     return None