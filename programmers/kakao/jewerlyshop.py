# 카카오 여름인턴 3번
from collections import defaultdict

def solution(gems):
    answer = []
    length = len(gems)
    unique_num = len(set(gems))
    unique = set()
    jewerly = defaultdict(int)

    hi = 0
    for idx, gem in enumerate(gems) :
        unique.add(gem)
        jewerly[gem] += 1
        if len(unique) == unique_num :
            hi = idx
            break
    lo = 0

    if lo == hi :
        return [1,1]

    while lo != hi :
        while jewerly[gems[lo]] != 1 :
            jewerly[gems[lo]] -= 1
            lo += 1

        answer.append( (lo+1, hi+1, hi-lo+1) )

        if hi == length-1 :
            break

        hi += 1
        jewerly[gems[hi]] += 1

    answer = sorted(answer, key=lambda x : (x[2],x[0],x[1]))

    return answer[0][0], answer[0][1]


print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))