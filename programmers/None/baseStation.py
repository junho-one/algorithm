# 프로그래머스 기지국 설치
import math

def solution(N, stations, w):
    starts = []
    ends = []
    prev_end = -float("inf")

    for station in stations:
        start = station - w
        end = station + w

        if prev_end < start:
            starts.append(start)
            ends.append(prev_end)

        prev_end = end

    if ends:
        ends.pop(0)
        ends.append(prev_end)

    else:
        starts = [stations[0] - w]
        ends = [stations[-1] + w]

    bases = list(zip(starts, ends))
    answer = 0
    cover = 1 + 2 * w
    until = 0
    for start, end in bases:

        if start - until > 1:
            answer += math.ceil((start - until - 1) / cover)

        until = end

    if until < N:
        answer += math.ceil((N - until) / cover)

    return answer

# print(solution(11, [4, 7, 11], 1))
# print(solution(11, [1, 8], 3))
print(solution(11, [], 3))

# 현재 5G로 커버하는 범위를 구한 뒤, 못커버하는 구간은
# (5G가 안닿는 집의 개수 / 5G 한개가 커버하는 집의 수)를 올림하면 필요한 5G 기지국 개수가 된다.
