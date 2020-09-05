# 프로그래머스 선입선출 스케쥴링

def solution(n, cores):
    answer = 0

    if n <= len(cores) :
        return n

    lo = 0
    hi = len(cores) * max(cores)

    while lo < hi:

        mid = (lo + hi) // 2

        finish = len(cores)
        for c in cores:
            finish += (mid // c)
        if n <= finish:
            hi = mid
        else:
            lo = mid + 1

        if hi == lo:
            break

    time = lo
    prevs = []
    ends = []
    for core in cores:
        ends.append(time // core + 1)

    for core in cores:
        prevs.append((time-1) // core + 1)

    diff = [ends[i]-prevs[i] for i in range(len(prevs))]

    times = sum(prevs)

    for i, d in enumerate(diff,start=1) :
        if d == 1 :
            times += 1
            if times == n :
                return i

    return "None"

print(solution(6, [1,2,3]))
print(solution(7, [1,2,3]))
print(solution(8, [1,2,3]))

# 이분탐색을 통해 n개의 작업을 모두 처리 하는 최소 시간 time을 구한다.
# (time-1)은 n개 작업을 모두 처리 못하는 최대 시간이다.
# time // core + 1을 통해 time 시간에서 각 프로세서가 작업한 개수를 구한다.
# time에서의 프로세서 작업 횟수 - time-1에서의 프로세스 작업 횟수를 구해 time시간에 작업한 프로세스들을 구함.
# 번호가 작은 프로세서부터 하나씩 추가하며 총 작업횟수가 n이 될 떄까지 구한다.
