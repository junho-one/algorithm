# 프로그래머스 야근 지수

from collections import defaultdict

def solution(n, works):
    answer = 0

    counter = defaultdict(int)

    for work in works :
        counter[work] += 1

    key = max(counter.keys())

    # print(counter)
    for i in range(key, -1, -1) :

        if counter[i] <= n :
            counter[i-1] += counter[i]

        else :
            counter[i-1] += n
            counter[i] -= n
            last = i
            break

        n -= counter[i]

    else :
        return 0

    for i in range(last,-1,-1) :
        answer += (counter[i] * i * i)

    return answer

print(solution(4, [4, 3, 3]))
print(solution(1,[2, 1, 2]))

# 딕셔너리 형태로 key = 야근 시간, value = 일 개수로 나타낸다.
# 그리고 max key 부터 시작해서 값이 작아지면서 해당 key에 있는 값들을 key-1로 옮긴다.
# 그러다 더 이상 옮길 수 없을 때 남은 시간의 제곱을 구한다.